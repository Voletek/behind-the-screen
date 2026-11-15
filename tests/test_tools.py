#!/usr/bin/env python3
"""Unit tests for the tools (standard library unittest).  Run:  python3 -m unittest discover -s tests"""

import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
FIX = os.path.join(ROOT, "tests", "fixtures")
sys.path.insert(0, TOOLS)


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(TOOLS, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


roll = load("roll", "roll.py")
validate = load("validate_campaign", "validate-campaign.py")
encounter = load("encounter", "encounter.py")
bundle = load("build_bundle", "build-bundle.py")
checkrepo = load("check_repo", "check-repo.py")
character = load("character", "character.py")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def run(fn, argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = fn(argv)
    return code, out.getvalue(), err.getvalue()


class TestRoll(unittest.TestCase):
    def roll_json(self, *argv):
        code, out, _ = run(roll.main, list(argv) + ["--json"])
        self.assertEqual(code, 0)
        return json.loads(out.strip().splitlines()[0])

    def test_sum_with_record_and_dc(self):
        res = self.roll_json("1d20+5", "--record", "10", "--dc", "15")
        self.assertEqual(res["total"], 15)
        self.assertEqual(res["outcome"], "success")
        self.assertEqual(res["log"]["source"], "player")

    def test_advantage_keeps_highest(self):
        res = self.roll_json("2d20kh1+2", "--record", "3,17")
        self.assertEqual(res["total"], 19)

    def test_disadvantage_keeps_lowest(self):
        res = self.roll_json("2d20kl1", "--record", "3,17")
        self.assertEqual(res["total"], 3)
        self.assertEqual(res.get("natural"), 3)

    def test_natural_20_note(self):
        res = self.roll_json("1d20+1", "--record", "20")
        self.assertEqual(res["note"], "natural 20")

    def test_drop_lowest(self):
        res = self.roll_json("4d6dl1", "--record", "1,4,5,6")
        self.assertEqual(res["total"], 15)

    def test_pool_successes_vs_ob(self):
        res = self.roll_json("5d6>=4", "--record", "1,4,6,3,5", "--ob", "3")
        self.assertEqual(res["successes"], 3)
        self.assertEqual(res["outcome"], "success")

    def test_pool_explodes_sixes(self):
        # the first die shows 6 and explodes into the next value (2); then the second die (5)
        res = self.roll_json("2d6>=4!", "--record", "6,2,5")
        self.assertEqual(res["terms"][0]["dice"], [6, 2, 5])
        self.assertEqual(res["successes"], 2)

    def test_pbta_bands(self):
        self.assertEqual(self.roll_json("pbta+1", "--record", "5,4")["outcome"], "full success")
        self.assertEqual(self.roll_json("pbta+1", "--record", "3,3")["outcome"], "partial success")
        self.assertEqual(self.roll_json("pbta+0", "--record", "1,5")["outcome"], "miss")
        self.assertEqual(self.roll_json("pbta+2", "--record", "6,4", "--crit", "12")["outcome"], "critical")

    def test_d616_marvel_die_one_is_six_and_fantastic(self):
        res = self.roll_json("d616+3", "--record", "2,5,1", "--tn", "16")
        self.assertTrue(res["fantastic"])
        self.assertEqual(res["total"], 2 + 5 + 6 + 3)
        self.assertEqual(res["outcome"], "success")

    def test_d616_ultimate_fantastic(self):
        res = self.roll_json("d616", "--record", "6,6,1")
        self.assertTrue(res["ultimate_fantastic"])

    def test_d616_edge_rerolls_lowest_keeps_better(self):
        res = self.roll_json("d616", "--record", "1,4,5,6", "--edge", "1")
        self.assertEqual(res["terms"][0]["dice"][0], 6)
        self.assertEqual(res["total"], 15)

    def test_d616_trouble_keeps_worse(self):
        res = self.roll_json("d616", "--record", "6,2,3,1", "--trouble", "1")
        self.assertEqual(res["total"], 1 + 2 + 3)

    def test_percentile_under(self):
        self.assertEqual(self.roll_json("1d100", "--record", "45", "--under", "45")["outcome"], "success")
        self.assertEqual(self.roll_json("1d100", "--record", "46", "--under", "45")["outcome"], "failure")

    def test_fate_dice(self):
        res = self.roll_json("4dF+1", "--record", "1,0,-1,1")
        self.assertEqual(res["total"], 2)

    def test_bad_expressions(self):
        for expr in ("3x", "1d1", "d20 d20"):
            code, _, _ = run(roll.main, [expr])
            self.assertEqual(code, 2, expr)

    def test_record_value_out_of_range(self):
        code, _, err = run(roll.main, ["1d20", "--record", "21"])
        self.assertEqual(code, 2)
        self.assertIn("not possible", err)

    def test_record_unused_values(self):
        code, _, _ = run(roll.main, ["1d20", "--record", "5,6"])
        self.assertEqual(code, 2)

    def test_log_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "dice-log.jsonl")
            run(roll.main, ["1d20+2", "--seed", "7", "--who", "Ada", "--session", "3", "--log", path])
            entry = json.loads(read(path).strip())
            for key in ("ts", "expr", "total", "source", "seed"):
                self.assertIn(key, entry)
            self.assertEqual(entry["who"], "Ada")
            self.assertEqual(entry["session"], 3)

    def test_player_reported_total(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "dice-log.jsonl")
            code, out, _ = run(roll.main, ["1d20+5", "--total", "19", "--dc", "15", "--who", "Lyra", "--log", path])
            self.assertEqual(code, 0)
            self.assertIn("player's roll", out)
            entry = json.loads(read(path).strip())
            self.assertEqual(entry["source"], "player")
            self.assertEqual(entry["outcome"], "success")
            self.assertIsNone(entry["dice"])

    def test_player_reported_total_pbta(self):
        res = self.roll_json("pbta+2", "--total", "8")
        self.assertEqual(res["outcome"], "partial success")

    def test_request_does_not_roll_or_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "dice-log.jsonl")
            code, out, err = run(roll.main, ["1d20+5", "--request", "--who", "Lyra", "--why", "Stealth",
                                             "--dc", "15", "--stakes", "someone hears you", "--log", path])
            self.assertEqual(code, 0)
            self.assertIn("roll your dice", out)
            self.assertNotIn("15", out)          # target stays with the GM
            self.assertIn("DC 15", err)
            self.assertFalse(os.path.exists(path))

    def test_seed_is_deterministic(self):
        a = self.roll_json("3d6", "--seed", "42")["total"]
        b = self.roll_json("3d6", "--seed", "42")["total"]
        self.assertEqual(a, b)


class TestValidateCampaign(unittest.TestCase):
    def report(self, *paths):
        rep = validate.Report()
        for kind, p in validate.discover(list(paths)):
            if kind == "folder":
                validate.validate_folder(rep, p)
            elif kind == "file":
                validate.validate_file(rep, p)
        return rep

    def test_valid_fixture_campaign(self):
        rep = self.report(os.path.join(FIX, "valid-campaign"))
        self.assertEqual(rep.count("FAIL"), 0, rep.items)
        msgs = " ".join(m for _, _, m in rep.items)
        self.assertIn("retired term 'Old Town'", msgs)

    def test_broken_state(self):
        rep = self.report(os.path.join(FIX, "broken-state.json"))
        msgs = " | ".join(m for l, _, m in rep.items if l == "FAIL")
        for needle in ("schema must be", "session must be >= 0", "exceeds max", "duplicate id",
                       "status 'zombified'", "filled must be", "status 'maybe'", "exhaustion above 6"):
            self.assertIn(needle, msgs)
        warns = " | ".join(m for l, _, m in rep.items if l == "WARN")
        self.assertIn("stat 'Strength'", warns)
        self.assertIn("condition 'Sleepy'", warns)

    def test_save_block(self):
        rep = self.report(os.path.join(FIX, "save-block.md"))
        self.assertEqual(rep.count("FAIL"), 0, rep.items)

    def test_dice_log(self):
        rep = self.report(os.path.join(FIX, "bad-dice-log.jsonl"))
        self.assertEqual(rep.count("FAIL"), 2, rep.items)

    def test_missing_session_headings(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, "sessions"))
            with open(os.path.join(tmp, "state.json"), "w") as fh:
                json.dump({"schema": "behind-the-screen/state@1", "campaign": "x", "system": "root",
                           "session": 1, "party": [{"id": "a", "name": "A"}]}, fh)
            with open(os.path.join(tmp, "BIBLE.md"), "w") as fh:
                fh.write("# B\n## Premise\nx\n")
            with open(os.path.join(tmp, "sessions", "session-01.md"), "w") as fh:
                fh.write("# S\n## Recap\nx\n")
            rep = validate.Report()
            validate.validate_folder(rep, tmp)
            msgs = " | ".join(m for l, _, m in rep.items if l == "FAIL")
            self.assertIn("missing required heading", msgs)
            self.assertIn("missing ## Safety", msgs)

    def test_examples_are_valid(self):
        code, out, _ = run(validate.main, [os.path.join(ROOT, "examples")])
        self.assertEqual(code, 0, out)

    def test_hook_mode_always_exits_zero(self):
        code, _, _ = run(validate.main, ["--hook", os.path.join(FIX, "broken-state.json")])
        self.assertEqual(code, 0)


class TestCharacter(unittest.TestCase):
    def campaign(self, tmp):
        import shutil
        dst = os.path.join(tmp, "c")
        shutil.copytree(os.path.join(FIX, "valid-campaign"), dst)
        return dst

    def test_new_and_check_point_buy(self):
        with tempfile.TemporaryDirectory() as tmp:
            c = self.campaign(tmp)
            stats = ["STR=8", "DEX=15", "CON=14", "INT=10", "WIS=14", "CHA=10"]
            argv = ["new", "--campaign", c, "--id", "lyra", "--name", "Lyra", "--player", "Kira", "--method", "point_buy"]
            for st in stats:
                argv += ["--stat", st]
            self.assertEqual(run(character.main, argv)[0], 0)
            self.assertTrue(os.path.exists(os.path.join(c, "characters", "lyra.md")))
            code, out, _ = run(character.main, ["check", "--campaign", c, "--id", "lyra"])
            self.assertEqual(code, 0, out)
            state = json.loads(read(os.path.join(c, "state.json")))
            self.assertEqual(state["party"][-1]["sheet"], "characters/lyra.md")
            # validator agrees
            self.assertEqual(run(validate.main, [c])[0], 0)

    def test_point_buy_overspent_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            c = self.campaign(tmp)
            argv = ["new", "--campaign", c, "--id", "max", "--name", "Max", "--method", "point_buy"]
            for st in ["STR=15", "DEX=15", "CON=15", "INT=10", "WIS=10", "CHA=10"]:
                argv += ["--stat", st]
            run(character.main, argv)
            code, out, _ = run(character.main, ["check", "--campaign", c, "--id", "max"])
            self.assertEqual(code, 1)
            self.assertIn("spent 33 of 27", out)

    def test_standard_array_and_sheet_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            c = self.campaign(tmp)
            argv = ["new", "--campaign", c, "--id", "sam", "--name", "Sam", "--method", "standard_array"]
            for st in ["STR=15", "DEX=14", "CON=13", "INT=12", "WIS=10", "CHA=8"]:
                argv += ["--stat", st]
            run(character.main, argv)
            self.assertEqual(run(character.main, ["check", "--campaign", c, "--id", "sam"])[0], 0)
            sheet = os.path.join(c, "characters", "sam.md")
            text = read(sheet).replace("- STR: 15", "- STR: 16")
            with open(sheet, "w", encoding="utf-8") as fh:
                fh.write(text)
            code, out, _ = run(character.main, ["check", "--campaign", c, "--id", "sam"])
            self.assertEqual(code, 1)
            self.assertIn("STR is 16 on the sheet", out)

    def test_unknown_stat_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            c = self.campaign(tmp)
            with self.assertRaises(SystemExit):
                run(character.main, ["new", "--campaign", c, "--id", "x", "--name", "X", "--stat", "Strength=10"])

    def test_missing_sheet_fails_validator(self):
        with tempfile.TemporaryDirectory() as tmp:
            c = self.campaign(tmp)
            path = os.path.join(c, "state.json")
            state = json.loads(read(path))
            state["party"][0]["sheet"] = "characters/nobody.md"
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(state, fh)
            code, out, _ = run(validate.main, [c])
            self.assertEqual(code, 1)
            self.assertIn("character sheet", out)

    def test_methods_listing(self):
        code, out, _ = run(character.main, ["methods", "--system", "dnd-5e"])
        self.assertEqual(code, 0)
        self.assertIn("point_buy", out)
        self.assertIn("4d6dl1", out)


class TestEncounter(unittest.TestCase):
    def test_srd_budget_examples(self):
        # SRD 5.2.1 worked examples: 4 x level 1 low = 200; 5 x level 3 moderate = 1,125; 6 x level 15 high = 46,800
        self.assertEqual(encounter.budgets([1] * 4)["Low"], 200)
        self.assertEqual(encounter.budgets([3] * 5)["Moderate"], 1125)
        self.assertEqual(encounter.budgets([15] * 6)["High"], 46800)

    def test_rating(self):
        code, out, _ = run(encounter.main, ["--party", "4x3", "--creatures", "cr3,cr1/4x4", "--json"])
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["spent"], 900)
        self.assertEqual(data["difficulty"], "Moderate")

    def test_mixed_party_and_xp_entries(self):
        code, out, _ = run(encounter.main, ["--party", "3,4", "--creatures", "xp100x2", "--json"])
        data = json.loads(out)
        self.assertEqual(data["budgets"]["Low"], 150 + 250)
        self.assertEqual(data["difficulty"], "Low")

    def test_bad_input(self):
        self.assertEqual(run(encounter.main, ["--party", "4x21"])[0], 2)
        self.assertEqual(run(encounter.main, ["--party", "4x3", "--creatures", "dragon"])[0], 2)


class TestBundleAndRepo(unittest.TestCase):
    def test_bundle_for_campaign(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "b.md")
            code, _, err = run(bundle.main, ["--campaign", os.path.join(ROOT, "examples", "campaigns", "fractured-shadows"), "-o", out])
            self.assertEqual(code, 0)
            text = read(out)
            for needle in ("Game Master Boot Prompt", "Game Master Tenets", "Rules-Light Engine",
                           "Fractured Shadows — Campaign Bible", "behind-the-screen/state@1", "Session 01",
                           "Character Creation and Customization", "# Rikan Tunnelsprint", "Players roll their own dice"):
                self.assertIn(needle, text)
            self.assertNotIn("Session Zero — Choosing the Game", text)
            self.assertIn("characters", err)

    def test_bundle_new_game_includes_session_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "b.md")
            run(bundle.main, ["--system", "mouse-guard", "--lean", "-o", out])
            text = read(out)
            self.assertIn("Session Zero — Choosing the Game", text)
            self.assertNotIn("NPC Voice — Designing", text)

    def test_check_repo_passes(self):
        code, out, _ = run(checkrepo.main, ["--root", ROOT])
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()

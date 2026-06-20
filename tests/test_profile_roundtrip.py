from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from contractor_bid.profile import build_profile, load_profile, render_skill, write_profile


class ProfileRoundTripTest(unittest.TestCase):
    def test_starter_profiles_render_committed_skills(self) -> None:
        root = Path(__file__).resolve().parents[1]
        for profile_path in sorted((root / "profiles").glob("*.json")):
            with self.subTest(profile=profile_path.name):
                profile = load_profile(profile_path, root)
                skill_path = root / "skills" / f"{profile['profile_id']}-bid-scope" / "SKILL.md"
                self.assertEqual(render_skill(profile), skill_path.read_text(encoding="utf-8"))

    def test_generated_profile_preserves_custom_scope_rule(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = build_profile(
                company_name="Example Sub",
                trade_name="Example Scope",
                profile_id="example-scope",
                skill_description="Custom skill description.",
                scope_rule="Carry only the approved example scope.",
            )
            profile_file, skill_file = write_profile(root, profile)

            loaded = load_profile(profile_file, root)
            self.assertEqual(loaded["scope_rule"], "Carry only the approved example scope.")
            self.assertEqual(loaded["skill_description"], "Custom skill description.")
            self.assertIn("Carry only the approved example scope.", skill_file.read_text())
            self.assertIn("description: Custom skill description.", skill_file.read_text())


if __name__ == "__main__":
    unittest.main()

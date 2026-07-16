from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class EntryLayoutTests(unittest.TestCase):
    def test_entry_titles_use_compact_responsive_scale(self) -> None:
        stylesheet = (ROOT / "assets/css/style.css").read_text(encoding="utf-8")

        self.assertIn("font-size: clamp(40px, 5vw, 58px)", stylesheet)
        self.assertIn("font-size: clamp(34px, 9vw, 40px)", stylesheet)


if __name__ == "__main__":
    unittest.main()

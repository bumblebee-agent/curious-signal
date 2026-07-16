from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class EntryLayoutTests(unittest.TestCase):
    def test_entry_titles_use_compact_responsive_scale(self) -> None:
        stylesheet = (ROOT / "assets/css/style.css").read_text(encoding="utf-8")

        self.assertIn("font-size: clamp(40px, 5vw, 58px)", stylesheet)
        self.assertIn("font-size: clamp(34px, 9vw, 40px)", stylesheet)

    def test_composite_morning_brief_links_to_grouped_sources(self) -> None:
        layout = (ROOT / "_layouts" / "entry.html").read_text(encoding="utf-8")

        self.assertIn('{% if page.section_slug == "morning-brief" %}', layout)
        self.assertIn('href="#sources">View sources ↓</a>', layout)
        self.assertIn("{% elsif page.primary_source %}", layout)
        self.assertIn("Primary source ↗", layout)


if __name__ == "__main__":
    unittest.main()

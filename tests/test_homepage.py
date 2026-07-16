from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HomepageLatestListenTests(unittest.TestCase):
    def test_latest_listen_uses_newest_morning_brief(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")

        self.assertIn(
            "{% assign featured = sorted_entries | where: 'section_slug', "
            "'morning-brief' | first %}",
            homepage,
        )
        self.assertNotIn("where: 'featured', true", homepage)

    def test_newest_morning_brief_has_playable_audio_metadata(self) -> None:
        morning_briefs: list[tuple[str, dict[str, str]]] = []
        for path in (ROOT / "_entries").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                continue
            front_matter = text.split("\n---\n", 1)[0].removeprefix("---\n")
            metadata = {
                key.strip(): value.strip().strip('"')
                for line in front_matter.splitlines()
                if ":" in line
                for key, value in [line.split(":", 1)]
            }
            if metadata.get("section_slug") == "morning-brief":
                morning_briefs.append((metadata["date"], metadata))

        self.assertTrue(morning_briefs)
        _, newest = max(morning_briefs, key=lambda item: item[0])
        self.assertTrue(newest.get("audio", "").endswith(".mp3"))
        self.assertTrue(newest.get("duration"))


if __name__ == "__main__":
    unittest.main()

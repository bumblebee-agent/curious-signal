from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


HOMEPAGE_FILTER_HARNESS = r"""
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

function element(dataset = {}) {
  const listeners = {};
  const classes = new Set();
  return {
    dataset,
    hidden: false,
    attributes: {},
    addEventListener(type, listener) { listeners[type] = listener; },
    dispatch(type) { assert.ok(listeners[type], `missing ${type} listener`); listeners[type](); },
    setAttribute(name, value) { this.attributes[name] = value; },
    classList: {
      toggle(name, enabled) {
        if (enabled) classes.add(name);
        else classes.delete(name);
      },
      contains(name) { return classes.has(name); },
    },
  };
}

const cards = [
  element({ section: "daily-news", search: "daily" }),
  element({ section: "morning-brief", search: "morning" }),
  element({ section: "research-summary", search: "summary" }),
  element({ section: "deep-research", search: "deep" }),
];
const groups = cards.map((card) => ({
  hidden: false,
  querySelector(selector) {
    assert.equal(selector, ".entry-card:not([hidden])");
    return card.hidden ? null : card;
  },
}));
const buttons = ["all", "daily-news", "morning-brief", "research-summary", "deep-research"]
  .map((filter) => element({ filter }));

const document = {
  querySelectorAll(selector) {
    if (selector === ".entry-card") return cards;
    if (selector === ".archive-group, .recent-group") return groups;
    if (selector === "[data-filter]") return buttons;
    return [];
  },
  querySelector() { return null; },
};

vm.runInNewContext(fs.readFileSync(process.argv[1], "utf8"), { document });
buttons[3].dispatch("click");

assert.deepEqual(cards.map((card) => card.hidden), [true, true, false, true]);
assert.deepEqual(groups.map((group) => group.hidden), [true, true, false, true]);
assert.deepEqual(buttons.map((button) => button.attributes["aria-pressed"]),
  ["false", "false", "false", "true", "false"]);
assert.equal(buttons[3].classList.contains("is-active"), true);
"""


class FilterInteractionTests(unittest.TestCase):
    def test_homepage_filtering_does_not_require_archive_search(self) -> None:
        result = subprocess.run(
            [
                "node",
                "-e",
                HOMEPAGE_FILTER_HARNESS,
                str(ROOT / "assets" / "js" / "archive.js"),
            ],
            capture_output=True,
            check=False,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)


if __name__ == "__main__":
    unittest.main()

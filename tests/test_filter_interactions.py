from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


DOM_HARNESS = r"""
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
    value: "",
    textContent: "",
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

function group(cards) {
  return {
    hidden: false,
    querySelector(selector) {
      assert.equal(selector, ".entry-card:not([hidden])");
      return cards.find((card) => !card.hidden) || null;
    },
  };
}

function runPage({ cards, groups, buttons, search = null, status = null }) {
  const document = {
    querySelectorAll(selector) {
      if (selector === ".entry-card") return cards;
      if (selector === ".archive-group, .recent-group") return groups;
      if (selector === "[data-filter]") return buttons;
      return [];
    },
    querySelector(selector) {
      if (selector === "#archive-search") return search;
      if (selector === "#archive-status") return status;
      return null;
    },
  };
  vm.runInNewContext(fs.readFileSync(process.argv[1], "utf8"), { document });
}
"""


HOMEPAGE_FILTER_HARNESS = DOM_HARNESS + r"""
const cards = [
  element({ section: "daily-news", search: "daily" }),
  element({ section: "morning-brief", search: "morning" }),
  element({ section: "research-summary", search: "summary" }),
  element({ section: "deep-research", search: "deep" }),
];
const groups = cards.map((card) => group([card]));
const buttons = ["all", "daily-news", "morning-brief", "research-summary", "deep-research"]
  .map((filter) => element({ filter }));

runPage({ cards, groups, buttons });
buttons[3].dispatch("click");

assert.deepEqual(cards.map((card) => card.hidden), [true, true, false, true]);
assert.deepEqual(groups.map((group) => group.hidden), [true, true, false, true]);
assert.deepEqual(buttons.map((button) => button.attributes["aria-pressed"]),
  ["false", "false", "false", "true", "false"]);
assert.equal(buttons[3].classList.contains("is-active"), true);
"""


ARCHIVE_FILTER_HARNESS = DOM_HARNESS + r"""
const cards = [
  element({ section: "daily-news", search: "daily alpha" }),
  element({ section: "research-summary", search: "research alpha" }),
  element({ section: "daily-news", search: "daily beta" }),
];
const groups = [group(cards), group(cards.slice(0, 2)), group(cards.slice(2))];
const buttons = ["all", "daily-news", "research-summary"]
  .map((filter) => element({ filter }));
const search = element();
const status = element();

runPage({ cards, groups, buttons, search, status });
assert.equal(status.textContent, "3 editions");

buttons[1].dispatch("click");
assert.deepEqual(cards.map((card) => card.hidden), [false, true, false]);
assert.deepEqual(groups.map((group) => group.hidden), [false, false, false]);
assert.equal(status.textContent, "2 editions found");

search.value = "beta";
search.dispatch("input");
assert.deepEqual(cards.map((card) => card.hidden), [true, true, false]);
assert.deepEqual(groups.map((group) => group.hidden), [false, true, false]);
assert.equal(status.textContent, "1 edition found");

buttons[2].dispatch("click");
assert.deepEqual(cards.map((card) => card.hidden), [true, true, true]);
assert.deepEqual(groups.map((group) => group.hidden), [true, true, true]);
assert.equal(status.textContent, "0 editions found");
"""


class FilterInteractionTests(unittest.TestCase):
    def run_harness(self, harness: str) -> None:
        result = subprocess.run(
            ["node", "-e", harness, str(ROOT / "assets" / "js" / "archive.js")],
            capture_output=True,
            check=False,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_homepage_filtering_does_not_require_archive_search(self) -> None:
        self.run_harness(HOMEPAGE_FILTER_HARNESS)

    def test_archive_combines_type_filter_search_groups_and_status(self) -> None:
        self.run_harness(ARCHIVE_FILTER_HARNESS)


if __name__ == "__main__":
    unittest.main()

(function () {
  const cards = Array.from(document.querySelectorAll(".entry-card"));
  const groups = Array.from(document.querySelectorAll(".archive-group"));
  const buttons = Array.from(document.querySelectorAll("[data-filter]"));
  const search = document.querySelector("#archive-search");
  const status = document.querySelector("#archive-status");

  if (!cards.length || !buttons.length || !search || !status) return;

  let activeFilter = "all";

  function applyFilters() {
    const query = search.value.trim().toLowerCase();
    let visibleCount = 0;

    cards.forEach((card) => {
      const sectionMatches = activeFilter === "all" || card.dataset.section === activeFilter;
      const textMatches = !query || card.dataset.search.includes(query);
      const visible = sectionMatches && textMatches;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    groups.forEach((group) => {
      group.hidden = !group.querySelector(".entry-card:not([hidden])");
    });

    status.textContent = visibleCount === cards.length && !query && activeFilter === "all"
      ? `${visibleCount} editions`
      : `${visibleCount} ${visibleCount === 1 ? "edition" : "editions"} found`;
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      activeFilter = button.dataset.filter;
      buttons.forEach((candidate) => {
        const selected = candidate === button;
        candidate.classList.toggle("is-active", selected);
        candidate.setAttribute("aria-pressed", String(selected));
      });
      applyFilters();
    });
  });

  search.addEventListener("input", applyFilters);
  applyFilters();
}());

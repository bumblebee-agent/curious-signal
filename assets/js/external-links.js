document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("a[href]").forEach((link) => {
    let destination;
    try {
      destination = new URL(link.href, window.location.href);
    } catch {
      return;
    }

    if (
      destination.origin === window.location.origin ||
      (destination.protocol !== "http:" && destination.protocol !== "https:")
    ) {
      return;
    }

    link.target = "_blank";
    link.relList.add("noopener", "noreferrer");
  });
});

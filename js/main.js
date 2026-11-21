(function () {
  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");

  var stored = null;
  try {
    stored = localStorage.getItem("theme");
  } catch (err) {
    stored = null;
  }
  var requested = new URLSearchParams(window.location.search).get("theme");
  if (requested === "dark" || requested === "light") stored = requested;

  function systemTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function currentTheme() {
    return root.getAttribute("data-theme") || systemTheme();
  }

  function paintChrome(theme) {
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", theme === "dark" ? "#1c1b19" : "#f7f5f0");
  }

  function apply(theme) {
    if (theme) root.setAttribute("data-theme", theme);
    var active = currentTheme();
    paintChrome(active);
    if (!toggle) return;
    toggle.setAttribute("aria-pressed", active === "dark" ? "true" : "false");
    toggle.textContent = active === "dark" ? "Light mode" : "Dark mode";
  }

  apply(stored);

  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      apply(next);
      try {
        localStorage.setItem("theme", next);
      } catch (err) {
        /* Preference stays for this visit if storage is blocked. */
      }
    });
  }
})();

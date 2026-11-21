(function () {
  var root = document.documentElement;
  root.classList.add("js");
  var toggle = document.querySelector("[data-theme-toggle]");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

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
    var dark = theme === "dark";
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", dark ? "#070910" : "#eef3f8");
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

  var rotator = document.querySelector("[data-rotate]");
  var words = ["Python", "FastAPI", "PostgreSQL", "Odoo", "fintech"];
  if (rotator) {
    if (reduce) {
      rotator.textContent = words.join(" · ");
    } else {
      var index = 0;
      window.setInterval(function () {
        index = (index + 1) % words.length;
        rotator.textContent = words[index];
      }, 1800);
    }
  }

  var nodes = document.querySelectorAll("[data-reveal]");
  function show(node) { node.classList.add("is-in"); }
  if (reduce || !("IntersectionObserver" in window)) {
    nodes.forEach(show);
    return;
  }
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      show(entry.target);
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
  nodes.forEach(function (node) {
    var rect = node.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.92 && rect.bottom > 0) show(node);
    else observer.observe(node);
  });
  window.setTimeout(function () { nodes.forEach(show); }, 1600);
})();

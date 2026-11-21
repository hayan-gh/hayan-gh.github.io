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
    if (meta) meta.setAttribute("content", dark ? "#12110f" : "#f6f1e7");
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

  var links = Array.prototype.slice.call(document.querySelectorAll(".nav a"));
  var sections = links.map(function (link) {
    return { link: link, section: document.querySelector(link.getAttribute("href")) };
  }).filter(function (item) { return item.section; });

  function mark(id) {
    links.forEach(function (link) {
      if (link.getAttribute("href") === "#" + id) link.setAttribute("aria-current", "true");
      else link.removeAttribute("aria-current");
    });
  }

  if ("IntersectionObserver" in window && sections.length) {
    var visible = new Map();
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        visible.set(entry.target.id, entry.isIntersecting ? entry.intersectionRatio : 0);
      });
      var best = null;
      var bestRatio = 0;
      visible.forEach(function (ratio, id) {
        if (ratio > bestRatio) {
          best = id;
          bestRatio = ratio;
        }
      });
      if (best) mark(best);
    }, { rootMargin: "-20% 0px -55% 0px", threshold: [0, 0.15, 0.4] });
    sections.forEach(function (item) { spy.observe(item.section); });
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

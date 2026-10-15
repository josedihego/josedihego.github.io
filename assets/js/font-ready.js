// Runs right after the theme's main.min.js: hold the theme's jQuery init until the Inter web font
// has loaded, so the masthead menu is measured with the real font (max 1.5 s wait).
(function () {
  if (!window.jQuery || !document.fonts || !document.fonts.load) return;
  var released = false;
  function release() {
    if (!released) { released = true; jQuery.holdReady(false); }
  }
  jQuery.holdReady(true);
  document.fonts.load('400 1em Inter').then(release, release);
  setTimeout(release, 1500);
})();

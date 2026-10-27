// Copy button for BibTeX citation boxes and code blocks. Progressive
// enhancement: the button is rendered with `hidden` and only shown when this
// script runs, so pages without JavaScript simply show selectable text.
// `data-copy-name` on the button names what is copied (default: BibTeX).
(function () {
  "use strict";

  function selectText(el) {
    var range = document.createRange();
    range.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  }

  function legacyCopy(el) {
    selectText(el);
    try {
      return document.execCommand("copy");
    } catch (e) {
      return false;
    }
  }

  function announce(box, button, message, ok) {
    var status = box.querySelector(".citation__status");
    if (status) status.textContent = message;
    button.textContent = ok ? "Copied" : "Copy";
    window.clearTimeout(button._resetTimer);
    button._resetTimer = window.setTimeout(function () {
      button.textContent = "Copy";
      if (status) status.textContent = "";
    }, 4000);
  }

  document.querySelectorAll(".citation__copy").forEach(function (button) {
    var target = document.getElementById(button.getAttribute("data-copy-target"));
    var box = button.closest(".citation");
    if (!target || !box) return;
    var name = button.getAttribute("data-copy-name") || "BibTeX";
    button.hidden = false;

    button.addEventListener("click", function () {
      var text = target.textContent;
      var fail = function () {
        if (legacyCopy(target)) {
          announce(box, button, name + " copied to clipboard.", true);
        } else {
          selectText(target);
          target.focus();
          announce(box, button, "Copying is not available here. The text is selected: press Ctrl+C (or ⌘C) to copy it.", false);
        }
      };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(function () {
          announce(box, button, name + " copied to clipboard.", true);
        }, fail);
      } else {
        fail();
      }
    });
  });
})();

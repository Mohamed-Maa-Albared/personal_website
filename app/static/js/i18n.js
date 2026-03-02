/* ====================================================
   i18n — Route-based Language Switcher
   Neural aesthetic transition: synaptic scan sweep.
   Locale is rendered server-side (Flask) — JS only adds
   transition polish before navigating.
   ==================================================== */

(function () {
    'use strict';

    function sleep(ms) {
        return new Promise(function (resolve) { setTimeout(resolve, ms); });
    }

    /**
     * Fire the neuro-scan overlay animation, fade out main content,
     * then navigate to the target URL.
     *
     * Performance notes:
     *  - Overlay is CSS-animated (GPU-composited transform + opacity).
     *  - Total blocking time before navigation: ~280 ms — imperceptible.
     *  - No heavy JS running during the animation.
     */
    async function animateAndNavigate(url) {
        if (!url) return;

        var isRTL = document.documentElement.dir === 'rtl';

        // ── 1. Announce to screen readers ──────────────────────────
        var announcer = document.getElementById('lang-announcer');
        if (announcer) {
            announcer.textContent = url.indexOf('/ar/') !== -1
                ? 'جارٍ التبديل إلى العربية'
                : 'Switching to English';
        }

        // ── 2. Neuro scan overlay ───────────────────────────────────
        var overlay = document.getElementById('neuroScanOverlay');
        if (overlay) {
            // Mirror sweep direction on RTL pages for natural feel
            overlay.style.transform = isRTL ? 'translateX(110%) scaleX(-1)' : '';
            overlay.classList.add('active');
        }

        // ── 3. Fade main content ────────────────────────────────────
        var main = document.querySelector('main');
        if (main) {
            // Force reflow so CSS transition fires correctly
            main.style.transition = 'opacity .28s ease, transform .28s ease';
            main.getBoundingClientRect(); // eslint-disable-line no-unused-expressions
            main.classList.add('lang-switching');
        }

        // ── 4. Navigate after animation has mostly completed ───────
        await sleep(280);
        window.location.href = url;
    }

    function init() {
        var toggle = document.getElementById('langToggle');
        if (!toggle) return;

        toggle.addEventListener('click', function () {
            var targetUrl = toggle.dataset.switchUrl;
            animateAndNavigate(targetUrl);
        });
    }

    document.addEventListener('DOMContentLoaded', init);
}());

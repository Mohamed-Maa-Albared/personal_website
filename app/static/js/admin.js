/* ═══════ Admin Dashboard Tab Navigation ═══════ */
document.addEventListener('DOMContentLoaded', function () {
    var tabs = document.querySelectorAll('.admin-tab');
    var panels = document.querySelectorAll('.tab-panel');

    if (!tabs.length) return;

    tabs.forEach(function (tab) {
        tab.addEventListener('click', function () {
            var target = tab.getAttribute('data-tab');

            // Deactivate all tabs and panels
            tabs.forEach(function (t) { t.classList.remove('active'); });
            panels.forEach(function (p) { p.classList.remove('active'); });

            // Activate clicked tab and matching panel
            tab.classList.add('active');
            var panel = document.getElementById(target);
            if (panel) {
                panel.classList.add('active');
            }

            // Persist active tab in URL hash
            history.replaceState(null, '', '#' + target);
        });
    });

    // Restore from hash on load
    var hash = location.hash.replace('#', '');
    if (hash) {
        var t = document.querySelector('.admin-tab[data-tab="' + hash + '"]');
        if (t) t.click();
    }
});

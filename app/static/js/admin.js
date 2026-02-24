/* ═══════════════════════════════════════════════════════════════
 *  Admin Dashboard — UI Controller
 *  Handles: tabs, WYSIWYG editing, image upload, inline edits,
 *  delete confirmations, and Chart.js analytics.
 * ═══════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {

    /* ── 1. Tab Navigation ───────────────────────────────────── */
    var tabs = document.querySelectorAll('.admin-tab');
    var panels = document.querySelectorAll('.tab-panel');

    if (tabs.length) {
        tabs.forEach(function (tab) {
            tab.addEventListener('click', function () {
                var target = tab.getAttribute('data-tab');
                tabs.forEach(function (t) { t.classList.remove('active'); });
                panels.forEach(function (p) { p.classList.remove('active'); });
                tab.classList.add('active');
                var panel = document.getElementById(target);
                if (panel) panel.classList.add('active');
                history.replaceState(null, '', '#' + target);
            });
        });

        // Restore from URL hash
        var hash = location.hash.replace('#', '');
        if (hash) {
            var t = document.querySelector('.admin-tab[data-tab="' + hash + '"]');
            if (t) t.click();
        }
    }

    /* ── 2. WYSIWYG Editors ──────────────────────────────────── */
    initWysiwygEditors();

    /* ── 2b. Highlight List Editor ───────────────────────────── */
    initHighlightEditor();

    /* ── 3. Image Upload ─────────────────────────────────────── */
    initImageUpload();

    /* ── 4. Inline Edit Toggles (Impact / Skills / Languages) ─ */
    document.querySelectorAll('.inline-edit-toggle').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var formId = btn.getAttribute('data-form');
            var form = document.getElementById(formId);
            if (form) {
                var isVisible = form.style.display !== 'none';
                form.style.display = isVisible ? 'none' : 'block';
                btn.textContent = isVisible ? 'Edit' : 'Cancel';
            }
        });
    });

    /* ── 5. Delete Confirmations (replaces inline onsubmit) ─── */
    document.addEventListener('submit', function (e) {
        var form = e.target;
        if (form.tagName === 'FORM' && form.hasAttribute('data-confirm')) {
            if (!confirm(form.getAttribute('data-confirm'))) {
                e.preventDefault();
            }
        }
    });

    /* ── 6. Charts (Analytics) ───────────────────────────────── */
    initCharts();
});


/* ═══════════════════════════════════════════════════════════════
 *  WYSIWYG Rich-Text Editor
 *  Converts any <textarea data-wysiwyg> into a contentEditable
 *  div with a formatting toolbar.  Uses document.execCommand()
 *  which is still universally supported in modern browsers.
 * ═══════════════════════════════════════════════════════════════ */

function initWysiwygEditors() {
    var textareas = document.querySelectorAll('[data-wysiwyg]');
    if (!textareas.length) return;

    textareas.forEach(function (textarea) {
        // Check if there's already a toolbar immediately before the textarea
        var toolbar = null;
        var prevEl = textarea.previousElementSibling;
        if (prevEl && prevEl.classList && prevEl.classList.contains('editor-toolbar')) {
            toolbar = prevEl;
        }

        // Create toolbar if none exists
        var isMini = textarea.getAttribute('data-wysiwyg') === 'mini';
        if (!toolbar) {
            toolbar = buildToolbar(isMini);
            textarea.parentNode.insertBefore(toolbar, textarea);
        }

        // Create contentEditable div
        var editor = document.createElement('div');
        editor.className = 'wysiwyg-editor';
        editor.setAttribute('contenteditable', 'true');
        editor.innerHTML = textarea.value || '';

        // Sizing — match the intended textarea rows
        var rows = parseInt(textarea.getAttribute('rows')) || 6;
        editor.style.minHeight = (rows * 1.6) + 'em';

        // Hide textarea and insert the visual editor after it
        textarea.style.display = 'none';
        textarea.parentNode.insertBefore(editor, textarea.nextSibling);

        // ── Toolbar click handler ──
        toolbar.addEventListener('click', function (e) {
            var btn = e.target.closest('.toolbar-btn');
            if (!btn || btn.classList.contains('toolbar-toggle-html')) return;
            e.preventDefault();
            editor.focus();
            execToolbarCmd(btn.getAttribute('data-cmd'));
            // Sync after command
            textarea.value = editor.innerHTML;
        });

        // ── Sync on every input ──
        editor.addEventListener('input', function () {
            textarea.value = editor.innerHTML;
        });

        // ── Sync before form submit ──
        var form = textarea.closest('form');
        if (form && !form.hasAttribute('data-wysiwyg-bound')) {
            form.setAttribute('data-wysiwyg-bound', 'true');
            form.addEventListener('submit', function () {
                // Sync ALL editors within this form
                form.querySelectorAll('[data-wysiwyg]').forEach(function (ta) {
                    var ed = ta.nextElementSibling;
                    if (ed && ed.classList.contains('wysiwyg-editor')) {
                        ta.value = ed.innerHTML;
                    }
                    // Also sync from source view if it's active
                    var src = ta.parentNode.querySelector('.wysiwyg-source');
                    if (src && src.style.display !== 'none') {
                        ta.value = src.value;
                    }
                });
            });
        }

        // ── HTML / Visual toggle (non-mini editors only) ──
        if (!isMini) {
            // Add separator and toggle button to toolbar
            var sep = document.createElement('span');
            sep.className = 'toolbar-sep';
            toolbar.appendChild(sep);

            var toggleBtn = document.createElement('button');
            toggleBtn.type = 'button';
            toggleBtn.className = 'toolbar-btn toolbar-toggle-html';
            toggleBtn.innerHTML = '&lt;/&gt; HTML';
            toggleBtn.title = 'Toggle HTML Source';
            toolbar.appendChild(toggleBtn);

            // Create HTML source textarea
            var sourceView = document.createElement('textarea');
            sourceView.className = 'wysiwyg-source';
            sourceView.style.display = 'none';
            sourceView.rows = rows;
            sourceView.spellcheck = false;
            editor.parentNode.insertBefore(sourceView, editor.nextSibling);

            var isHtmlMode = false;

            toggleBtn.addEventListener('click', function (e) {
                e.preventDefault();
                isHtmlMode = !isHtmlMode;

                if (isHtmlMode) {
                    // Switch to HTML source mode
                    sourceView.value = editor.innerHTML;
                    editor.style.display = 'none';
                    sourceView.style.display = 'block';
                    toggleBtn.classList.add('active');
                    // Disable formatting buttons
                    toolbar.querySelectorAll('.toolbar-btn:not(.toolbar-toggle-html)').forEach(function (btn) {
                        btn.disabled = true;
                        btn.style.opacity = '0.3';
                        btn.style.pointerEvents = 'none';
                    });
                } else {
                    // Switch back to Visual mode
                    editor.innerHTML = sourceView.value;
                    textarea.value = sourceView.value;
                    sourceView.style.display = 'none';
                    editor.style.display = 'block';
                    toggleBtn.classList.remove('active');
                    // Re-enable formatting buttons
                    toolbar.querySelectorAll('.toolbar-btn:not(.toolbar-toggle-html)').forEach(function (btn) {
                        btn.disabled = false;
                        btn.style.opacity = '';
                        btn.style.pointerEvents = '';
                    });
                }
            });

            // Sync source view to textarea on input
            sourceView.addEventListener('input', function () {
                textarea.value = sourceView.value;
            });
        }
    });
}

/** Build a toolbar element.  @param {boolean} mini — smaller toolbar for config fields */
function buildToolbar(mini) {
    var bar = document.createElement('div');
    bar.className = 'editor-toolbar';

    if (mini) {
        bar.innerHTML =
            '<button type="button" class="toolbar-btn" data-cmd="bold" title="Bold"><strong>B</strong></button>' +
            '<button type="button" class="toolbar-btn" data-cmd="italic" title="Italic"><em>I</em></button>' +
            '<button type="button" class="toolbar-btn toolbar-btn-accent" data-cmd="accentColor" title="Accent Color"><span style="color:#00e5ff;font-weight:700">A</span></button>' +
            '<span class="toolbar-sep"></span>' +
            '<button type="button" class="toolbar-btn" data-cmd="link" title="Insert Link">&#128279;</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="removeFormat" title="Clear Formatting">&#10005;</button>';
    } else {
        bar.innerHTML =
            '<button type="button" class="toolbar-btn" data-cmd="bold" title="Bold"><strong>B</strong></button>' +
            '<button type="button" class="toolbar-btn" data-cmd="italic" title="Italic"><em>I</em></button>' +
            '<button type="button" class="toolbar-btn" data-cmd="h2" title="Heading 2">H2</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="h3" title="Heading 3">H3</button>' +
            '<span class="toolbar-sep"></span>' +
            '<button type="button" class="toolbar-btn" data-cmd="link" title="Insert Link">&#128279;</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="image" title="Insert Image">&#128247;</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="ul" title="Bulleted List">&#8226; List</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="ol" title="Numbered List">1. List</button>' +
            '<span class="toolbar-sep"></span>' +
            '<button type="button" class="toolbar-btn" data-cmd="blockquote" title="Blockquote">&#10077;</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="code" title="Code Block">&lt;/&gt;</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="hr" title="Horizontal Rule">&#8213;</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="p" title="Paragraph">&#182;</button>' +
            '<button type="button" class="toolbar-btn" data-cmd="removeFormat" title="Clear Formatting">&#10005;</button>';
    }
    return bar;
}

/** Execute a formatting command on the focused contentEditable region. */
function execToolbarCmd(cmd) {
    switch (cmd) {
        case 'bold':
            document.execCommand('bold', false);
            break;
        case 'italic':
            document.execCommand('italic', false);
            break;
        case 'h2':
            document.execCommand('formatBlock', false, '<h2>');
            break;
        case 'h3':
            document.execCommand('formatBlock', false, '<h3>');
            break;
        case 'link':
            var url = prompt('Enter URL:', 'https://');
            if (url) document.execCommand('createLink', false, url);
            break;
        case 'image':
            var imgUrl = prompt('Enter image URL:', 'https://');
            if (imgUrl) document.execCommand('insertImage', false, imgUrl);
            break;
        case 'ul':
            document.execCommand('insertUnorderedList', false);
            break;
        case 'ol':
            document.execCommand('insertOrderedList', false);
            break;
        case 'blockquote':
            document.execCommand('formatBlock', false, '<blockquote>');
            break;
        case 'code':
            document.execCommand('formatBlock', false, '<pre>');
            break;
        case 'hr':
            document.execCommand('insertHorizontalRule', false);
            break;
        case 'p':
            document.execCommand('formatBlock', false, '<p>');
            break;
        case 'accentColor':
            wrapSelectionWithAccent();
            break;
        case 'removeFormat':
            document.execCommand('removeFormat', false);
            // Also strip accent-hl spans
            var editor = document.querySelector('.wysiwyg-editor:focus');
            if (editor) {
                editor.querySelectorAll('.accent-hl').forEach(function (span) {
                    var parent = span.parentNode;
                    while (span.firstChild) parent.insertBefore(span.firstChild, span);
                    parent.removeChild(span);
                });
            }
            break;
    }
}

/**
 * Wrap the current selection in a <span class="accent-hl"> for accent-colored text.
 * If the selection is already inside an .accent-hl span, unwrap it (toggle).
 */
function wrapSelectionWithAccent() {
    var sel = window.getSelection();
    if (!sel.rangeCount || sel.isCollapsed) return;

    var range = sel.getRangeAt(0);

    // Check if already inside an accent-hl span — if so, unwrap
    var parent = range.commonAncestorContainer;
    if (parent.nodeType === 3) parent = parent.parentNode;
    var existing = parent.closest ? parent.closest('.accent-hl') : null;
    if (existing) {
        var p = existing.parentNode;
        while (existing.firstChild) p.insertBefore(existing.firstChild, existing);
        p.removeChild(existing);
        return;
    }

    var span = document.createElement('span');
    span.className = 'accent-hl';
    try {
        range.surroundContents(span);
    } catch (e) {
        // If range crosses element boundaries, extract and wrap
        var frag = range.extractContents();
        span.appendChild(frag);
        range.insertNode(span);
    }
    sel.removeAllRanges();
    var newRange = document.createRange();
    newRange.selectNodeContents(span);
    sel.addRange(newRange);
}


/* ═══════════════════════════════════════════════════════════════
 *  Image Upload (Blog Cover Image)
 * ═══════════════════════════════════════════════════════════════ */

function initImageUpload() {
    var uploadBtn = document.getElementById('uploadBtn');
    var uploadInput = document.getElementById('imageUpload');
    var coverInput = document.getElementById('cover_image');
    var statusEl = document.getElementById('uploadStatus');

    // Trigger file picker from button (no inline onclick needed)
    if (uploadBtn && uploadInput) {
        uploadBtn.addEventListener('click', function () {
            uploadInput.click();
        });
    }

    // Handle file selection → upload
    if (uploadInput && coverInput) {
        uploadInput.addEventListener('change', function () {
            var file = this.files[0];
            if (!file) return;

            if (file.size > 5 * 1024 * 1024) {
                statusEl.textContent = 'File too large (max 5 MB)';
                statusEl.style.color = '#ff5050';
                return;
            }

            statusEl.textContent = 'Uploading\u2026';
            statusEl.style.color = '#00e5ff';

            var formData = new FormData();
            formData.append('image', file);

            var csrfMeta = document.querySelector('input[name="csrf_token"]');
            var headers = {};
            if (csrfMeta) headers['X-CSRFToken'] = csrfMeta.value;

            fetch('/admin/upload-image', {
                method: 'POST',
                body: formData,
                headers: headers
            })
                .then(function (r) { return r.json(); })
                .then(function (data) {
                    if (data.success) {
                        coverInput.value = data.url;
                        statusEl.textContent = 'Uploaded! URL set.';
                        statusEl.style.color = '#34d399';
                    } else {
                        statusEl.textContent = data.message || 'Upload failed.';
                        statusEl.style.color = '#ff5050';
                    }
                })
                .catch(function () {
                    statusEl.textContent = 'Upload failed.';
                    statusEl.style.color = '#ff5050';
                });
        });
    }
}


/* ═══════════════════════════════════════════════════════════════
 *  Chart.js Analytics Init
 * ═══════════════════════════════════════════════════════════════ */

function initCharts() {
    // Daily visits chart
    var dailyCanvas = document.getElementById('dailyVisitsChart');
    if (!dailyCanvas || typeof Chart === 'undefined') return;

    var ctx = dailyCanvas.getContext('2d');
    var labels = JSON.parse(dailyCanvas.getAttribute('data-labels') || '[]');
    var counts = JSON.parse(dailyCanvas.getAttribute('data-counts') || '[]');

    var shortLabels = labels.map(function (l) {
        var parts = l.split('-');
        return parts[2] + '/' + parts[1];
    });

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: shortLabels,
            datasets: [{
                label: 'Page Views',
                data: counts,
                borderColor: '#7c5cfc',
                backgroundColor: 'rgba(124, 92, 252, 0.1)',
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#7c5cfc',
                pointBorderColor: '#7c5cfc',
                pointRadius: 2,
                pointHoverRadius: 5,
                borderWidth: 2,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: '#12161f',
                    titleColor: '#e8e6f0',
                    bodyColor: '#e8e6f0',
                    borderColor: 'rgba(124, 92, 252, 0.2)',
                    borderWidth: 1,
                    cornerRadius: 8,
                    padding: 10,
                }
            },
            scales: {
                x: {
                    ticks: { color: '#8b8a97', font: { size: 10 }, maxTicksLimit: 10 },
                    grid: { color: 'rgba(255,255,255,0.04)' }
                },
                y: {
                    beginAtZero: true,
                    ticks: { color: '#8b8a97', font: { size: 10 }, precision: 0 },
                    grid: { color: 'rgba(255,255,255,0.04)' }
                }
            }
        }
    });

    // Browser chart
    var browserCanvas = document.getElementById('browserChart');
    if (browserCanvas) {
        var bLabels = JSON.parse(browserCanvas.getAttribute('data-labels') || '[]');
        var bCounts = JSON.parse(browserCanvas.getAttribute('data-counts') || '[]');
        var browserColors = ['#7c5cfc', '#00e5ff', '#34d399', '#fbbf24', '#ff5050', '#a78bfa'];

        new Chart(browserCanvas.getContext('2d'), {
            type: 'doughnut',
            data: {
                labels: bLabels,
                datasets: [{
                    data: bCounts,
                    backgroundColor: browserColors.slice(0, bLabels.length),
                    borderColor: '#12161f',
                    borderWidth: 2,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '65%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color: '#8b8a97', font: { size: 11 }, padding: 12, boxWidth: 12 }
                    }
                }
            }
        });
    }

    // Device chart
    var deviceCanvas = document.getElementById('deviceChart');
    if (deviceCanvas) {
        var dLabels = JSON.parse(deviceCanvas.getAttribute('data-labels') || '[]');
        var dCounts = JSON.parse(deviceCanvas.getAttribute('data-counts') || '[]');

        new Chart(deviceCanvas.getContext('2d'), {
            type: 'doughnut',
            data: {
                labels: dLabels,
                datasets: [{
                    data: dCounts,
                    backgroundColor: ['#7c5cfc', '#00e5ff', '#34d399'],
                    borderColor: '#12161f',
                    borderWidth: 2,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '65%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color: '#8b8a97', font: { size: 11 }, padding: 12, boxWidth: 12 }
                    }
                }
            }
        });
    }
}


/* ── Highlight List Editor ────────────────────────────────────── */
function initHighlightEditor() {
    var list = document.getElementById('highlightListEditor');
    var addBtn = document.getElementById('addHighlightBtn');
    var hidden = document.getElementById('highlights');
    if (!list || !addBtn || !hidden) return;

    /** Collect all highlight editors' HTML into the hidden textarea (one per line). */
    function syncHidden() {
        var items = list.querySelectorAll('.hl-item');
        var lines = [];
        items.forEach(function (item) {
            var ta = item.querySelector('.hl-source');
            // The WYSIWYG init may have replaced the textarea — sync from editor first
            var ed = ta.nextElementSibling;
            if (ed && ed.classList.contains('wysiwyg-editor')) {
                ta.value = ed.innerHTML;
            }
            var src = item.querySelector('.wysiwyg-source');
            if (src && src.style.display !== 'none') {
                ta.value = src.value;
            }
            var val = ta.value.trim();
            if (val) lines.push(val);
        });
        hidden.value = lines.join('\n');
    }

    /** Wire a remove button. */
    function wireRemoveBtn(btn) {
        btn.addEventListener('click', function () {
            var item = btn.closest('.hl-item');
            item.style.opacity = '0';
            item.style.transform = 'scale(.95)';
            setTimeout(function () { item.remove(); syncHidden(); }, 150);
        });
    }

    /** Create a new highlight item with a WYSIWYG mini editor. */
    function addItem(initialHtml) {
        var item = document.createElement('div');
        item.className = 'hl-item';

        var ta = document.createElement('textarea');
        ta.className = 'hl-source';
        ta.setAttribute('data-wysiwyg', 'mini');
        ta.rows = 2;
        ta.value = initialHtml || '';

        var removeBtn = document.createElement('button');
        removeBtn.type = 'button';
        removeBtn.className = 'hl-remove';
        removeBtn.title = 'Remove this highlight';
        removeBtn.innerHTML = '&times;';

        item.appendChild(ta);
        item.appendChild(removeBtn);
        list.appendChild(item);

        wireRemoveBtn(removeBtn);

        // Initialize the WYSIWYG editor on this new textarea
        initSingleWysiwyg(ta);

        // Focus the new editor
        var ed = ta.nextElementSibling;
        if (ed && ed.classList.contains('wysiwyg-editor')) {
            ed.focus();
        }
    }

    // Wire existing remove buttons
    list.querySelectorAll('.hl-remove').forEach(wireRemoveBtn);

    // Add button
    addBtn.addEventListener('click', function () {
        addItem('');
    });

    // Sync on form submit
    var form = hidden.closest('form');
    if (form) {
        form.addEventListener('submit', function () {
            syncHidden();
        });
    }
}

/**
 * Initialize a single WYSIWYG mini editor on a textarea element.
 * Reuses the existing buildToolbar / execToolbarCmd infrastructure.
 */
function initSingleWysiwyg(textarea) {
    var toolbar = buildToolbar(true); // mini toolbar
    textarea.parentNode.insertBefore(toolbar, textarea);

    var editor = document.createElement('div');
    editor.className = 'wysiwyg-editor';
    editor.setAttribute('contenteditable', 'true');
    editor.innerHTML = textarea.value || '';

    var rows = parseInt(textarea.getAttribute('rows')) || 2;
    editor.style.minHeight = (rows * 1.6) + 'em';

    textarea.style.display = 'none';
    textarea.parentNode.insertBefore(editor, textarea.nextSibling);

    toolbar.addEventListener('click', function (e) {
        var btn = e.target.closest('.toolbar-btn');
        if (!btn) return;
        e.preventDefault();
        editor.focus();
        execToolbarCmd(btn.getAttribute('data-cmd'));
        textarea.value = editor.innerHTML;
    });

    editor.addEventListener('input', function () {
        textarea.value = editor.innerHTML;
    });
}

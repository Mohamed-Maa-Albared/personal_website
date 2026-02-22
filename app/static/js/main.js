/* ====================================================
   Mohamed Maa Albared — Neural Personal Website
   Main JavaScript — Canvas + Animations + Interactions
   ==================================================== */

(function () {
    'use strict';

    // ─── LOADER ───────────────────────────────────
    window.addEventListener('load', () => {
        setTimeout(() => {
            document.getElementById('loader')?.classList.add('hidden');
        }, 800);
    });

    // ─── NEURAL CANVAS ────────────────────────────
    const canvas = document.getElementById('neuralCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let w, h, nodes = [], mouse = { x: -999, y: -999 };
        const NODE_COUNT = 80;
        const CONNECT_DIST = 160;

        function resize() {
            w = canvas.width = canvas.offsetWidth;
            h = canvas.height = canvas.offsetHeight;
        }

        function createNodes() {
            nodes = [];
            for (let i = 0; i < NODE_COUNT; i++) {
                nodes.push({
                    x: Math.random() * w,
                    y: Math.random() * h,
                    vx: (Math.random() - 0.5) * 0.4,
                    vy: (Math.random() - 0.5) * 0.4,
                    r: Math.random() * 2 + 1,
                    pulse: Math.random() * Math.PI * 2
                });
            }
        }

        function draw() {
            ctx.clearRect(0, 0, w, h);

            // Draw connections
            for (let i = 0; i < nodes.length; i++) {
                for (let j = i + 1; j < nodes.length; j++) {
                    const dx = nodes[i].x - nodes[j].x;
                    const dy = nodes[i].y - nodes[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < CONNECT_DIST) {
                        const alpha = (1 - dist / CONNECT_DIST) * 0.15;
                        ctx.strokeStyle = `rgba(124, 92, 252, ${alpha})`;
                        ctx.lineWidth = 0.5;
                        ctx.beginPath();
                        ctx.moveTo(nodes[i].x, nodes[i].y);
                        ctx.lineTo(nodes[j].x, nodes[j].y);
                        ctx.stroke();
                    }
                }

                // Mouse connection
                const mdx = nodes[i].x - mouse.x;
                const mdy = nodes[i].y - mouse.y;
                const mdist = Math.sqrt(mdx * mdx + mdy * mdy);
                if (mdist < 200) {
                    const alpha = (1 - mdist / 200) * 0.3;
                    ctx.strokeStyle = `rgba(0, 229, 255, ${alpha})`;
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(nodes[i].x, nodes[i].y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.stroke();
                }
            }

            // Draw & update nodes
            const time = Date.now() * 0.002;
            for (const n of nodes) {
                n.x += n.vx;
                n.y += n.vy;
                if (n.x < 0 || n.x > w) n.vx *= -1;
                if (n.y < 0 || n.y > h) n.vy *= -1;

                const pulseScale = 1 + Math.sin(time + n.pulse) * 0.3;
                const r = n.r * pulseScale;

                // Glow
                const grad = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, r * 4);
                grad.addColorStop(0, 'rgba(124, 92, 252, 0.3)');
                grad.addColorStop(1, 'rgba(124, 92, 252, 0)');
                ctx.fillStyle = grad;
                ctx.beginPath();
                ctx.arc(n.x, n.y, r * 4, 0, Math.PI * 2);
                ctx.fill();

                // Node
                ctx.fillStyle = 'rgba(124, 92, 252, 0.8)';
                ctx.beginPath();
                ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
                ctx.fill();
            }

            requestAnimationFrame(draw);
        }

        resize();
        createNodes();
        draw();
        window.addEventListener('resize', () => { resize(); createNodes(); });
        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
        });
        canvas.addEventListener('mouseleave', () => { mouse.x = -999; mouse.y = -999; });
    }

    // ─── CUSTOM CURSOR ────────────────────────────
    const dot = document.querySelector('.cursor-dot');
    const ring = document.querySelector('.cursor-ring');

    if (dot && ring && window.innerWidth > 768) {
        let mx = 0, my = 0, rx = 0, ry = 0;

        document.addEventListener('mousemove', (e) => {
            mx = e.clientX; my = e.clientY;
            dot.style.left = mx - 3 + 'px';
            dot.style.top = my - 3 + 'px';
        });

        function animateCursor() {
            rx += (mx - rx) * 0.15;
            ry += (my - ry) * 0.15;
            ring.style.left = rx + 'px';
            ring.style.top = ry + 'px';
            requestAnimationFrame(animateCursor);
        }
        animateCursor();

        // Hover effect on interactive elements
        document.querySelectorAll('a, button, .project-card, .filter-btn').forEach(el => {
            el.addEventListener('mouseenter', () => ring.classList.add('hover'));
            el.addEventListener('mouseleave', () => ring.classList.remove('hover'));
        });
    }

    // ─── NAVBAR SCROLL ────────────────────────────
    const navbar = document.getElementById('navbar');
    if (navbar) {
        let lastScroll = 0;
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            navbar.classList.toggle('scrolled', scrollY > 50);
            lastScroll = scrollY;
        });
    }

    // ─── MOBILE NAV ───────────────────────────────
    const mobileToggle = document.getElementById('mobileToggle');
    const navLinks = document.getElementById('navLinks');
    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            navLinks.classList.toggle('open');
        });
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileToggle.classList.remove('active');
                navLinks.classList.remove('open');
            });
        });
    }

    // ─── SCROLL REVEAL ────────────────────────────
    const revealElements = document.querySelectorAll('.reveal-up');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    revealElements.forEach(el => revealObserver.observe(el));

    // ─── COUNTER ANIMATION ────────────────────────
    const counters = document.querySelectorAll('[data-count]');
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.dataset.count, 10);
                const duration = 2000;
                const start = performance.now();

                function update(now) {
                    const elapsed = now - start;
                    const progress = Math.min(elapsed / duration, 1);
                    // Ease out cubic
                    const eased = 1 - Math.pow(1 - progress, 3);
                    el.textContent = Math.round(target * eased);
                    if (progress < 1) requestAnimationFrame(update);
                }
                requestAnimationFrame(update);
                counterObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(el => counterObserver.observe(el));

    // ─── PROJECT FILTERS ──────────────────────────
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card[data-category]');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;
            projectCards.forEach(card => {
                if (filter === 'all' || card.dataset.category.includes(filter)) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });

    // ─── CONTACT FORM ─────────────────────────────
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const btnText = contactForm.querySelector('.btn-text');
            const btnLoading = contactForm.querySelector('.btn-loading');
            const messageDiv = document.getElementById('formMessage');
            const submitBtn = contactForm.querySelector('.submit-btn');

            // Get data
            const data = {
                name: contactForm.querySelector('#name').value.trim(),
                email: contactForm.querySelector('#email').value.trim(),
                subject: contactForm.querySelector('#subject').value.trim(),
                message: contactForm.querySelector('#message').value.trim(),
                website: contactForm.querySelector('[name="website"]')?.value || ''
            };

            // Client-side validation
            if (!data.name || !data.email || !data.subject || !data.message) {
                showMessage(messageDiv, 'Please fill in all fields.', 'error');
                return;
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(data.email)) {
                showMessage(messageDiv, 'Please enter a valid email address.', 'error');
                return;
            }

            if (data.message.length < 10) {
                showMessage(messageDiv, 'Message is too short (min 10 characters).', 'error');
                return;
            }

            // Show loading
            submitBtn.disabled = true;
            if (btnText) btnText.style.display = 'none';
            if (btnLoading) btnLoading.style.display = 'inline';

            try {
                const response = await fetch('/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                showMessage(messageDiv, result.message, result.success ? 'success' : 'error');

                if (result.success) {
                    contactForm.reset();
                }
            } catch (err) {
                showMessage(messageDiv, 'Network error. Please try again.', 'error');
            } finally {
                submitBtn.disabled = false;
                if (btnText) btnText.style.display = 'inline';
                if (btnLoading) btnLoading.style.display = 'none';
            }
        });
    }

    function showMessage(el, text, type) {
        el.textContent = text;
        el.className = 'form-message ' + type;
        setTimeout(() => {
            el.className = 'form-message';
        }, 6000);
    }

    // ─── SMOOTH SCROLL ────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                const offset = 80;
                const top = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });

})();

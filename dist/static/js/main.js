/**
 * 江汉大学 · AI+冲击动力学 课题组 - Main JavaScript
 * Interactive features: scroll animations, mobile menu, counter animations, particles
 */

(function() {
    'use strict';

    // ─── DOM Elements ───
    const navbar = document.getElementById('navbar');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navLinks = document.getElementById('navLinks');
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    const heroParticles = document.getElementById('heroParticles');

    // ─── Mobile Menu Toggle ───
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', function() {
            this.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // Close menu on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuBtn.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });

        // Close menu on outside click
        document.addEventListener('click', function(e) {
            if (!navLinks.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                mobileMenuBtn.classList.remove('active');
                navLinks.classList.remove('active');
            }
        });
    }

    // ─── Navbar Scroll Effect ───
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // ─── Scroll to Top Button ───
    if (scrollTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });

        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ─── Counter Animation ───
    function animateCounters() {
        const counters = document.querySelectorAll('.stat-number[data-target]');
        counters.forEach(counter => {
            const target = parseInt(counter.getAttribute('data-target'));
            const duration = 2000;
            const startTime = performance.now();
            const startValue = 0;

            function update(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                // Ease-out cubic
                const easeProgress = 1 - Math.pow(1 - progress, 3);
                const currentValue = Math.round(startValue + (target - startValue) * easeProgress);

                counter.textContent = currentValue.toLocaleString();

                if (progress < 1) {
                    requestAnimationFrame(update);
                }
            }

            requestAnimationFrame(update);
        });
    }

    // ─── Scroll Reveal Animation ───
    function handleScrollReveal() {
        const reveals = document.querySelectorAll('.reveal');
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        reveals.forEach(el => {
            const revealTop = el.getBoundingClientRect().top;
            if (revealTop < windowHeight - revealPoint) {
                el.classList.add('visible');
            }
        });
    }

    // Add reveal class to elements
    function addRevealClasses() {
        document.querySelectorAll(
            '.direction-card, .member-card, .news-item, .course-card, ' +
            '.direction-detail, .philosophy-item, .pub-item, .path-card, ' +
            '.resource-card, .tip-item, .profile-section, .pipeline-item'
        ).forEach(el => {
            if (!el.classList.contains('reveal')) {
                el.classList.add('reveal');
            }
        });
    }

    window.addEventListener('scroll', handleScrollReveal);

    // ─── Hero Particles ───
    function createParticles() {
        if (!heroParticles) return;

        const colors = ['#ff6b35', '#4a90d9', '#2ecc71', '#9b59b6', '#f7c948', '#1abc9c'];
        const particleCount = 30;

        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');

            const size = Math.random() * 4 + 2;
            const color = colors[Math.floor(Math.random() * colors.length)];

            particle.style.cssText = `
                left: ${Math.random() * 100}%;
                width: ${size}px;
                height: ${size}px;
                background: ${color};
                animation-duration: ${Math.random() * 15 + 10}s;
                animation-delay: ${Math.random() * 5}s;
            `;

            heroParticles.appendChild(particle);
        }
    }

    // ─── Smooth Scroll for Anchor Links ───
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                const offset = navbar ? navbar.offsetHeight + 24 : 80;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top: targetPosition, behavior: 'smooth' });
            }
        });
    });

    // ─── Parallax Effect for Hero ───
    function parallaxHero() {
        const hero = document.querySelector('.hero');
        if (!hero) return;

        const scrolled = window.pageYOffset;
        const heroBg = hero.querySelector('.hero-bg');
        if (heroBg) {
            heroBg.style.transform = `translateY(${scrolled * 0.4}px)`;
        }
    }

    // ─── Active Nav Link on Scroll ───
    function updateActiveNavLink() {
        const sections = document.querySelectorAll('section[id], .page-hero');
        const navItems = document.querySelectorAll('.nav-link');
        const scrollPos = window.scrollY + 100;

        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;

            if (scrollPos >= top && scrollPos < top + height) {
                // Not implemented for all pages, mainly for in-page
            }
        });
    }

    // ─── Keyboard Navigation ───
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && navLinks && navLinks.classList.contains('active')) {
            mobileMenuBtn.classList.remove('active');
            navLinks.classList.remove('active');
        }
    });

    // ─── Initialize ───
    function init() {
        createParticles();
        addRevealClasses();
        handleScrollReveal();

        // Observe hero stats for counter animation
        const statsSection = document.querySelector('.hero-stats');
        if (statsSection) {
            const observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        animateCounters();
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.5 });

            observer.observe(statsSection);
        }

        // Global scroll listener
        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    handleScrollReveal();
                    parallaxHero();
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        // Initial reveal check
        setTimeout(handleScrollReveal, 100);
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();

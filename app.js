document.addEventListener('DOMContentLoaded', () => {

    /* ─── Scroll Reveal (IntersectionObserver) ─── */
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1, rootMargin: '0px 0px -30px 0px' }
    );

    document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

    /* ─── Parallax hero background on scroll ─── */
    const heroBg = document.querySelector('.hero-bg img');
    if (heroBg && !('ontouchstart' in window)) {
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            if (scrolled < window.innerHeight) {
                heroBg.style.transform = `translateY(${scrolled * 0.25}px) scale(1.05)`;
            }
        }, { passive: true });
    }

    /* ─── Smooth scroll for anchor links ─── */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    /* ─── Counter animation for trust bar ─── */
    const trustNums = document.querySelectorAll('.trust-num');
    const trustObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    trustObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.5 }
    );
    trustNums.forEach(el => trustObserver.observe(el));

    function animateCounter(el) {
        const text = el.textContent.trim();
        // Check if it contains a number
        const match = text.match(/^(\d+)(\+?)$/);
        if (!match) return; // Skip non-numeric like "VIP", "24/7"
        
        const target = parseInt(match[1]);
        const suffix = match[2] || '';
        const duration = 1500;
        const start = performance.now();
        
        el.textContent = '0' + suffix;
        
        function update(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);
            // Ease out cubic
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.round(target * eased);
            el.textContent = current + suffix;
            
            if (progress < 1) {
                requestAnimationFrame(update);
            }
        }
        requestAnimationFrame(update);
    }
});

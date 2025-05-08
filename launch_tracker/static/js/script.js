document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.launch-card');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // animate only once
            }
        });
    }, {
        threshold: 0.1
    });

    cards.forEach(card => {
        observer.observe(card);
    });
});


const scrollBtn = document.getElementById('scrollToTop');

if (scrollBtn) {
    window.addEventListener('scroll', () => {
        scrollBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
    });

    scrollBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
} else {
    console.log('Element #scrollToTop not found.');
}

document.addEventListener('DOMContentLoaded', () => {
    // Starfield
    const canvas = document.getElementById('starfield');
    const ctx = canvas.getContext('2d');
    let stars = [];

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    function createStars(count) {
        stars = [];
        for (let i = 0; i < count; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                radius: Math.random() * 1.2,
                speed: Math.random() * 0.5 + 0.2
            });
        }
    }

    function drawStars() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'white';
        for (let star of stars) {
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.radius, 0, 2 * Math.PI);
            ctx.fill();
        }
    }

    function updateStars() {
        for (let star of stars) {
            star.y += star.speed;
            if (star.y > canvas.height) {
                star.y = 0;
                star.x = Math.random() * canvas.width;
            }
        }
    }

    function animate() {
        drawStars();
        updateStars();
        requestAnimationFrame(animate);
    }

    createStars(250);
    animate();
});


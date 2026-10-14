// 3D arka plan laptop açılma animasyonu
const laptopLid = document.querySelector('.laptop-lid');
const laptop3d = document.querySelector('.laptop-3d');

window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight - windowHeight;
    
    // Sayfa kaydırıldıkça laptop kapağı açılır
    // Başlangıçta -90deg (kapalı), scroll ile 0deg (açık) olur
    if (scrollY <= documentHeight) {
        const progress = Math.min(scrollY / (windowHeight * 0.8), 1);
        const rotation = -90 + (progress * 90);
        laptopLid.style.transform = `rotateX(${rotation}deg)`;
    }
});

// Mouse parallax efekti
document.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX / window.innerWidth - 0.5;
    const mouseY = e.clientY / window.innerHeight - 0.5;
    
    if (laptop3d) {
        const rotateX = mouseY * 10;
        const rotateY = mouseX * 10;
        laptop3d.style.transform = `translateY(${Math.sin(Date.now() / 1000) * 10}px) rotateX(${5 + rotateX}deg) rotateY(${-5 + rotateY}deg)`;
    }
    
    // Hero bölümü parallax
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.style.transform = `translate(${mouseX * 20}px, ${mouseY * 20}px)`;
    }
});

// Scroll animasyonları için Intersection Observer
const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Hakkımda bölümünü izle
const aboutCard = document.querySelector('.about-card');
if (aboutCard) {
    observer.observe(aboutCard);
}

// İletişim başlığını izle
const contactHeading = document.querySelector('.contact-section h3');
if (contactHeading) {
    observer.observe(contactHeading);
}

// İletişim linklerini izle
const contactLinks = document.querySelectorAll('.contact-link');
contactLinks.forEach(link => {
    observer.observe(link);
});

// Blog kartları için scroll animasyonu
const postCards = document.querySelectorAll('.post-card');
postCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
    
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.2 });
    
    cardObserver.observe(card);
});

// Smooth scroll için navigation linkleri
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Back to Top Button
const backToTopButton = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTopButton.classList.add('visible');
    } else {
        backToTopButton.classList.remove('visible');
    }
});

backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

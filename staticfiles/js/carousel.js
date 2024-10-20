// JavaScript para controlar el carrusel
const carousel = document.querySelector('.carousel');
const prevBtn = document.querySelector('.carousel-control.prev');
const nextBtn = document.querySelector('.carousel-control.next');
const dots = document.querySelectorAll('.dot');

let scrollAmount = 0;
const cardWidth = document.querySelector('.service-card').offsetWidth + 20; // Ancho de la tarjeta + margen
const cardsPerView = Math.floor(document.querySelector('.carousel-container').offsetWidth / cardWidth); 

nextBtn.addEventListener('click', () => {
    const containerWidth = document.querySelector('.carousel-container').offsetWidth;
    const maxScroll = carousel.scrollWidth - containerWidth;

    // Mover varias tarjetas a la vez
    scrollAmount += cardWidth * cardsPerView;

    // Limitar para no sobrepasar el máximo
    if (scrollAmount > maxScroll) {
        scrollAmount = maxScroll;
    }

    carousel.style.transform = `translateX(-${scrollAmount}px)`;
    updateIndicators();
});

prevBtn.addEventListener('click', () => {
    scrollAmount -= cardWidth * cardsPerView;

    // Limitar para no retroceder más allá del principio
    if (scrollAmount < 0) {
        scrollAmount = 0;
    }

    carousel.style.transform = `translateX(-${scrollAmount}px)`;
    updateIndicators();
});

// Función para actualizar los indicadores
function updateIndicators() {
    dots.forEach((dot, index) => {
        dot.classList.remove('active');
        const isActive = scrollAmount / cardWidth >= index && scrollAmount / cardWidth < index + cardsPerView;
        if (isActive) dot.classList.add('active');
    });
}

// Event listener para hacer clic en los puntos (indicadores)
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        scrollAmount = index * cardWidth;
        carousel.style.transform = `translateX(-${scrollAmount}px)`;
        updateIndicators();
    });
});

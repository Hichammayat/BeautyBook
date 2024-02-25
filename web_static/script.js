let currentIndex = 0;
function moveCarousel(direction) {
    const carousel = document.querySelector('.carousel');
    const totalItems = document.querySelectorAll('.carousel figure').length;
    currentIndex += direction;
    if (currentIndex >= totalItems) {
        currentIndex = 0;
    } else if (currentIndex < 0) {
        currentIndex = totalItems - 1;
    }
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}
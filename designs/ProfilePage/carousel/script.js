// script.js
const track = document.querySelector('.carousel-track');
const leftButton = document.querySelector('.carousel-button.left');
const rightButton = document.querySelector('.carousel-button.right');

// Current index of the first visible item
let index = 0;

// Total number of items
const totalItems = document.querySelectorAll('.carousel-item').length;

// Number of items visible at once
const visibleItems = 4;

function updateCarousel() {
    const offset = -(index * 100) / visibleItems;
    track.style.transform = `translateX(${offset}%)`;
}

leftButton.addEventListener('click', () => {
    index = (index - 1 + totalItems) % totalItems;
    updateCarousel();
});

rightButton.addEventListener('click', () => {
    index = (index + 2) % totalItems;
    updateCarousel();
});

// Initialize the carousel
updateCarousel();

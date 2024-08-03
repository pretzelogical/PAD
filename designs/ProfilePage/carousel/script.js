// script.js
const track = document.querySelector('.carousel-track');
const leftButton = document.querySelector('.carousel-button.left');
const rightButton = document.querySelector('.carousel-button.right');

// Current index of the first visible item
let index = 0;

// Total number of items
const totalItems = document.querySelectorAll('.carousel-item').length;

// Number of items visible at once
const visibleItems = 10;

function updateCarousel() {
    const offset = -(index * 150) / visibleItems;
    track.style.transform = `translateX(${offset}%)`;
}

leftButton.addEventListener('click', () => {
    index = (index - 1 + totalItems) % totalItems;
    updateCarousel();
});

rightButton.addEventListener('click', () => {
    index = (index + 1) % totalItems;
    updateCarousel();
});

// Initialize the carousel
updateCarousel();

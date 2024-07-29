document.addEventListener("DOMContentLoaded", function() {
    const readMoreLink = document.querySelector('.read-more');
    const textFull = document.querySelector('.text-full');

    readMoreLink.addEventListener('click', function(event) {
        event.preventDefault();
        textFull.style.display = 'inline';
        readMoreLink.style.display = 'none';
    });
});

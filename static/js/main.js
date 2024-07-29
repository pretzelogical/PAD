document.addEventListener('DOMContentLoaded', function() {
    // Function to add event listeners after content is loaded
    function addEventListeners() {
        document.querySelectorAll('.open-modal').forEach(button => {
            button.addEventListener('click', function () {
                var modal = document.getElementById('modal');
                modal.classList.remove('hidden');
            });
        });

        var closeModalButton = document.getElementById('close-modal');
        if (closeModalButton) {
            closeModalButton.addEventListener('click', function () {
                var modal = document.getElementById('modal');
                modal.classList.add('hidden');
            });
        }

        // Dropdown menu toggle
        document.getElementById('dropdown-btn').addEventListener('click', function () {
            var dropdownMenu = document.getElementById('dropdown-menu');
            dropdownMenu.classList.toggle('hidden');
        });

        // Mobile menu toggle
        document.getElementById('menu-btn').addEventListener('click', function () {
            var menu = document.getElementById('menu');
            menu.classList.toggle('hidden');
        });
    }

    // Add event listeners on load
    addEventListeners();
});

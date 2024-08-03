document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggleButton");
    const details = document.querySelector(".profile-card .details");

    toggleButton.addEventListener("click", function() {
        if (details.classList.contains("hidden")) {
            details.classList.remove("hidden");
            toggleButton.textContent = "▲";
            toggleButton.classList.add("collapsed");
        } else {
            details.classList.add("hidden");
            toggleButton.textContent = "▼";
            toggleButton.classList.remove("collapsed");
        }
    });
});

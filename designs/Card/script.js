document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggleButton");
    const details = document.querySelector(".profile-card .details");

    toggleButton.addEventListener("click", function() {
        if (details.style.display === "none" || details.style.display === "") {
            details.style.display = "block";
            toggleButton.textContent = "▲";
            toggleButton.classList.add("collapsed");
        } else {
            details.style.display = "none";
            toggleButton.textContent = "▼";
            toggleButton.classList.remove("collapsed");
        }
    });
});

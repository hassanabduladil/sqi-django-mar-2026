// Wait for the page to fully load
document.addEventListener("DOMContentLoaded", function() {

    const announcementBar = document.getElementById("announcement-bar");
    const closeBtn = document.getElementById("close-btn");

    // Slide down the announcement bar
    if (announcementBar) {
        // start hidden
        announcementBar.style.display = "block";
        announcementBar.style.top = "-100px"; // start above view
        announcementBar.style.transition = "top 0.5s ease";

        // trigger slide down
        setTimeout(() => {
            announcementBar.style.top = "0";
        }, 100); // slight delay for smooth effect
    }

    // Close button functionality
    if (closeBtn) {
        closeBtn.addEventListener("click", function() {
            // Slide up and hide
            announcementBar.style.top = "-100px";
            setTimeout(() => {
                announcementBar.style.display = "none";
            }, 500); // wait for animation to finish
        });
    }

});
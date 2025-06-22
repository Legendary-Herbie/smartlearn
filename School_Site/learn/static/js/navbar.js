// Responsive navbar and dropdown logic

document.addEventListener('DOMContentLoaded', function() {
    const burger = document.querySelector('.navbar-burger');
    const navMenu = document.querySelector('.navbar-menu');
    if (burger && navMenu) {
        burger.addEventListener('click', function() {
            navMenu.classList.toggle('is-active');
            burger.classList.toggle('is-active');
        });
    }

    // Dropdown logic
    document.querySelectorAll('.has-dropdown').forEach(function(drop) {
        drop.addEventListener('mouseenter', function() {
            this.classList.add('is-open');
        });
        drop.addEventListener('mouseleave', function() {
            this.classList.remove('is-open');
        });
        // For mobile
        drop.querySelector('a').addEventListener('click', function(e) {
            if (window.innerWidth < 700) {
                e.preventDefault();
                drop.classList.toggle('is-open');
            }
        });
    });
});

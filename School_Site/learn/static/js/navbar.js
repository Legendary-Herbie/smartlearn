// Responsive navbar and dropdown logic

document.addEventListener('DOMContentLoaded', function() {
    const burger = document.getElementById('navbarBurger');
    const navMenu = document.getElementById('navbarMenu');
    if (burger && navMenu) {
        burger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            burger.classList.toggle('active');
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
        const link = drop.querySelector('a');
        if (link) {
            link.addEventListener('click', function(e) {
                if (window.innerWidth < 700) {
                    e.preventDefault();
                    drop.classList.toggle('is-open');
                }
            });
        }
    });
});

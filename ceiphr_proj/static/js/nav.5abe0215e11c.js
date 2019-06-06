document.addEventListener('DOMContentLoaded', function () {
    document.getElementById("navbar-burger").addEventListener('click', function () {
        // Get all "navbar-burger" elements
        $navbarBurgers = document.getElementById("navbar-burger")

        // Get the target from the "data-target" attribute
        target = $navbarBurgers.dataset.target;
        $target = document.getElementById(target);
        $navbar = document.getElementById('navbar');

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $navbarBurgers.classList.toggle('is-active');
        $target.classList.toggle('is-active');
        $navbar.classList.toggle('increase-opacity');

    });
});
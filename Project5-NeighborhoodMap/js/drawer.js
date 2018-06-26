/*
 * Open the drawer when the menu ison is clicked.
 */
var menu = document.querySelector('#menu');
var drawer = document.querySelector('.list');

menu.addEventListener('click', function(e) {
  drawer.classList.toggle('open');
  e.stopPropagation();
});
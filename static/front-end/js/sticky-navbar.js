
// Get the navbar
var navbar = document.getElementById("header-nav-bar");
var main_nav_div = document.getElementById('nav');


// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function navStickyOnScroll() {
if (window.pageYOffset >= sticky) {
  navbar.classList.add("sticky");
  main_nav_div.style.background = "white";
  main_nav_div.style.boxShadow = "0 8px 6px -6px black";
  
} else {
  navbar.classList.remove("sticky");
  main_nav_div.style.background = "none";
  main_nav_div.style.boxShadow = "0px 0px 0px 0px";
//   document.body.scrollTop = 0;
//   document.documentElement.scrollTop = 0;
}
}

window.onscroll = ()=>{
    navStickyOnScroll();
}


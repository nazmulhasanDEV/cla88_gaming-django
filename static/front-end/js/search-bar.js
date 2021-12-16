// search bar 

const click_to_search_here = document.getElementById('click-to-search-here');
const search_bar_main_div = document.getElementById('search-bar-main-div');
const search_form = document.getElementById('search-form');
const hide_search_bar = document.querySelector('.search_close_btn');

// main nav options
const main_nav_options = document.querySelector('.main-nav-options');

function viewSearchBar(el, el1){
el1.style.visibility = 'hidden';
el.style.display = 'inline';
}

function hideSearchBar(el, el1) {
el.style.display = 'none';
el1.style.visibility = 'visible';
}

click_to_search_here.onclick = (event) =>{
viewSearchBar(search_form, main_nav_options);
}
hide_search_bar.onclick = () =>{
hideSearchBar(search_form, main_nav_options);
}
// tabs for most recent and most favourite
function mostRecentPopVisited(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }


//   date

const today_eng_date = document.getElementById('today_eng_date');

const weekday = {
    '0' : "রবিবার",
    '1' : "সোমবার",
    '2' : "মঙ্গলবার",
    '3' : "বুধবার",
    '4' : "বৃহস্পতিবার",
    '5' : "শুক্রবার",
    '6' : "শনিবার",
};

const month = {
    '0': "জানুয়ারী",
    '1': "ফেব্রুয়ারী",
    '2': "মার্চ",
    '3': "এপ্রিল",
    '4': "মে",
    '5': "জুন",
    '6': "জুলাই",
    '7': "আগস্ট",
    '8': "সেপ্টেম্বর",
    '9': "অক্টোবর",
    '10': "নভেম্বর",
    '11': "ডিসেম্বর",
};

function engToBD(year){

var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();


var today_date = today.getDate().toString();
let today_date_in_bd = '';

    let engYear = year; // ['2', '0', '2', '1']
    let yearInBd = '';

    const engToBDNumber = {
        '0' : "০",
        '1' : "১",
        '2' : "২",
        '3' : "৩",
        '4' : "৪",
        '5' : "৫",
        '6' : "৬",
        '7' : "৭",
        '8' : "৮",
        '9' : "৯",
    };

    for (let i=0; i<engYear.length; i++){
      yearInBd += engYear[i].replace(engYear[i], engToBDNumber[year[i]]);
    }

    for (let i=0; i<today_date.length; i++){
      today_date_in_bd += today_date[i].replace(today_date[i], engToBDNumber[today_date[i]]);
    }
    


    
    today = weekday[today.getDay()] +", " + today_date_in_bd + ' ' + month[today.getMonth()] + ' ' + yearInBd;

    today_eng_date.textContent = today;
}
var today = new Date();

engToBD(today.getFullYear().toString());



// sticky nav bar
// When the user scrolls the page, execute myFunction
window.onscroll = function() {
  myFunction();
  scroll_to_topF();
};



// Get the navbar
var navbar = document.getElementById("header-nav-bar");
var main_nav_div = document.getElementById('nav');


// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
    main_nav_div.style.background = "white";
    main_nav_div.style.boxShadow = "0 8px 6px -6px black";
  } else {
    navbar.classList.remove("sticky");
    main_nav_div.style.background = "none";
    main_nav_div.style.boxShadow = "0px 0px 0px 0px";
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}




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


// scroll to top
const scroll_to_top = document.querySelector('.scroll_to_top');

function scroll_to_topF(){
  if (document.body.scrollTop >= 0 && document.documentElement.scrollTop >= 0) {
    scroll_to_top.style.visibility = 'visible';
  }
  if (document.body.scrollTop < 100 && document.documentElement.scrollTop < 100) {
    scroll_to_top.style.visibility = 'hidden';
  }
}


function click_to_reach_top(){
  // scrollTo, scroll, scrollIntoView are same
  document.documentElement.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}

scroll_to_top.onclick = ()=>{
  click_to_reach_top();
}

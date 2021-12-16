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



// scroll to top
const scroll_to_top = document.querySelector('.scroll_to_top');

function scroll_to_topF(){
if (document.documentElement.scrollTop >= 0) {
  scroll_to_top.style.visibility = 'visible';
}
if (document.documentElement.scrollTop < 100) {
  scroll_to_top.style.visibility = 'hidden';
}
}
// document.body.scrollTop >= 0 && 
// document.body.scrollTop < 100 && 

// sticky nav bar
// When the user scrolls the page, execute myFunction
window.onscroll = function() {
  scroll_to_topF();
};




// ads

const ads_sec = document.querySelector('.section-for-ads');
const blur_body = document.querySelector('body');

const close_ads = document.querySelector('.close_ads');

window.onload = ()=>{
  ads_sec.style.visibility='visible';
}

close_ads.onclick = ()=>{
  ads_sec.style.visibility='hidden';
  blur_body.style.overflowY = 'scroll';
}






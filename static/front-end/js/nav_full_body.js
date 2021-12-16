const full_body_nav = document.querySelector('#full_body_nav');
const nav_full_body = document.querySelector('.nav_full_body');
const close_full_nav = document.querySelector('.close_full_nav');
const full_body = document.querySelector('body');


full_body_nav.onclick =()=>{
    nav_full_body.classList.remove('hide_full_navBar');
    nav_full_body.classList.add("show_full_navBar");
    full_body.style.overflowY = 'hidden';
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

close_full_nav.onclick = ()=>{
    nav_full_body.classList.remove("show_full_navBar");
    nav_full_body.classList.add("hide_full_navBar");
    full_body.style.overflowY = 'visible';
    nav_full_body.style.display = 'block';
}
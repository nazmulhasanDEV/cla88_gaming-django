const nav_cat_list = document.querySelectorAll('.nav-main-li');
const nav_main_options = document.querySelector('.main-nav-options');


    nav_main_options.onclick = (e)=>{
        for (let i = 0; i<nav_cat_list.length; i++){
            if (nav_cat_list[i].children[0] == e.target) {
                nav_cat_list[i].children[0].classList.add('active_category');
                    console.log("I am here");
            }
            if(nav_cat_list[i].children[0] != e.target) {
                nav_cat_list[i].children[0].classList.remove('active_category');
            }
        }
    }


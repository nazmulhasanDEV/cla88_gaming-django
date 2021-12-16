// custom ads section at header
const custom_header_ads_section = document.querySelector('.section-for-custom-ads');
const close_custom_header_ads_btn   = document.querySelector('.close_custom_header_ads');

const close_custom_header_ads = (element) =>{
    element.style.display = 'none';
}

close_custom_header_ads_btn.onclick =() =>{
    close_custom_header_ads(custom_header_ads_section);
}

// section for ads at middle
const section_for_ads = document.querySelector('.div_for_add_1');
const close_section_for_ads_btn = document.querySelector('.close_section_for_ads_btn');

close_section_for_ads_btn.onclick = () =>{
    close_custom_header_ads(section_for_ads);
}

const section_for_ads_mddle_2 = document.querySelector('.div_for_middle_ads_2');
const close_ads_middle_2 = document.querySelector('#close_ads_middle_2');

close_ads_middle_2.onclick = () =>{
    close_custom_header_ads(section_for_ads_mddle_2);
}
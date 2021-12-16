const breaking_news_title = document.getElementById('breaking-news-title');

const text_slider_main_div = document.getElementById('text-slider-main-div');
const textSliderContent = document.getElementById('text-slider-content');

const breaking_news_title_width = breaking_news_title.clientWidth; 

const main_div_width = text_slider_main_div.clientWidth; // main_div width

const textSliderContentWidth = textSliderContent.clientWidth; // content width

const total_width = main_div_width + (textSliderContentWidth); // main_div + content width * 2


// transform to left
var transform_to_left = main_div_width - breaking_news_title_width;

var transform_to_right_after_one_cycle = total_width - breaking_news_title_width;

var move_to_left = 1;

const sliderFunc = (element) =>{
    if (move_to_left < total_width) {
        element.style.transform = 'translateX(' + ((main_div_width)-move_to_left) + 'px)';
        move_to_left = move_to_left + 1;

        if (move_to_left >= total_width) {
            element.style.transform = 'translateX(' + (total_width) + 'px)';
            move_to_left = 1;
        }
    }
    else {
        element.style.transform = 'translateX(' + (main_div_width) + 'px)';
    }
}



var calling_slider = setInterval(()=>{
    sliderFunc(textSliderContent);
}, 20);

const stopSlider = () =>{
    clearInterval(calling_slider);
};

textSliderContent.onmouseover = ()=>{
    stopSlider();
};

textSliderContent.onmouseout = ()=> {
    calling_slider = setInterval(()=>{
        sliderFunc(textSliderContent);
    }, 20);
};





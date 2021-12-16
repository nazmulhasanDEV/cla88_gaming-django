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
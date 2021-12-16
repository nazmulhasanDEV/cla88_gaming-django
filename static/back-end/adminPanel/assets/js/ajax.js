// breaking news section ##########################################################################

let breaking_news_action_center = document.querySelectorAll('#breaking_news_action_center');

let get_id_value_of_dropdown = document.querySelectorAll('.activate_or_deactivate_breaking_news');


function change_status(element){

element.onchange= (event)=>{

// starts ajax method
$.ajax({

url: '',
type: 'get',
data: {
   news_status: event.target.value
},
success: function(response){
    location.reload();
},

});
// ends ajax method

}
}



















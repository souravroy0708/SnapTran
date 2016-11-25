//********************************* STARTS HERE ***********
//For User input form validation error message
var message;
function commonPnotify(type,message) {
    var opts = {
        shadow: false
    };
    switch (type) {
        case 'userInputValidationError':
            opts.title ="Error :)";
            opts.text = "Please enter valid first name";
            opts.type = "info";
            break;
      
        
     }
     new PNotify(opts);
  }

var form = $("#gpFormtest");
form.validate({
       rules: {
            name_text: {
              required:true,
              minlength:3,
            },
        
      },
        messages: {
            name_text:{
            required:"First Name cannot be blank",
            minlength : "First name should be atleast 3 characters",
          }
          }
});



$(document).ready(function(){

  
    $('[data-toggle="tooltip"]').tooltip();
$("#user_input_submit").removeAttr('disabled','disabled');
    $("#user_input_submit_test").click(function(){
      
      $(".record_tr").hide();
      var name_text = $("#name_text").val();
      $("#user_input_submit").attr('disabled','disabled');
      $("#aue_not_found").hide();
      $("#aueTable").hide();
      formValidation=form.valid();
    
    if(formValidation == false){
        commonPnotify('userInputValidationError');
        $("#user_input_submit").removeAttr('disabled','disabled');
        }
       else{
  
  $("#aueLoadingSpinner").show();
  $(".loading_div").show();
  
    $.ajax({
    url : "get-gender-prediction/", 
    type : "GET", 
    timeout: '6000000000',
    data : { names : name_text}, 
    success : function(data) {
      $(".loading_div").hide();
      $("#aueLoadingSpinner").hide();
      var search_result = data["result"]
      counter  = 1
      for (i = 0; i < search_result.length; i++) {
        $("#aueTable").show();
        $("#aue_not_found").hide();
        $("#record_tr_"+counter).show();
          result_url = search_result[i]
          $("#s_no_"+counter).text(counter);
          $("#name_"+counter).text(result_url["name"]);
          $("#predictions_"+counter).text(result_url["prediction"]);
          counter ++;
        }
        if(search_result.length <= 0){
          $("#aue_not_found").show();
          $("#aueTable").hide();
        }
        $("#user_input_submit").removeAttr('disabled','disabled');
        },
    error : function(xhr,errmsg,err) {
      alert("Timeout error.Please check your internet connection or enter a valid url and then try again "+errmsg);
         console.log(xhr.status + ": " + xhr.responseText+"xhr"+xhr+"err"+err);
         $("#user_input_submit").removeAttr('disabled','disabled');
         $("#aueLoadingSpinner").hide();
         $(".loading_div").hide();
    }
});
}

});
});




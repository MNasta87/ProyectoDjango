function toggleChevron(e) {
  $(e.target)
      .prev('.panel-heading')
      .find("i.indicator")
      .toggleClass('glyphicon-chevron-down glyphicon-chevron-right');
      
  $(e.target).parent().toggleClass('panel-default panel-primary');           
}
$('#accordion').on('hidden.bs.collapse shown.bs.collapse', toggleChevron);

//----------------------------------------------------------------------
// when the submit is clicked form check
//----------------------------------------------------------------------

$(function() {
  $('#submitform').click(function() {

  // traverse all the required elements looking for an empty one
  $("#myForm input[required='required']").each(function() {

      // if the value is empty, that means that is invalid
      if ($(this).val() == "") {

          // hide the currently open accordion and open the one with the invalid field
          $(".panel-collapse.in").removeClass("in");
          $(this).closest(".panel-collapse").addClass("in").css("height","auto");     
          
          // toggle bar color
          $(".panel-group").children().removeClass("panel-primary");
          $(".panel-group").children().addClass("panel-default");
          $(this).closest(".panel-default").toggleClass('panel-default panel-primary');  
          
          // toggleChevron
          $(".panel-heading").find("i.indicator").removeClass("glyphicon-chevron-down");
          $(".panel-heading").find("i.indicator").addClass("glyphicon-chevron-right");
          $(this).closest(".panel-collapse").parent().find("i.indicator").toggleClass('glyphicon-chevron-down glyphicon-chevron-right');
         
          
          // stop scrolling through the required elements
          return false;
      }
  });    
  
  
  });
});
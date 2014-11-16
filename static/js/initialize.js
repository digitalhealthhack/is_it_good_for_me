$(document).ready(function(){
  $("#main").accordion({
    heightStyle: "content",
    active: false,
    collapsible: true
   });
  console.log("document ready working")
  var controller = new Controller();
  controller.addAllEventListeners();
})

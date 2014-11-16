
Controller = function(){
  this.diseases = [];
  this.treatment = "";
  this.view = new View();
};

Controller.prototype = {
  addAllEventListeners: function() {
    var controller = this;
    $('#button').click(function(event) {
      event.preventDefault();
      controller.clearDiseaseObjects();
      console.log("click listener works");
      controller.treatment = $('#treatment_field').map(function (index) {
            return ($(this))[0].value;
        })[0];
      console.log(controller.treatment)
      controller.getDiseaseData();
    });
  },

  getDiseaseData: function() {
    console.log("inside getDiseaseData");
    var controller = this;
    $.post( "/diseases", controller.treatment, function(data) {
      console.log("successful ajax");
      controller.parseJsonDiseaseData(data);
      controller.view.createTitle(controller.treatment);
      controller.view.createList(controller.diseases);
      $('body').scrollTo('#banner');
    });
  },

  parseJsonDiseaseData: function(diseaseData){
    console.log("inside parseJsonDiseaseData")
    var that = this;
    $.each(diseaseData, function(index, diseaseDatum){
      console.log("inside json parse loop")
      var disease = new Disease(diseaseDatum);
      that.diseases.push(disease);
    })
  },

  clearDiseaseObjects: function() {
    console.log("inside clearDiseaseData")
    this.diseases = [];
    this.treatment = "";
    $("#main").empty();
    $("#title").empty();
  }
};

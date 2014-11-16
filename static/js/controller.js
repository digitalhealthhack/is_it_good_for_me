
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
      controller.createCharts();
      $('body').scrollTo('#banner');
    });
  },

  createCharts: function() {
    var controller = this;
    for (var i = 0; i < controller.diseases.length; i++) {
      new Morris.Bar({
        // ID of the element in which to draw the chart.
        element: controller.diseases[i].id.toString()+"bar",
        // Chart data records -- each entry in this array corresponds to a point on
        // the chart.
        data: [
          { year: 'Metric1', value: controller.diseases[i].levels[0] },
          { year: 'Metric2', value: controller.diseases[i].levels[1] },
          { year: 'Metric3', value: controller.diseases[i].levels[2] },
          { year: 'Metric4', value: controller.diseases[i].levels[3] },
          { year: 'Metric5', value: controller.diseases[i].levels[4] }
        ],
        // The name of the data record attribute that contains x-values.
        xkey: 'year',
        // A list of names of data record attributes that contain y-values.
        ykeys: ['value'],
        // Labels for the ykeys -- will be displayed when you hover over the
        // chart.
        labels: ['Metrics'],
        parseTime:false
      });
    new Morris.Donut({
      element: controller.diseases[i].id.toString()+"donut",
      data: [
        {label: "Confidence", value: controller.diseases[i].confidence},
        {label: "", value: 20},
      ]
      });
    }
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

View = function() {};

View.prototype = {
  createList: function(diseaseArray) {
    console.log("inside createList")
    for (var i = 0; i < diseaseArray.length; i++) {
      console.log("inside for loop")
      var diseaseObject = diseaseArray[i];
      var htmlstring = "<h2 style='clear:both;'><a>{{name}}</a></h2><div><h3>{{title}}</h3><h4>{{content}}</h4><div><div id='{{id}}bar' style='float:left;height:250px;width:400px;text-align:center;'></div></div><div id='{{id}}donut' style='float:right;height:250px;width:400px;text-align:center;'></div></div></div>";
      // var htmlstring = "<h2><a>{{name}}</a></h2><div><table><tr><th>Goodness</th><th>Confidence</th><th>Article Title</th><th>Article Content</th></tr><td>{{levels}}</td><td>{{confidence}}</td><td>{{title}}</td><td>{{content}}</td></table></div>"
      var output = Mustache.render(htmlstring, diseaseObject);
      console.log(output);
      $("#main").append($(output));
      $("#main").accordion( "refresh" );
    }
  },
  createTitle: function(treatment) {
    console.log("inside createTitle")
    console.log(treatment)
    var treatmentObject = {"treatment": treatment};
    var htmlstring = "<h2>{{treatment}} is correlated with: </h2>";
    var output = Mustache.render(htmlstring,treatmentObject);
    $("#title").append($(output));
  }
};

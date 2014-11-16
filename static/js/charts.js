BarChart = function(object){
  var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .staggerLabels(false)
      .tooltips(false)
      .showValues(true)
      .transitionDuration(350)
      ;
  chart.xAxis.axisLabel(object.xAxisLabel || null);
  d3.select(object.divSelector)
      .datum(object.chartData)
      .call(chart);

  nv.utils.windowResize(chart.update);
  return chart;
};

StackedBarChart = function(object){
  var chart = nv.models.multiBarChart()
    .transitionDuration(350)
    .reduceXTicks(false)
    .rotateLabels(0)
    .showControls(true)
    .groupSpacing(0.1)
    .stacked(true)
  ;

  chart.xAxis.axisLabel(object.xAxisLabel || null);
  chart.yAxis
    .tickFormat(d3.format(',.1f'));

  // chart.groupSpacing(0.5);

  d3.select(object.divSelector)
    .datum(object.chartData)
    .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
};

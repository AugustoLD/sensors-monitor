var chartTemperature; // global

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */

var lastTimestampTemperature = 0; //global
function requestDataTemperature() {
  var url = "http://179.106.206.211:5000/sensors/api/temperature/" + lastTimestampTemperature;

  $.ajax({
      type: "GET",
      url: url,
      dataType: "json",
      success: function (pointsArray){
        var point;

        for(var i = 0; i < pointsArray.length; i++){
          point = [pointsArray[i].timestamp, pointsArray[i].degree];
          chartTemperature.series[0].addPoint(point, false, false);
        };

        lastTimestampTemperature = point[0];
        chartTemperature.redraw();

        //call it again after one second and a half
        setTimeout(requestDataTemperature, 1500);

        }
    });
};


$(document).ready(function() {
    chartTemperature = new Highcharts.StockChart({
        chart: {
            renderTo: 'ctnTemperature',
            events: {
                load: requestDataTemperature
            }
        },
        rangeSelector : {
            buttons : [{
                type : 'minute',
                count : 30,
                text : '30m'
            }, {
                type : 'minute',
                count : 10,
                text : '10m'
            }, {
              type : 'minute',
              count : 5,
              text : '5m'
            }, {
              type : 'minute',
              count : 1,
              text : '1m'
            }, {
                type : 'all',
                count : 1,
                text : 'All'
            }],
            selected : 3
        },
        title: {
            text: 'Temperature'
        },
        xAxis: {
            type: 'datetime',
        },
        yAxis: {
            title: {
                text: 'Celsius',
            },
            labels: {
              formatter: function() {
                return this.value + "°C";
              }
            },
        },
        series: [{
            name: 'Random data',
            data: [],
            type: 'spline',
            shadow: true,
            color: 'rgba(165, 42, 42, 0.8)'
        }]
    });
});

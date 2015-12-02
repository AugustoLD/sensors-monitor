var chartHumidity; // global

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
var lastTimestampHumidity = 0; //global
function requestDataHumidity() {
  var url = "http://179.106.206.211:5000/sensors/api/humidity/" + lastTimestampHumidity;
  $.ajax({
      type: "GET",
      url: url,
      dataType: "json",
      success: function (pointsArray){
        var point;

        for(var i = 0; i < pointsArray.length; i++){
          point = [pointsArray[i].timestamp, pointsArray[i].percent];
          chartHumidity.series[0].addPoint(point, false, false);
        };

        lastTimestampHumidity = point[0];
        chartHumidity.redraw();

       //call it again after one second and a half
       setTimeout(requestDataHumidity, 1500);

      }
    });
};


$(document).ready(function() {

    chartHumidity = new Highcharts.StockChart({
        chart: {
            renderTo: 'ctnHumidity',
            events: {
                load: requestDataHumidity
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
            text: 'Humidity'
        },
        xAxis: {
            type: 'datetime',
        },
        yAxis:{
            title: {
                text: 'Percent',
            },
            opposite: false,
            labels: {
              formatter: function() {
                return this.value + "%";
              }
            }
          },
        series: [{
            name: 'Random data',
            data: [],
            type: 'spline',
            shadow: true
        }]
    });
});

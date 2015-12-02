var chartLuminosity; // global

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
var lastTimestampLuminosity = 0; //global
function requestDataLuminosity() {
  var url = "http://179.106.206.211:5000/sensors/api/luminosity/" + lastTimestampLuminosity;
  $.ajax({
      type: "GET",
      url: url,
      dataType: "json",
      success: function (pointsArray){
        var point;

        for(var i = 0; i < pointsArray.length; i++){
          point = [pointsArray[i].timestamp, pointsArray[i].intensity];
          chartLuminosity.series[0].addPoint(point, false, false);
        };

        lastTimestampLuminosity = point[0];
        chartLuminosity.redraw();

       //call it again after one second and a half
       setTimeout(requestDataLuminosity, 1500);

      }
    });
};

$(document).ready(function() {
    chartLuminosity = new Highcharts.StockChart({
        chart: {
            renderTo: 'ctnLuminosity',
            events: {
                load: requestDataLuminosity
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
                selected : 4
        },
        title: {
            text: 'Luminosity'
        },
        xAxis: {
            type: 'datetime',
        },
        yAxis: {
            title: {
                text: 'Degree of brightness',
            },
            plotBands: [
                  {
                    from: 0,
                    to: 10,
                    color: 'rgba(0, 0, 0, 0.3)',
                    label: {
                        text: 'Muito Escuro'
                    }
                  },{
                    from: 11,
                    to: 200,
                    color: 'rgba(0, 0, 0, 0.1)',
                    label: {
                        text: 'Escuro'
                    }
                  },{
                      from: 201,
                      to: 500,
                      color: 'rgba(217, 217, 25, 0.2)',
                      label: {
                          text: 'Iluminado'
                      }
                  },{
                      from: 501,
                      to: 800,
                      color: 'rgba(217, 217, 25, 0.1)',
                      label: {
                          text: 'Claro'
                    }
                  },{
                      from: 801,
                      to: 1023,
                      color: 'rgba(217, 217, 25, 0.001)',
                      label: {
                          text: 'Muito Claro'
                    }
                  }
                ]
        },
        series: [{
            name: 'Random data',
            data: [],
            type: 'spline',
            color:  'rgba(217,217,25, 0.9)'
        }]
    });
});

/**
 * Created by babackkhosravikatoli on 9/10/17.
 */
google.charts.load('current', {packages: ['corechart', 'bar','line']});
google.charts.setOnLoadCallback(drawAxisTickColors);
google.charts.setOnLoadCallback(drawSeriesChart);
//google.charts.setOnLoadCallback(drawChart);
google.charts.setOnLoadCallback(drawBasic);
google.charts.setOnLoadCallback(drawMultSeries);
google.charts.setOnLoadCallback(example);



$(document).ready(function() {
    $("#analysisForm").on('submit', function(event){
        event.preventDefault();
        $("#analysisResponse").html("Running analysis. Give me a second. In some cases, give me a minute. I'm running a lot of calculations. Give me a break. You run try to do it really quickly. That's what I thought. You'll see the chart pop up when I'm done.");
        $.ajax({
            type: 'POST',
            url: '/analysis',
            data: {
                analysis: $("#analysisText").val()
            },
            success: function(result) {
                //text = result.resultpopup;
                yara = result.yararesponse;
                array = result.array;
                number = result.number;
                buy = result.Buy;
                hold = result.Hold;
                sell = result.Sell;
                q1 = result.q1;
                q2 = result.q2;
                q3 = result.q3;
                q4 = result.q4;
                date = result.date;
                stock = result.stock;
                console.log(stock);
                sharperatio_user = result.sharpeuser;
                sharperatio_new = result.sharpewhatif;
                totalreturn_new = result.total_return_new;
                totalreturn_user = result.total_return_usr;
                stdport_new = result.STD_Port_new;
                stdport_user = result.STD_usr_Port;
                //portfolio = result.portfoliotable;
                console.log(stock);
                $("#analysisResponse").html(yara);
                if (number == 0) {
                    drawAxisTickColors(buy, hold, sell, stock)
                } else if (number == 1) {
                    drawMultSeries(q1,q2,q3,q4,stock);
                } else if (number == 2) {
                    drawBasic(array);
                } else if (number == 7) {
                    drawSeriesChart(sharperatio_user,sharperatio_new,totalreturn_new,totalreturn_user,stdport_new,stdport_user)
                }
                //drawBasic(array);
                }
            });
        });
    });


// $(document).ready(function() {
//     $("#analysisInputMic").click(function(event){
//         event.preventDefault();
//         $("#analysisText").val("Speak into the microphone!");
//         $(".analysisResponse").html("Give me a second after your speak. Running analysis.");
//         $.ajax({
//             type: 'POST',
//             url: '/analysis',
//             data: {
//                 analysis: $("#analysisText").val()
//             },
//             success: function(result) {
//                 //text = result.resultpopup;
//                 yara = result.yararesponse;
//                 array = result.array;
//                 number = result.number;
//                 buy = result.Buy;
//                 hold = result.Hold;
//                 sell = result.Sell;
//                 q1 = result.q1;
//                 q2 = result.q2;
//                 q3 = result.q3;
//                 q4 = result.q4;
//                 date = result.date;
//                 stock = result.stock;
//                 sharperatio_user = result.sharpeuser;
//                 sharperatio_new = result.sharpewhatif;
//                 totalreturn_new = result.total_return_new;
//                 totalreturn_user = result.total_return_usr;
//                 stdport_new = result.STD_Port_new;
//                 stdport_user = result.STD_usr_Port;
//                 //portfolio = result.portfoliotable;
//                 console.log(yara);
//                 $("#analysisResponse").html(yara);
//                 if (number == 0) {
//                     drawAxisTickColors(buy, hold, sell, stock)
//                 } else if (number == 1) {
//                     drawMultSeries(q1,q2,q3,q4,stock);
//                 } else if (number == 2) {
//                     drawBasic(array);
//                 } else if (number == 7) {
//                     drawSeriesChart(sharperatio_user,sharperatio_new,totalreturn_new,totalreturn_user,stdport_new,stdport_user)
//                 }
//                 //drawBasic(array);
//                 }
//             });
//         });
//     });



function example() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Date');
        data.addColumn('number', 'A.I.');
        data.addColumn('number', 'Human');
        data.addRows([
            ['2017',50,100],['',100,101],['',250,102],
            ['',500,103],['',750,104],['',1000,105],
            ['',1500,106],['',2000,107],['',3000,108],
            ['',5000,109],['',9000,110],['∞',15000,15000]
        ]);

        var options = {
            title: 'Example of your analysis results. Let there be light..∞ is the year we and AC fuse',
            hAxis: {
            title: 'Average IQ of Humans vs. A.I.'
            },
            vAxis: {
            title: 'IQ'
            },
            animation: {
            startup:true,
            duration: 1000,
            easing: 'out'
            }
        };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

      chart.draw(data, options);
    }




function drawBasic(array) {
        var array = array;
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Date');
        data.addColumn('number', 'Portfolio');
        data.addColumn('number', 'S&P 500');
        data.addRows(
            array
        );

        var options = {
            title: 'Backtest Complete for Your Portfolio',
            hAxis: {
            title: 'Date'
            },
            vAxis: {
            title: 'Index Value'
            },
            animation: {
            startup:true,
            duration: 1000,
            easing: 'out'
            }
        };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

      chart.draw(data, options);
    }



function drawAxisTickColors(buy, hold, sell, stock) {
        var a = eval(buy);
        var b = eval(hold);
        var c = eval(sell);
        var stock = stock;
  var data = google.visualization.arrayToDataTable([
    ['Analyst Recommendations', '%'],
    ['Buy', a],
    ['Hold', b],
    ['Sell', c]
  ]);

  var options = {
    title: 'Expert Consensus for: ' + stock,
    chartArea: {width: '50%'},
    hAxis: {
      title: 'Recent expert opinions.',
      minValue: 0,
      textStyle: {
        bold: true,
        fontSize: 12,
        color: '#4d4d4d'
      },
      titleTextStyle: {
        bold: true,
        fontSize: 18,
        color: '#4d4d4d'
      }
    },
    vAxis: {
      title: '',
      textStyle: {
        fontSize: 14,
        bold: true,
        color: '#848484'
      },
      titleTextStyle: {
        fontSize: 14,
        bold: true,
        color: '#848484'
      }
    },
    animation: {
    startup:true,
    duration: 1000,
    easing: 'out'
    }
  };
  var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}




function drawMultSeries(q1,q2,q3,q4,stock) {
    var a = q1;
    var b = q2;
    var c = q3;
    var d = q4;
    var stock = stock;
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Earnings');
    data.addColumn('number', 'Expected Profit Per Share');
    data.addColumn('number', 'Actual Profit Per Share');

    data.addRows([
        a,
        b,
        c,
        d
    ]);

    var options = {
        title: 'Comparison of Actual vs Expected Earnings for ' + stock.toUpperCase(),
        hAxis: {
            title: 'Last Four Quarters',
            format: 'h:mm a',
            viewWindow: {
                min: [7, 30, 0],
                max: [17, 30, 0]
            }
        },
        vAxis: {
            title: 'Profit Per Share'
        },
        animation: {
        startup:true,
        duration: 1000,
        easing: 'out'
        }
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));

    chart.draw(data, options);

}



function drawSeriesChart(sharperatio_user,sharperatio_new,totalreturn_new,totalreturn_user,stdport_new,stdport_user) {
        var sharpeuser = eval(sharperatio_user);
        var sharpewhatif = eval(sharperatio_new);
        var total_return_new = eval(totalreturn_new);
        var total_return_usr = eval(totalreturn_user);
        var STD_Port_new = eval(stdport_new);
        var STD_usr_Port = eval(stdport_user);
    var data = google.visualization.arrayToDataTable([
        ['ID', 'Risk', 'Return', 'Portfolio', 'Sharpe Ratio'],
        ['New', STD_Port_new, total_return_new, 'New Portfolio', sharpewhatif],
        ['CUR', STD_usr_Port, total_return_usr, 'Current Portfolio', sharpeuser]
      ]);

      var options = {
        title: 'Risk to Return of your New Portfolio versus your Current Portfolio',
        hAxis: {title: 'Risk'},
        hAxis: {ticks: [0,4,8,12,16,20]},
        vAxis: {title: 'Return'},
        vAxis: {ticks: [0,4,8,12,16,20]},
        animation: {
            startup:true,
            duration: 1000,
            easing: 'out'
            },
        bubble: {textStyle: {fontSize: 11}}
      };

      var chart = new google.visualization.BubbleChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }


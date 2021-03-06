<?php
require_once 'header.php';
?>

<style>
.video-container {
  max-width: 600px;
  margin: auto;
}
.demo-placeholder,
a {
    -khtml-user-select: none;
    -o-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
  }
#plot-chart {
    height: 400px;
}
.video-placeholder.demo-placeholder {
  height: 200px;
}
#attention-bar {
  background-color: orange;
}
#happiness-bar {
  background-color: green;
}
#neutral-bar {
  background-color: lightgray;
}
#anger-bar {
  background-color: red;
}
#contempt-bar {
  background-color: brown;
}
#disgust-bar {
  background-color: darkgreen;
}
#surprise-bar {
  background-color: pink;
}
#fear-bar {
  background-color: purple;
}
#sadness-bar {
  background-color: darkblue;
}
.tab-bar {
  padding: 15px;
  text-align: center;
}
.tab-bar ul {
  list-style: none;
  list-style-type: none;
  margin: auto;
  padding: 0;
}
.tab-bar ul li {
  display: inline-block;
}
a.tab-button {
    padding: 10px;
    cursor: pointer;
}
a.tab-button.active {
  background: #efefef;
}
.dashboard_graph {
  overflow: hidden;
}
</style>
          <!-- top tiles -->
          <div class="row tile_count">
            <div class="col-md-3 col-sm-4 col-xs-6 tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Max Attentive People</span>
              <div class="count" id="max-attentive">123</div>
            </div>
            <div class="col-md-3 col-sm-4 col-xs-6 tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Average Happiness Index</span>
              <div class="count" id="avg-happiness-index">123</div>
            </div>
            <div class="col-md-3 col-sm-4 col-xs-6 tile_stats_count">
              <span class="count_top"><i class="fa fa-clock-o"></i> Average Attention Index</span>
              <div class="count" id="avg-attention-index">0.43</div>
            </div>
            <div class="col-md-3 col-sm-4 col-xs-6 tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Most common sentiment</span>
              <div class="count green" id="common-sentiment">Happiness</div>
              <span class="count_bottom" id="sentiment-percentage"><i class="green">86% </i> Average</span>
            </div>
          </div>
          <!-- /top tiles -->
          <div class="row">
            <div class="col-md-12 col-sm-12 col-xs-12">
              <div class="dashboard_graph">
                <div class="col-md-9 col-sm-9 col-xs-12">
                  <div id="plot-attention" class="demo-placeholder"></div>
                </div>
                <div class="col-md-3 col-sm-3 col-xs-12 bg-white">
                  <div class="x_title">
                    <h2>Attention</h2>
                    <div class="clearfix"></div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Average Attention</p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="attention-bar-avg" class="progress-bar attention" role="progressbar"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
          </div>
          <br>
          <div class="row">
            <div class="col-md-12 col-sm-12 col-xs-12">
              <div class="dashboard_graph">
                <div class="col-md-9 col-sm-9 col-xs-12">
                  <div id="plot-chart" class="demo-placeholder"></div>
                </div>
                <div class="col-md-3 col-sm-3 col-xs-12 bg-white">
                  <div class="x_title">
                    <h2>Average Sentiments</h2>
                    <div class="clearfix"></div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Happiness <span class="happiness-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="happiness-bar" class="progress-bar happiness" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Neutral <span class="neutral-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="neutral-bar" class="progress-bar neutral" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Contempt <span class="contempt-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="contempt-bar" class="progress-bar contempt" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Disgust <span class="disgust-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="disgust-bar" class="progress-bar disgust" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Anger <span class="anger-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="anger-bar" class="progress-bar anger" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Surprise <span class="surprise-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="surprise-bar" class="progress-bar surprise" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Fear <span class="fear-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="fear-bar" class="progress-bar fear" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Sadness <span class="sadness-percent"></span></p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div id="sadness-bar" class="progress-bar sadness" role="progressbar"  ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
          </div>
          <br>
          <div class="row">
            <div class="col-md-12 col-sm-12 col-xs-12">
              <div class="dashboard_graph">
                <div class="video-container">
                  <audio
                      id="video"
                      class="video-active"
                      width="100%"
                      style="display:block;width:100%"
                      controls="controls">
                      <source src="video.mp4" type="audio/mp4">
                  </audio>
                </div>
                <div class="tab-bar">
                  <ul class="plot-tabs">
                    <li><a class="tab-button active" data-tab="attention">Attention</a></li>
                    <li><a class="tab-button" data-tab="happiness">Happiness</a></li>
                    <li><a class="tab-button" data-tab="sadness">Sadness</a></li>
                    <li><a class="tab-button" data-tab="anger">Anger</a></li>
                    <li><a class="tab-button" data-tab="surprise">Surprise</a></li>
                    <li><a class="tab-button" data-tab="fear">Fear</a></li>
                    <li><a class="tab-button" data-tab="contempt">Contempt</a></li>
                    <li><a class="tab-button" data-tab="disgust">Disgust</a></li>
                    <li><a class="tab-button" data-tab="neutral">Neutral</a></li>
                  </ul>
                </div>
                <div id="plot-video-attention" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-happiness" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-sadness" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-anger" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-surprise" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-fear" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-contempt" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-disgust" class="video-placeholder demo-placeholder"></div>
                <div id="plot-video-neutral" class="video-placeholder demo-placeholder"></div>
                <br>
                <div class="x_title">
                  <h2>Key Phrases</h2>
                  <div class="clearfix"></div>
                </div>
                <div class="x_content">
                  <p id="keyphrases">ugi pula in cur</p>
                  <div class="clearfix"></div>
                </div>
              </div>
            </div>
          </div>
          <br>
<?php
require_once 'footer.php';
?>
<script>
var theVideoPlots = {
    "attention": {},
    "happiness": {},
    "sadness": {},
    "contempt": {},
    "anger": {},
    "neutral": {},
    "disgust": {},
    "surprise": {},
    "fear": {}
  };
$(document).ready(function() {
  var processData = function() {
    var a = <?=file_get_contents('results.json')?>;
    var graphData = {
      "attention": [],
      "happiness": [],
      "neutral": [],
      "anger": [],
      "contempt": [],
      "disgust": [],
      "surprise": [],
      "fear": [],
      "sadness": [],
  };
    d = a["averages"];
    graphData["speech"] = []
    for(var i=0; i<d.length; i++) {
      graphData["attention"].push([d[i]["frame"], d[i]["info"]["attentionIndex"]]);
      graphData["happiness"].push([d[i]["frame"], d[i]["info"]["averageHappiness"]]);
      graphData["neutral"].push([d[i]["frame"], d[i]["info"]["averageNeutral"]]);
      graphData["anger"].push([d[i]["frame"], d[i]["info"]["averageAnger"]]);
      graphData["contempt"].push([d[i]["frame"], d[i]["info"]["averageContempt"]]);
      graphData["disgust"].push([d[i]["frame"], d[i]["info"]["averageDisgust"]]);
      graphData["surprise"].push([d[i]["frame"], d[i]["info"]["averageSurprise"]]);
      graphData["fear"].push([d[i]["frame"], d[i]["info"]["averageFear"]]);
      graphData["sadness"].push([d[i]["frame"], d[i]["info"]["averageSadness"]]);
      graphData["speech"][d[i]["frame"]] = {"sentiment": d[i]["speech"], "kp": d[i]["keyphrases"]};
    }
    graphData["avgs"] = a["videoAverages"];
    return graphData;
  },
  setAttentionPlot = function() {
    graphData = processData();
    var options = {
                   series: {
                       curvedLines: {active: true}
                   },
                   yaxis: {
                     min: 0,
                     max: 1
                   }
                };
    $.plot($("#plot-attention"), [
      {
        data: graphData['attention'],
        lines: { show: true, lineWidth: 2, fill: true},
        curvedLines: {apply: true, tension: 0.5}
      },
      {
        data: graphData['attention'], color: '#f03b20',
        points: {show: true}
      }
    ], options);
  }
  setPlot = function() {
    graphData = processData();
    var options = {
                   series: {
                       curvedLines: {active: true},
                       stack: true,
                       lines: {
                         fill: true
                       }
                   },
                   yaxis: {
                     min: 0,
                     max: 1
                   }
                };
    $.plot($("#plot-chart"), [
      {
        data: graphData["happiness"],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'green'
      },
      {
        data: graphData["neutral"],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'grey'
      },
      {
        data: graphData["anger"],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'red'
      },
      {
        data: graphData['contempt'],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'brown'
      },
      {
        data: graphData['disgust'],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'darkgreen'
      },
      {
        data: graphData['surprise'],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'pink'
      },
      {
        data: graphData['fear'],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'purple'
      },
      {
        data: graphData['sadness'],
        lines: {
          show: true,
          lineWidth: 1,
        },
        curvedLines: {
          apply: true,
          tension: 0.5
        },
        color: 'darkblue'
      }
    ], options);
    // General data
    $("#max-attentive").text(graphData['avgs']['maxFaces']);
    $("#avg-happiness-index").text(parseFloat(graphData['avgs']['averageHappiness']*100).toFixed(2)+'%');
    $("#avg-attention-index").text(parseFloat(graphData['avgs']['attentionIndex']*100).toFixed(2)+'%');
    $("#attention-bar-avg").css("width", "42%");
    $("#common-sentiment").text(graphData['avgs']['mostCommon']);
    $("#sentiment-percentage").text(parseFloat(graphData['avgs']['mostCommonPercentage']*100).toFixed(2)+'%');
    // Sentiments
    $("#happiness-bar").css('width', graphData['avgs']['averageHappiness']*100+'%');
    $("#sadness-bar").css('width', graphData['avgs']['averageSadness']*100+'%');
    $("#contempt-bar").css('width', graphData['avgs']['averageContempt']*100+'%');
    $("#disgust-bar").css('width', graphData['avgs']['averageDisgust']*100+'%');
    $("#anger-bar").css('width', graphData['avgs']['averageAnger']*100+'%');
    $("#surprise-bar").css('width', graphData['avgs']['averageSurprise']*100+'%');
    $("#fear-bar").css('width', graphData['avgs']['averageFear']*100+'%');
    $("#neutral-bar").css('width', graphData['avgs']['averageNeutral']*100+'%');
    $(".happiness-percent").text(parseFloat(graphData['avgs']['averageHappiness']*100).toFixed(2)+'%');
    $(".sadness-percent").text(parseFloat(graphData['avgs']['averageSadness']*100).toFixed(2)+'%');
    $(".contempt-percent").text(parseFloat(graphData['avgs']['averageContempt']*100).toFixed(2)+'%');
    $(".disgust-percent").text(parseFloat(graphData['avgs']['averageDisgust']*100).toFixed(2)+'%');
    $(".anger-percent").text(parseFloat(graphData['avgs']['averageAnger']*100).toFixed(2)+'%');
    $(".surprise-percent").text(parseFloat(graphData['avgs']['averageSurprise']*100).toFixed(2)+'%');
    $(".fear-percent").text(parseFloat(graphData['avgs']['averageFear']*100).toFixed(2)+'%');
    $(".neutral-percent").text(parseFloat(graphData['avgs']['averageNeutral']*100).toFixed(2)+'%');

    $(".progress .progress-bar").progressbar();
  },
  videoPlot = function(data) {
    graphData = processData();
    theVideo = $("#video");
    // Create plot after video meta is loaded
    theVideo.on('loadedmetadata', function(event) {
      var theVideo = this,
          duration = theVideo.duration,
          options = {
                     series: {
                         curvedLines: {active: true}
                     },
                     cursors: [
                       {
                         name: 'Player',
                         color: 'red',
                         mode: 'x',
                         showIntersections: false,
                         symbol: 'triangle',
                         showValuesRelativeToSeries: 0,
                         position: {
                           x: 0.0,
                           y: 0.5
                         },
                         snapToPlot: 0
                       }
                     ],
                     xaxis: {
                       min: 0,
                       max: duration
                     },
                     yaxis: {
                       min: 0,
                       max: 1
                     },
                     clickable: false,
                     hoverable: false,
                     grid: {
                     }
                  },
            doPlot = function(sentiment, color, options) {
              // The video tag
              var theVideo = $("#video");
              // Add the created plot for the sentiment to the plots var, to
              // keep reference
              theVideoPlots[sentiment] = $.plot($("#plot-video-" + sentiment), [
                {
                  data: graphData[sentiment],
                  lines: { show: true, lineWidth: 2},
                  curvedLines: {apply: true, tension: 0.5},
                  color: color
                },
                {
                  data: graphData[sentiment],
                  color: '#f03b20',
                  points: {show: true},
                },
              ], options);
              $("#plot-video-" + sentiment).bind("cursorupdates", function(event, cursordata) {
                if(theVideo.get(0).paused) {
                  theVideo.get(0).currentTime = cursordata[0].x;
                  // key phrases
                  var posFrame = pad(Math.floor(cursordata[0].x), 4);
                  if(graphData["speech"][posFrame]) {
                    $("#keyphrases").text(graphData["speech"][posFrame]["kp"]);
                  }
                }
              });
            };
      doPlot("attention", "orange", options);
      doPlot("happiness", "orange", options);
      doPlot("sadness", "darkblue", options);
      doPlot("anger", "red", options);
      doPlot("surprise", "pink", options);
      doPlot("fear", "purple", options);
      doPlot("contempt", "brown", options);
      doPlot("disgust", "darkgreen", options);
      doPlot("neutral", "lightgray", options);
      $(".video-placeholder").hide();
      $("#plot-video-attention").show();

      // Set interval to track video cursor
      setInterval(function () {
        if(!theVideo.paused) {
          onTrackedVideoFrame(theVideo.currentTime, theVideo.duration);
        }
      }, 50);
    });

  };
  $(".plot-tabs a").click(function(e) {
    $(".video-placeholder").hide();
    $(".plot-tabs a").removeClass("active");
    $("#plot-video-" + $(this).attr("data-tab")).show();
    $(this).addClass("active");
  });
  setAttentionPlot();
  setPlot();
  videoPlot();
});
function onTrackedVideoFrame(currentTime, duration){
  for (var key in theVideoPlots) {
    // skip loop if the property is from prototype
    if (!theVideoPlots.hasOwnProperty(key)) continue;
      theVideoPlots[key].setCursor(theVideoPlots[key].getCursors()[0], {
        position: {
          x: currentTime,
          y: 0.5
        }
      });
      var posFrame = pad(Math.floor(currentTime), 4);
      if(graphData["speech"][posFrame]) {
        $("#keyphrases").text(graphData["speech"][posFrame]["kp"]);
      }
      theVideoPlots[key].draw();
    }
}
function pad (str, max) {
  str = str.toString();
  return str.length < max ? pad("0" + str, max) : str;
}
</script>
</body>
</html>

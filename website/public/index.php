<?php
require_once 'header.php';
?>

<style>
.video-container {
  max-width: 600px;
  margin: auto;
}
.demo-placeholder {
    -khtml-user-select: none;
    -o-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
}
#plot-video.demo-placeholder {
  height: 100px;
}
</style>
          <!-- top tiles -->
          <div class="row tile_count">
            <div class="col-md-3 col-sm-4 col-xs-6 tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Max Attentive People</span>
              <div class="count" id="max-attentive">123</div>
            </div>
            <div class="col-md-3 col-sm-4 col-xs-6 tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Min Attention Index</span>
              <div class="count" id="max-attention-index">123</div>
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
                  <div id="plot-chart" class="demo-placeholder"></div>
                </div>
                <div class="col-md-3 col-sm-3 col-xs-12 bg-white">
                  <div class="x_title">
                    <h2>Sentiments</h2>
                    <div class="clearfix"></div>
                  </div>
                  <div class="col-md-12 col-sm-12 col-xs-6">
                    <div>
                      <p>Happiness</p>
                      <div class="">
                        <div class="progress progress_sm">
                          <div class="progress-bar bg-green" role="progressbar" data-transitiongoal="80"></div>
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
                  <video
                      id="video"
                      class="video-active"
                      width="100%"
                      controls="controls">
                      <source src="test.mp4" type="video/mp4">
                  </video>
                </div>
                <div id="plot-video" class="demo-placeholder"></div>
              </div>
            </div>
          </div>
          <br>
<?php
require_once 'footer.php';
?>
<script>
var theVideoPlot;
$(document).ready(function() {
  var processData = function() {
    var d = <?=file_get_contents('test.json')?>;
    var graphData = [];
    for(var i=0; i<d.length; i++) {
      graphData.push([d[i]["frame"], d[i]["attentionIndex"]]);
    }
    return graphData;
  },
  setPlot = function() {
    graphData = processData();
    var options = {
                   series: {
                       curvedLines: {active: true}
                   }
                };
    $.plot($("#plot-chart"), [
      {
        data: graphData,
        lines: { show: true, lineWidth: 2, fill: true},
        curvedLines: {apply: true, tension: 0.5}
      },
      {
        data: graphData, color: '#f03b20',
        points: {show: true}
      }
    ], options);
    $(".progress .progress-bar").progressbar();
  },
  videoPlot = function(data) {
    graphData = processData();
    theVideo = $("#video");
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
                     clickable: false,
                     hoverable: false,
                     grid: {
                     }
                  };
      theVideoPlot = $.plot($("#plot-video"), [
        {
          data: graphData,
          lines: { show: true, lineWidth: 2},
          curvedLines: {apply: true, tension: 0.5}
        },
        {
          data: graphData,
          color: '#f03b20',
          points: {show: true},
        },
      ], options);
      setInterval(function () {
        if(!theVideo.paused) {
          onTrackedVideoFrame(theVideo.currentTime, theVideo.duration); // will get you a lot more updates.
        }
      }, 30);
    });
    $("#plot-video").bind("cursorupdates", function(event, cursordata) {
      if(theVideo.get(0).paused) {
        theVideo.get(0).currentTime = cursordata[0].x;
      }
    });
  };
  setPlot();
  videoPlot();
});
function onTrackedVideoFrame(currentTime, duration){
    $("#current").text(currentTime);
    $("#duration").text(duration);
    theVideoPlot.setCursor(theVideoPlot.getCursors()[0], {
      position: {
        x: currentTime,
        y: 0.5
      }
    });
    theVideoPlot.draw();
}
</script>
</body>
</html>

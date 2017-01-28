<?php
require_once 'header.php';
?>


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
          <br />

<?php
require_once 'footer.php';
?>
<script>
$(document).ready(function() {
  var d = <?=file_get_contents('test.json')?>;
  var setPlot = function(data) {
    var graphData = [];
    for(var i=0; i<data.length; i++) {
      graphData.push([data[i]["frame"], data[i]["attentionIndex"]]);
    }
    var options = {
                   series: {
                       curvedLines: {active: true}
                   }
                };
    $.plot($("#plot-chart"), [
      {
        data: graphData,
        lines: { show: true, lineWidth: 2},
        curvedLines: {apply: true, tension: 0.5}
      },
      {
        data: graphData, color: '#f03b20',
        points: {show: true}
      }
    ], options);
    $(".progress .progress-bar").progressbar();
  };
  setPlot(d);
});
</script>
</body>
</html>

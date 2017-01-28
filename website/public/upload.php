<?php
$page_title = 'Upload';
include 'header.php';
?>
<div class="page-title">
  <div class="title_left">
    <h3>Upload Presentation</h3>
  </div>
</div>
<div class="clearfix"></div>
<div class="row">
  <div class="col-md-12 col-sm-12 col-xs-12">
    <div class="x_panel">
      <div class="x_content">
        <br />
        <?=isset($_GET['success'])&&$_GET['success']?"<span style='color:green'>Success</span>":''?>
        <?=isset($_GET['success'])&&!$_GET['success']?"<span style='color:red'>".urldecode($_GET['msg'])."</span>":''?>
        <form id="upload" data-parsley-validate
          class="form-horizontal form-label-left"
          enctype="multipart/form-data"
          method="POST" action="process.php">
          <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12" for="video">Video <span class="required">*</span>
            </label>
            <div class="col-md-6 col-sm-6 col-xs-12">
              <input type="file" id="video" name="video" required="required" class="form-control col-md-7 col-xs-12">
            </div>
          </div>
          <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12" for="audio">Audio
            </label>
            <div class="col-md-6 col-sm-6 col-xs-12">
              <input type="file" id="audio" name="audio" class="form-control col-md-7 col-xs-12">
            </div>
          </div>
          <div class="ln_solid"></div>
          <div class="form-group">
            <div class="col-md-6 col-sm-6 col-xs-12 col-md-offset-3">
              <button class="btn btn-primary" type="button">Cancel</button>
              <button class="btn btn-primary" type="reset">Reset</button>
              <button type="submit" class="btn btn-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
<?php
include 'footer.php';
?>
</body>
</html>

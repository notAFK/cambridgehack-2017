<?php
require_once '../inc/functions.php';

try {
  if(!$_FILES['video']['size'] > 10) {
    throw new Exception("Video file is mandatory", 1);
  }

  $uploadsDir = "presentations/";
  if(!file_exists($uploadsDir)) {
    if(!mkdir($uploadsDir)) {
      throw new Exception("Error creating presentations directory.", 1);
    }
  }
  // Remove extension
  $presentationName = explode('.', $_FILES['video']['name']);
  array_pop($presentationName);
  $presentationName = implode('.', $presentationName);
  // Check if folder exists for the presentation
  $presentationName = slugify($presentationName);

  if(file_exists($uploadsDir . '/' . $presentationName)) {
    $increment = 1;
    while(file_exists($uploadsDir . '/' . $presentationName . $increment)) {
      $increment ++;
    }
    $presentationName .= $increment;
  }
  // Make folder
  $uploadsDir .= $presentationName;
  if(!mkdir($uploadsDir)) {
    throw new Exception("Error creating folder with name " . $uploadsDir, 1);
  }
  $target_file = $uploadsDir . '/' . basename($_FILES['video']['name']);
  // Upload video there
  // Check if file already exists
  if (file_exists($target_file)) {
    throw new Exception("Sorry, file already exists.", 1);
  }
  if (!move_uploaded_file($_FILES["video"]["tmp_name"], $target_file)) {
    throw new Exception("The file could not be uploaded: " . $_FILES['video']['error'], 1);
  }

  // Upload audio
  if($_FILES['audio']['size'] > 10) {
    $target_file = $uploadsDir . '/audio-' . basename($_FILES['audio']['name']);
    // Check if file already exists
    if (file_exists($target_file)) {
      throw new Exception("Sorry, file already exists.", 1);
    }
    if (!move_uploaded_file($_FILES["audio"]["tmp_name"], $target_file)) {
      throw new Exception("The file could not be uploaded: " . $_FILES['audio']['error'], 1);
    }
  }

  if(!$shell_exec(PY_COMMAND . ' ' . '../../src/video_splitter.py ' . realpath($target_file))) {
    throw new Exception("Error executing splitter", 1);
  }
  if(!$shell_exec(PY_COMMAND . ' ' . '../../src/indexer.py')) {
    throw new Exception("Error executing summary", 1);
  }
  if(!$shell_exec(PY_COMMAND . ' ' . '../../src/analysis.py results.json')) {
    throw new Exception("Error executing summary", 1);
  }
  header('Location: ./index.php?file=results.json');
  exit();
} catch(Exception $e) {
  header('Location: ./upload.php?success=0&msg='.urlencode($e->getMessage()));
  exit();
}
?>

<?php

  require_once "config.php";

  if(isset($_GET["id"])) {
    $id = $_GET["id"];
    $result = mysqli_query($link, "SELECT * FROM mails WHERE id = '$id'");
    if (!$result) {
      echo 'Could not run query: ' . mysqli_error($link);
      exit;
    }
    $item = mysqli_fetch_object($result);
  } else {
    header("location index.php");
    exit;
  }

?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Preview Mail #<?php echo $id;?></title>
    <title>Add Mail</title>
    <link rel="stylesheet" type="text/css" href="Data/include/bootstrap/css/bootstrap.min.css?v=<?php echo time();?>"/>
    <script>window.jQuery || document.write('<script src="Data/include/jquery/jquery.slim.min.js"><\/script>')</script>
    <script src="Data/include/jquery/jquery-3.5.1.min.js"></script>
    <script src="Data/include/jquery/jquery-3.5.0.js"></script>
    <script src="Data/include/bootstrap/js/bootstrap.bundle.min.js"></script>
    <script src="Data/include/bootstrap/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="Data/style.css?v=<?php echo time(); ?>">
  </head>
  <body>
    <div id="content">
      <div id="mail-preview">
        <h1>Preview Mail #<?php echo $id;?></h1>
        <a class="btn btn-primary" href="mail-edit.php?id=<?php echo $id;?>">Edit</a>
        <h2>Title: <?php echo $item->title?></h2>
        <h4>Datetime: <?php echo $item->post_datetime?></h4>
        <h4>Data 1: <?php echo $item->data_1?></h4>
        <h4>Data 2: <?php echo $item->data_2?></h4>
        <h4>Data 3: <?php echo $item->data_3?></h4>
        <h4>Data 4: <?php echo $item->data_4?></h4>
        <h4>Data 5: <?php echo $item->data_5?></h4>
        <h4>Data 6: <?php echo $item->data_6?></h4>
      </div>
    </div>
  </body>
</html>
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
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <link rel="stylesheet" href="style.css?v=<?php echo time(); ?>">
  </head>
  <body>
    <div id="content">
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
  </body>
</html>
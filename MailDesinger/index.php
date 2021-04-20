<?php
  require_once "config.php";
  $items = mysqli_query($link, "SELECT * FROM `mails` ORDER BY `mails`.`post_datetime` DESC");
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Mail Desinger</title>
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
      <h1>Your Mails</h1>
      <div id="mails-navigation">
        <input type="text" value="">
        <button class="btn btn-primary">Search</button>
        <a id="add-btn" class="btn btn-primary" href="mail-add.php">Add</a>
      </div>
      <div id="mails-items">
        <?php
          foreach($items as $item):
         ?>
        <div class="mail-item" onclick="window.location.href = 'mail-preview.php?id=<?php echo $item['id']?>';">
          <h3><?php echo $item["firstname"]." ".$item["lastname"]?></h3>
          <h4><?php echo $item["job"]?></h4>
          <p><?php echo $item["c_profile"]?></p>
          <h5><?php echo $item["post_datetime"]?></h5>
        </div>
        <?php 
          endforeach;
        ?>
      </div>
    </div>
  </body>
</html>
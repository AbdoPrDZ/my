<?php
  require_once "config.php";
  $items = mysqli_query($link, "SELECT * FROM `mails` ORDER BY `mails`.`post_datetime` DESC");
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Mail Desinger</title>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <link rel="stylesheet" href="style.css?v=<?php echo time(); ?>">
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
          <h3><?php echo $item["title"]?></h3>
          <h5><?php echo $item["post_datetime"]?></h5>
        </div>
        <?php 
          endforeach;
        ?>
      </div>
    </div>
  </body>
</html>
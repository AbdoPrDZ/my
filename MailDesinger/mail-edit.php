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
  } elseif(isset($_POST["mail-edit"])) {
    if(!empty($_POST["edit-mail-title"]) && 
        !empty($_POST["edit-mail-data-1"]) && 
        !empty($_POST["edit-mail-data-2"]) && 
        !empty($_POST["edit-mail-data-3"]) && 
        !empty($_POST["edit-mail-data-4"]) && 
        !empty($_POST["edit-mail-data-5"]) && 
        !empty($_POST["edit-mail-data-6"])) {
      $sql = "UPDATE `mails-desinger`.`mails` SET 
        title='".$_POST['edit-mail-title']."',
        data_1='".$_POST['edit-mail-data-1']."',
        data_2='".$_POST['edit-mail-data-2']."',
        data_3='".$_POST['edit-mail-data-3']."',
        data_4='".$_POST['edit-mail-data-4']."',
        data_5='".$_POST['edit-mail-data-5']."',
        data_6='".$_POST['edit-mail-data-6']."'
      WHERE id ='".$_POST['edit-mail-id']."';";
      if(mysqli_query($link, $sql)){
        echo "successfully editing mail";
        header("location: index.php");
      } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
      }
    } else {
      echo 'please fill all data';
      exit;
    }
  } else {
    header("location: index.php");
    exit;
  }

?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Edit Mail #<?php echo $id?></title>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <link rel="stylesheet" href="style.css?v=<?php echo time(); ?>">
  </head>
  <body>
    <form id="content" action="mail-edit.php" method="post" name="mail-edit">
      <h1>Edit Mail #<?php echo $id?></h1>
      <input name="edit-mail-id" class="form-control" style="display: none;" type="text"  value="<?php echo $item->id?>"/>
      <input name="edit-mail-title" class="form-control" type="text" placeholder="Title" value="<?php echo $item->title?>"/>
      <input name="edit-mail-data-1" class="form-control" type="text" placeholder="data 1" value="<?php echo $item->data_1?>"/>
      <input name="edit-mail-data-2" class="form-control" type="text" placeholder="data 2" value="<?php echo $item->data_2?>"/>
      <input name="edit-mail-data-3" class="form-control" type="text" placeholder="data 3" value="<?php echo $item->data_3?>"/>
      <input name="edit-mail-data-4" class="form-control" type="text" placeholder="data 4" value="<?php echo $item->data_4?>"/>
      <input name="edit-mail-data-5" class="form-control" type="text" placeholder="data 5" value="<?php echo $item->data_5?>"/>
      <input name="edit-mail-data-6" class="form-control" type="text" placeholder="data 6" value="<?php echo $item->data_6?>"/>
      <input class="btn btn-primary" type="submit" name="mail-edit" value="Edit"/>
    </form>
  </body>
</html>
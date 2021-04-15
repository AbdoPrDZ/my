<?php
  require_once "config.php";

  if(isset($_POST["mail-add"])) {

    if(!empty($_POST["add-mail-title"]) && 
        !empty($_POST["add-mail-data-1"]) && 
        !empty($_POST["add-mail-data-2"]) && 
        !empty($_POST["add-mail-data-3"]) && 
        !empty($_POST["add-mail-data-4"]) && 
        !empty($_POST["add-mail-data-5"]) && 
        !empty($_POST["add-mail-data-6"])) {
      $sql = "INSERT INTO `mails-desinger`.`mails` (
        title, data_1, data_2, data_3, data_4, data_5, data_6
      ) VALUES (
        '".$_POST['add-mail-title']."',
        '".$_POST['add-mail-data-1']."',
        '".$_POST['add-mail-data-2']."',
        '".$_POST['add-mail-data-3']."',
        '".$_POST['add-mail-data-4']."',
        '".$_POST['add-mail-data-5']."',
        '".$_POST['add-mail-data-6']."'
      );";
      if(mysqli_query($link, $sql)){
        echo "successfully adding mail";
        header("location: index.php");
      } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
      }
    } else {
      echo 'please fill all data';
    }
  }

?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Add Mail</title>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <link rel="stylesheet" href="style.css?v=<?php echo time(); ?>">
  </head>
  <body>
    <form id="content" action="mail-add.php" method="post" name="mail-add">
      <h1>Add Mail</h1>
      <input name="add-mail-title" class="form-control" type="text" placeholder="Title"/>
      <input name="add-mail-data-1" class="form-control" type="text" placeholder="data 1"/>
      <input name="add-mail-data-2" class="form-control" type="text" placeholder="data 2"/>
      <input name="add-mail-data-3" class="form-control" type="text" placeholder="data 3"/>
      <input name="add-mail-data-4" class="form-control" type="text" placeholder="data 4"/>
      <input name="add-mail-data-5" class="form-control" type="text" placeholder="data 5"/>
      <input name="add-mail-data-6" class="form-control" type="text" placeholder="data 6"/>
      <input class="btn btn-primary" type="submit" name="mail-add" value="Add"/>
    </form>
  </body>
</html>
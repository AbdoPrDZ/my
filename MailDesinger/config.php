<?php
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'mails-desinger');

$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

if($link === false) {
  $link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD);
  $sql = "CREATE DATABASE IF NOT EXISTS `".DB_NAME."`;
          CREATE TABLE IF NOT EXISTS `".DB_NAME."`.`mails` (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            c_profile VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            job VARCHAR(255) NOT NULL,
            skils JSON NOT NULL,
            technicals JSON NOT NULL,
            experiences JSON NOT NULL,
            education VARCHAR(255) NOT NULL,
            post_datetime DATETIME DEFAULT CURRENT_TIMESTAMP
          );";
  if(mysqli_query($link, $sql)){
    $link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
  } else{
    die("ERROR: Could not able to execute <br>$sql<br>. " . mysqli_error($link));
  }
  die("ERROR: Could not connect. " . mysqli_connect_error());
}
?>
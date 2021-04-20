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
<html>
	<head>
    <title>Preview Mail #<?php echo $id;?></title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Add Mail</title>
    <link rel="stylesheet" type="text/css" href="Data/include/bootstrap/css/bootstrap.min.css?v=<?php echo time();?>"/>
    <script src="Data/include/jquery/jquery-3.5.1.min.js"></script>
    <script src="Data/include/jquery/jquery-3.5.0.js"></script>
    <link rel="stylesheet" href="Data/style.css?v=<?php echo time(); ?>">
	</head>
	<body>
    <div id="content">
      <div id="mail-content" class="yui-t7" style="margin: 15px 5px; margin-bottom: 2em; padding-bottom: 2em;">
        <div id="inner" style="padding: 10px 80px;
                               background: #f5f5f5;
                               border: solid #666;
                               border-width: 8px 0 2px 0;">
          <div id="hd" style="margin: 2.5em 0 3em 0;
                              padding-bottom: 1.5em;
                              border-bottom: 1px solid #ccc">
            <div class="yui-gc">
              <div class="yui-u first" style="width: 12.3%;">
                <h1 style="color: #333;
                           font-size: 48px;
                           text-transform: uppercase;
                           letter-spacing: 3px;">
                  <?php echo $item->firstname." ".$item->lastname;?>
                </h1>
                <h2 style="color: #333; 
                           font-size: 152%;
                           text-transform: uppercase;
                           letter-spacing: 2px;
                           font-style: italic;">
                  <?php echo $item->job;?>
                </h2>
              </div>
              <div class="yui-u" style="width: 80.2%;">
                <div class="contact-info" style="margin-top: 7px;">
                  <h3 style="color: #333; font-size: 122%;"><a style="color: #990003" href="mailto:<?php echo $item->email;?>"><?php echo $item->email;?></a></h3>
                  <h3 style="color: #333; font-size: 122%;"><a style="color: #990003" href="call:<?php echo $item->phone;?>"><?php echo $item->phone;?></a></h3>
                </div>
                <!--// .contact-info -->
              </div>
            </div>
            <!--// .yui-gc -->
          </div>
          <!--// hd -->
          <div id="bd" style="margin-bottom: 2em;">
            <div id="yui-main">
              <div class="yui-b">
                <div class="yui-gf" style="margin-bottom: 2em; padding-bottom: 2em;">
                  <div class="yui-u first" style="width: 12.3%;">
                    <h2 style="color: #333; font-size: 152%; font-style: italic;">Profile</h2>
                  </div>
                  <div class="yui-u" style="width: 80.2%;">
                    <p style="font-size: 100%;
                              line-height: 18px;
                              padding-right: 3em;"
                       class="enlarge"><?php echo $item->c_profile;?></p>
                  </div>
                </div>
                <!--// .yui-gf -->	
                <div class="yui-gf" style="margin-bottom: 2em; padding-bottom: 2em;">
                  <div class="yui-u first" style="width: 12.3%;">
                    <h2 style="color: #333; font-size: 152%; font-style: italic;">Skills</h2>
                  </div>
                  <div class="yui-u" style="width: 80.2%;">
                  <?php foreach(json_decode($item->skils) as $skil):?>
                    <div class="talent" style="width: 32%; float: left">
                      <h2 style="color: #333; font-size: 152%; margin-bottom: 6px;"><?php echo $skil[0];?></h2>
                      <p style="font-size: 100%;
                                line-height: 18px;
                                padding-right: 3em;"><?php echo $skil[1];?></p>
                    </div>
                  <?php endforeach;?>
                  </div>
                </div>
                <!--// .yui-gf -->
                <div class="yui-gf" style="margin-bottom: 2em; padding-bottom: 2em;">
                  <div class="yui-u first" style="width: 12.3%;">
                    <h2 style="color: #333; font-size: 152%; font-style: italic;">Technical</h2>
                  </div>
                  <div class="yui-u" style="width: 80.2%;">
                    <ul class="talent" style="width: 32%; float: left">
                    <?php foreach(json_decode($item->technicals) as $technical):?>
                      <li style="line-height: 24px; border-bottom: 1px solid #ccc;">
                        <?php echo $technical;?>
                      </li>
                    <?php endforeach;?>
                    </ul>
                  </div>
                </div>
                <!--// .yui-gf-->
                <div class="yui-gf" style="margin-bottom: 2em; padding-bottom: 2em;">
                  <div class="yui-u first" style="width: 12.3%;">
                    <h2 style="color: #333; font-size: 152%; font-style: italic;">Experience</h2>
                  </div>
                  <!--// .yui-u -->
                  <div class="yui-u" style="width: 80.2%;">
                  <?php foreach(json_decode($item->experiences) as $experience):?>
                    <div class="job" style="position: relative;
                                            margin-bottom: 1em;
                                            padding-bottom: 1em;
                                            border-bottom: 1px solid #ccc;">
                      <h2 style="color: #333; font-size: 152%;"><?php echo $experience[0];?></h2>
                      <h3 style="color: #333; font-size: 122%;"><?php echo $experience[1];?></h3>
                      <h4 style="color: #333;
                                font-size: 122%;
                                position: absolute;
                                top: 0.35em;
                                right: 0"><?php echo $experience[3];?></h4>
                      <p style="font-size: 100%;
                                line-height: 18px;
                                padding-right: 3em;
                                margin: 0.75em 0 3em 0;"><?php echo $experience[2];?></p>
                    </div>
                  <?php endforeach;?>
                  </div>
                  <!--// .yui-u -->
                </div>
                <!--// .yui-gf -->
                <div class="yui-gf last" style="border-bottom: 0; border: none;">
                  <div class="yui-u first" style="width: 12.3%;">
                    <h2 style="color: #333; font-size: 152%; font-style: italic;">Education</h2>
                  </div>
                  <div class="yui-u" style="width: 80.2%;">
                    <h2 style="color: #333; font-size: 152%;"><?php echo $item->education;?></h2>
                  </div>
                </div>
                <!--// .yui-gf -->
              </div>
              <!--// .yui-b -->
            </div>
            <!--// yui-main -->
          </div>
          <!--// bd -->
          <div id="ft" style="margin-bottom: 2em;
                              padding: 1em 0 5em 0;
                              font-size: 92%;
                              border-top: 1px solid #ccc;
                              text-align: center;">
            <p style="margin-bottom: 0;
                      text-align: center;
                      font-size: 100%;
                      line-height: 18px;
                      padding-right: 3em;">
              <?php echo $item->firstname." ".$item->lastname;?> 
              &mdash; <a style="color: #990003" href="mailto:<?php echo $item->email;?>"><?php echo $item->email;?></a> 
              &mdash; <?php echo $item->phone;?>
            </p>
          </div>
          <!--// footer -->
        </div>
        <!-- // inner -->
      </div>
      <!--// doc -->

      <button id="btn-print" class="btn btn-primary" style="margin: 0 auto;">Print</button>
    
    </div>
    <script>
      $('#btn-print').click(function(){
          var win = window.open('', 'Print Mail', 'height=500, width=500');
          win.document.write('<html><body>'+$('#mail-content')[0].outerHTML+'</body></html>');
          win.document.close();
          win.print();
      });
    </script>
	</body>
</html>
<?php
  require_once "config.php";

  if(isset($_POST["mail-add"])) {

    if(!empty($_POST["add-mail-firstname"]) && 
        !empty($_POST["add-mail-lastname"]) && 
        !empty($_POST["add-mail-profile"]) && 
        !empty($_POST["add-mail-email"]) && 
        !empty($_POST["add-mail-phone"]) && 
        !empty($_POST["add-mail-job"]) && 
        !empty($_POST["add-mail-skils"]) &&
        !empty($_POST["add-mail-technicals"]) &&
        !empty($_POST["add-mail-experiences"]) &&
        !empty($_POST["add-mail-education"])) {
      $sql = "INSERT INTO `mails-desinger`.`mails` (
        firstname, lastname, c_profile, email, phone,
        job, skils, technicals, experiences, education
      ) VALUES (
        '".$_POST['add-mail-firstname']."',
        '".$_POST['add-mail-lastname']."',
        '".$_POST['add-mail-profile']."',
        '".$_POST['add-mail-email']."',
        '".$_POST['add-mail-phone']."',
        '".$_POST['add-mail-job']."',
        '".$_POST['add-mail-skils']."',
        '".$_POST['add-mail-technicals']."',
        '".$_POST['add-mail-experiences']."',
        '".$_POST['add-mail-education']."'
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
    <link rel="stylesheet" type="text/css" href="Data/include/bootstrap/css/bootstrap.min.css?v=<?php echo time();?>"/>
    <script>window.jQuery || document.write('<script src="Data/include/jquery/jquery.slim.min.js"><\/script>')</script>
    <script src="Data/include/jquery/jquery-3.5.1.min.js"></script>
    <script src="Data/include/jquery/jquery-3.5.0.js"></script>
    <script src="Data/include/bootstrap/js/bootstrap.bundle.min.js"></script>
    <script src="Data/include/bootstrap/js/bootstrap.min.js"></script>
    <script src="Data/script.js"></script>
    <link rel="stylesheet" href="Data/style.css?v=<?php echo time(); ?>">
  </head>
  <body>
    <div id="my-noty" class="noties bottomright"></div>
    <form id="content" action="mail-add.php" method="post" name="mail-add">
      <h1>Add Mail</h1>
      <input name="add-mail-firstname" class="form-control" type="text" placeholder="Firstname"/>
      <input name="add-mail-lastname" class="form-control" type="text" placeholder="Lastname"/>
      <textarea name="add-mail-profile" class="form-control" placeholder="Profile"></textarea>
      <input name="add-mail-email" class="form-control" type="text" placeholder="Email"/>
      <input name="add-mail-phone" class="form-control" type="text" placeholder="phone"/>
      <input name="add-mail-job" class="form-control" type="text" placeholder="Job"/>
      <input name="add-mail-education" class="form-control" type="text" placeholder="Education"/>
      <div class="form-group" style="padding: 5px;">
        <h4>Skils:</h4>
        <div>
          <input type="text" class="form-control skil"
                  placeholder="Skil" name="skil">
          <textarea class="form-control skil-dec"
                  placeholder="Description" name="skil-dec"></textarea>
          <span class="btn btn-primary" onclick="addSkil($('.skil').val(), $('.skil-dec').val());">
            Add
          </span>
        </div>
        <ul id="skils-items" class="list-group form-control" 
            style="overflow: auto; height: 102px; padding: 0;margin: 5px 0;">
        </ul>
        <h5>Total items: <span class="count-skils"></span></h5>
        <textarea id="add-mail-skils" name="add-mail-skils" class="form-control hide"></textarea>
      </div>
      <script>
        $("#skils-items").sortable();
        $("#skils-items").disableSelection();

        countSkils();

        function addSkil(skil, skil_dec) {
          if(skil != '') {
            if(skil_dec != '') {
              var skils_items = new Array();
              const skils = document.querySelectorAll('#skils-items li #skil');
              for (let i = 0; i <= skils.length - 1; i++) {
                skils_items.push(skils[i].innerHTML);
              }
              if(skils_items.indexOf(skil) === -1) {
                var new_item = '<li class="list-group-item d-flex justify-content-between align-items-center" style="padding: 4px; text-align: left;">'+
                                '<span id="skil" style="width: 55%; overflow-wrap: break-word; padding: 0 5px;">'+skil+'</span>'+
                                '<span style="width: 40%; overflow-wrap: break-word; padding: 0 5px;">'+
                                  '<span id="skil-dec">'+skil_dec+'</span> '+
                                '</span>'+
                                '<button id="remove-item" class="close" onclick="removeSkilItem(this)" style="width: 5%; padding: 0 5px;">'+
                                  '<span aria-hidden="true">&times;</span>'+
                                '</button>'+
                              '</li>';
                $('#skils-items').append(new_item);
                $('.skil').val('');
                $('.skil-dec').val('');
              }else{
                createNoty('The Item already exists', 'danger');
              }
              countSkils();
            }else{
              createNoty('The skil description has been required', 'danger');
            }
          }else{
            createNoty('The skil has been required', 'danger');
          }
        }

        var skils = "";
        function countSkils() {
          var items = new Array();
          var count = $("#skils-items li").length;
          $('.count-skils').html(count);
          const skils_items = document.querySelectorAll('#skil');
          const skils_dec = document.querySelectorAll('#skil-dec');
          for (let i = 0; i <= skils_dec.length - 1; i++) {
            items.push([skils_items[i].innerHTML, skils_dec[i].innerHTML]);
          }
          skils = JSON.stringify(items);
          $('#add-mail-skils').html(skils);
        }

        function clear_skils() {
          items = document.querySelectorAll('#remove-item');
          for(i in items) {
            removeSkilItem(items[i]);
          }
        }

        function removeSkilItem(element) {
          $(element).parent().remove();
          countSkils();
        }
      </script>

      <div class="form-group" style="padding: 5px;">
        <h4>Technicals:</h4>
        <div>
          <input type="text" class="form-control technical"
                  placeholder="Technical" name="technical">
          <span class="btn btn-primary" onclick="addTechnical($('.technical').val());">
            Add
          </span>
        </div>
        <ul id="technicals-items" class="list-group form-control" 
            style="overflow: auto; height: 102px; padding: 0;margin: 5px 0;">
        </ul>
        <h5>Total items: <span class="count-technicals"></span></h5>
        <textarea id="add-mail-technicals" name="add-mail-technicals" class="form-control hide"></textarea>
      </div>
      <script>
        $("#technicals-items").sortable();
        $("#technicals-items").disableSelection();

        countTechnicals();

        function addTechnical(technical) {
          if(technical != '') {
            var technicals_items = new Array();
            const technicals = document.querySelectorAll('#technicals-items li #technical');
            for (let i = 0; i <= technicals.length - 1; i++) {
              technicals_items.push(technicals[i].innerHTML);
            }
            if(technicals_items.indexOf(technical) === -1) {
              var new_item = '<li class="list-group-item d-flex justify-content-between align-items-center" style="padding: 4px; text-align: left;">'+
                              '<span id="technical" style="width: 55%; overflow-wrap: break-word; padding: 0 5px;">'+technical+'</span>'+
                              '<button id="remove-item" class="close" onclick="removeTechnicalsItem(this)" style="width: 5%; padding: 0 5px;">'+
                                '<span aria-hidden="true">&times;</span>'+
                              '</button>'+
                            '</li>';
              $('#technicals-items').append(new_item);
              $('.technical').val('');
            }else{
              createNoty('The Item already exists', 'danger');
            }
            countTechnicals();
          }else{
            createNoty('The technical has been required', 'danger');
          }
        }

        var technicals = "";
        function countTechnicals() {
          var items = new Array();
          var count = $("#technicals-items li").length;
          $('.count-technicals').html(count);
          const technicals_items = document.querySelectorAll('#technical');
          for (let i = 0; i <= technicals_items.length - 1; i++) {
            items.push(technicals_items[i].innerHTML);
          }
          technicals = JSON.stringify(items);
          $('#add-mail-technicals').html(technicals);
        }

        function clear_technicals() {
          items = document.querySelectorAll('#remove-item');
          for(i in items) {
            removeTechnicalItem(items[i]);
          }
        }

        function removeTechnicalItem(element) {
          $(element).parent().remove();
          countTechnicals();
        }
      </script>

      <div class="form-group" style="padding: 5px;">
        <h4>Experience:</h4>
        <div>
          <input type="text" class="form-control experience-company"
                  placeholder="Company" name="company"/>
          <input type="text" class="form-control experience-job"
                  placeholder="Job" name="job"/>
          <textarea class="form-control experience-dec"
                    placeholder="Description" name="experience-dec"></textarea>
          <input type="date" class="form-control experience-date"
                  placeholder="Date" name="date"/>
          <span class="btn btn-primary"
           onclick="addExperience($('.experience-company').val(), $('.experience-job').val(), $('.experience-dec').val(), $('.experience-date').val());">
            Add
          </span>
        </div>
        <ul id="experiences-items" class="list-group form-control" 
            style="overflow: auto; height: 102px; padding: 0;margin: 5px 0;">
        </ul>
        <h5>Total items: <span class="count-experiences"></span></h5>
        <textarea id="add-mail-experiences" name="add-mail-experiences" class="form-control hide"></textarea>
      </div>
      <script>
        $("#experiences-items").sortable();
        $("#experiences-items").disableSelection();

        countExperiences();

        function addExperience(experience_company, experience_job, experience_dec, experience_date) {
          if(experience_company != '' && experience_job != '' &&
             experience_dec != '' && experience_date != '') {
            var experiences_items = new Array();
            const experiences_company = document.querySelectorAll('#experiences-items li #experience-company');
            const experiences_job = document.querySelectorAll('#experiences-items li #experience-job');
            const experiences_dec = document.querySelectorAll('#experiences-items li #experience-dec');
            const experiences_date = document.querySelectorAll('#experiences-items li #experience-date');
            for (let i = 0; i <= experiences_company.length - 1; i++) {
              experiences_items.push([experiences_company[i].innerHTML, experiences_job[i].innerHTML,
                                      experiences_dec[i].innerHTML, experiences_date[i].innerHTML]);
            }
            if(experiences_items.indexOf([experience_company, experience_job, experience_dec, experience_date]) === -1) {
              var new_item = '<li class="list-group-item d-flex justify-content-between align-items-center" style="padding: 4px; text-align: left;">'+
                              '<span id="experience-company" style="width: 55%; overflow-wrap: break-word; padding: 0 5px;">'+experience_company+'</span>'+
                              '<span id="experience-job" style="width: 55%; overflow-wrap: break-word; padding: 0 5px;">'+experience_job+'</span>'+
                              '<span id="experience-dec" style="width: 55%; overflow-wrap: break-word; padding: 0 5px;">'+experience_dec+'</span>'+
                              '<span id="experience-date" style="width: 55%; overflow-wrap: break-word; padding: 0 5px;">'+experience_date+'</span>'+
                              '<button id="remove-item" class="close" onclick="removeExperienceItem(this)" style="width: 5%; padding: 0 5px;">'+
                                '<span aria-hidden="true">&times;</span>'+
                              '</button>'+
                            '</li>';
              $('#experiences-items').append(new_item);
              $('.experience-company').val('');
              $('.experience-job').val('');
              $('.experience-dec').val('');
              $('.experience-date').val('');
            }else{
              createNoty('The Item already exists', 'danger');
            }
            countExperiences();
          }else{
            createNoty('All data has been required', 'danger');
          }
        }

        var experiences = "";
        function countExperiences() {
          var items = new Array();
          var count = $("#experiences-items li").length;
          $('.count-experiences').html(count);
          var items = new Array();
          const experiences_company = document.querySelectorAll('#experiences-items li #experience-company');
          const experiences_job = document.querySelectorAll('#experiences-items li #experience-job');
          const experiences_dec = document.querySelectorAll('#experiences-items li #experience-dec');
          const experiences_date = document.querySelectorAll('#experiences-items li #experience-date');
          for (let i = 0; i <= experiences_company.length - 1; i++) {
            items.push([experiences_company[i].innerHTML, experiences_job[i].innerHTML,
                        experiences_dec[i].innerHTML, experiences_date[i].innerHTML]);
          }
          experiences = JSON.stringify(items);
          $('#add-mail-experiences').html(experiences);
        }

        function clear_experiences() {
          items = document.querySelectorAll('#remove-item');
          for(i in items) {
            removeExperienceItem(items[i]);
          }
        }

        function removeExperienceItem(element) {
          $(element).parent().remove();
          countExperiences();
        }
      </script>

      <input class="form-control btn btn-primary" type="submit" name="mail-add" value="Add"/>
    </form>
  </body>
</html>
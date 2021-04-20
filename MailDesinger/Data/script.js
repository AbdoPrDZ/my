var _GET = {};
if(document.location.toString().indexOf('?') !== -1) {
  var query = document.location.toString()
                // get the query string
                .replace(/^.*?\?/, '')
                // and remove any existing hash string (thanks, @vrijdenker)
                .replace(/#.*$/, '')
                .split('&');
  for(var i=0, l=query.length; i<l; i++) {
    var aux = decodeURIComponent(query[i]).split('=');
    _GET[aux[0]] = aux[1];
  }
}

function createNoty(message, type) {
  var html = '<div class="alert alert-' + type + ' alert-dismissable page-alert">';    
  html += '<button class="close" aria-hidden="true" onclick="removeNoty(this)">×<span class="sr-only">Close</span></button>';
  html += message;
  html += '</div>';    
  $(html).hide().prependTo('#my-noty').slideDown();
};

function removeNoty(element) {
  $(element).closest('.page-alert').slideUp();
}

function get_element(id){
  return document.getElementById(id);
}

function load_page(path){
  var div = document.createElement("div");
  div.className = "modal";
  div.style.display='block';
  div.innerHTML = '<object type="text/html" data="'+path+'" style="width: 100%; height: 100%;"></object>';
  document.body.appendChild(div);
}

function getOffset(el) {
  const rect = el.getBoundingClientRect();
  return {
    left: rect.left + window.scrollX,
    top: rect.top + window.scrollY,
    width: rect.width,
    height: rect.height,
  };
}

function mouseX(evt) {
  if (evt.pageX) {
    return evt.pageX;
  } else if (evt.clientX) {
    return evt.clientX + (document.documentElement.scrollLeft ?
      document.documentElement.scrollLeft :
      document.body.scrollLeft);
  } else {
    return null;
  }
}

function mouseY(evt) {
  if(evt.pageY) {
    return evt.pageY;
  }else if (evt.clientY) {
    return evt.clientY + (document.documentElement.scrollTop ?
      document.documentElement.scrollTop :
      document.body.scrollTop);
  }else {
    return null;
  }
}

class UploadFile {

  constructor(element_id, display_el) {
    this.file = null;
    this.element_id = element_id;
    this.display_el = display_el;
  }

  RenderFile(){
    var file = get_element(this.element_id).files[0];
    if(file.name.indexOf(".png") == -1 &&
       file.name.indexOf(".jpg") == -1 &&
       file.name.indexOf(".jpeg") == -1) {
      createNoty(words['Please select file with .png .jpg extension'], "danger");
      get_element(this.element_id).value = "";
      return
    }
    this.file = file;
    var formdata = new FormData();
    formdata.append("filedata", this.file);
    var ajax = new XMLHttpRequest();
    ajax.upload.addEventListener("progress", this.progressHandler, false);
    ajax.addEventListener("load", this.completeHandler, false);
    ajax.addEventListener("error", this.errorHandler, false);
    ajax.addEventListener("abort", this.abortHandler, false);
    ajax.open("POST", "upload.php");
    ajax.send(formdata);
    ajax._this = this;
  }

  progressHandler(event){
    /*
    var percent = (event.loaded / event.total) * 100;
    get_element("loaded_n_total").innerHTML = "Uploaded "+event.loaded+" bytes of "+event.total;
    get_element("progressBar").value = Math.round(percent);
    get_element("status").innerHTML = Math.round(percent)+"% uploaded... please wait";
    get_element("percent").innerHTML = Math.round(percent)+"%";
    */
  }

  completeHandler(event){/*
    get_element("img-display").src = "uploads/"+ this.file.name;
    // get_element("progressBar").value = 0;*/
    var data = JSON.parse(event.target.responseText);
    if(data[0]){
      createNoty(data[1], "success");
      get_element(this._this.display_el).src = "uploads/"+ this._this.file.name;
    }else {
      createNoty(data[1], "danger");
    }
  }

  errorHandler(event){
    createNoty("Upload Failed", "danger")
  }

  abortHandler(event){
    createNoty("Upload Aborted", "danger")
  }
}
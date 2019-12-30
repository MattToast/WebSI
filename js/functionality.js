function main() {
  // What to execute when script is run
  placeFiles();
  // alert("Done Loading")
}

function scrollPage() {
  // Scroll to Contents
  $('html, body').animate({
    scrollTop: $("#body").offset().top
  }, 500);
}

function placeFiles() {
  // Get to files

  // var fs = require('fs');
  // var files = fs.readdirSync('..');

  for(i = 0; i < 6; i++) {
    var btn = document.createElement("BUTTON");
    btn.innerHTML = "Tests";
    document.getElementById("files").appendChild(btn);
  }
}

window.onload = main;

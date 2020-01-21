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

  // $.ajax({
  //   type: "POST",
  //   url: "../python/files.py",
  //   data: { param: text}
  // }).done(function( o ) {
  //   // do something
  // });

  for(i = 0; i < 6; i++) {
    var div = document.createElement("div");

    var head = document.createElement("p");
    head.innerHTML = "Here is button #" + i + ":";

    var btn = document.createElement("BUTTON");
    btn.innerHTML = "Tests";

    div.appendChild(head);
    div.appendChild(btn); 

    // div.style.float = "left";
    div.style.width = "100%";
    // div.style.height = "200%";

    if((i % 2)) {
      div.style.backgroundColor = "#dddddd";
      // div.style.float = "right";
    }

    document.getElementById("files").appendChild(div);
    // document.getElementById("files").appendChild(btn);
    // document.getElementById("files").appendChild(head);
  }
}

window.onload = main;

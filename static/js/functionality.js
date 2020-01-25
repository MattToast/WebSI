function main() {
  // What to execute when script is run
  placeFiles();
  /// alert(window.location.pathname);
}

function scrollPage() {
  // Scroll to Contents
  $('html, body').animate({
    scrollTop: $("#body").offset().top
  }, 500);
}

function placeFiles() {
  // Get to files
  $.ajax({
    url: "/files",
    type: 'POST',
    success: function (data) {
      alert(data.name);
    }
  });

  // Place Buttons for files
  var table = document.getElementById("files_table");
  for (i = 0; i < 5; i++) {
    var row = table.insertRow(1 + i);
    row.insertCell(0).innerHTML = "<p>// TODO: File Name</p>";
    row.insertCell(1).innerHTML = "<p>// TODO: Download</p>";
  }


}

$(document).ready(main);

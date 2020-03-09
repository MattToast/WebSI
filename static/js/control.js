function placeFiles() {
    // Get to files
    $.ajax({
        url: "/files",
        type: 'POST',
        success: function (data) {
            // Place Buttons for files
            for (i = 0; i < data.files.length; i++) {
                var fileName = document.createElement('p').innerHTML = data.files[i] + "\n";
                document.getElementById('list').append(fileName);
            }
        }
    });
}
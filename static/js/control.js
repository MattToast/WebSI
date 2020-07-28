function placeFiles() {
    // Get to files
    $.ajax({
        url: "/files",
        type: 'POST',
        success: function (data) {
            // On success list files
            var list = document.getElementById('list');
            for (i = 0; i < data.files.length; i++) {
                var fileName = document.createElement('li');
                fileName.appendChild(document.createTextNode(data.files[i]));
                list.appendChild(fileName);
            }
        }
    });
}

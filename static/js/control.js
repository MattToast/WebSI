function placeFiles() {
    // Get to files
    $.ajax({
        url: "/files",
        type: 'POST',
        success: function (data) {
            // On success list files
            var removableList = document.getElementById('removablelist');
            for (i = 0; i < data.files.length; i++) {
                var checkbox = document.createElement('input');
                checkbox.type = "checkbox";
                checkbox.name = "filename";
                checkbox.value = data.files[i];
                checkbox.id = data.files[i];

                var label = document.createElement('label');
                label.htmlFor = data.files[i];
                label.appendChild(document.createTextNode(data.files[i]));

                removableList.appendChild(checkbox);
                removableList.appendChild(label);
                removableList.appendChild(document.createElement('br'));

            }
        }
    });
}

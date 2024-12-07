var editor_counter = 0,
    used_ids = [];

function update_editor_display() {
    var counter = 1;
    const node = document.getElementById("editors");
}

function update_editor_counter() {
    const tci = document.getElementById('track_counter_index'),
        tcitb = document.getElementById('track_counter_index_to_be'),
        tcip = document.getElementById('track_counter_index_plural');
    if (editor_counter === 1) {
        tci.innerHTML = editor_counter;
        tcitb.innerHTML = "is";
        tcip.innerHTML = "";
    } else {
        tci.innerHTML = editor_counter;
        tcitb.innerHTML = "are";
        tcip.innerHTML = "s";
    }
    update_editor_display();
}

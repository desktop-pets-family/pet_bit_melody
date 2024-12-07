var MUSIC_LENGTH = 20;
function set_music_length(ID, length = 20) {
    const node = document.getElementById(ID);
    if (node === null || node === undefined) {
        console.error(`Id not found for ${ID}\nAborting function`);
        return;
    }
    node.value = length;
    MUSIC_LENGTH = length;
}
function update_music_length(length_node) {
    const new_value = length_node.value;
    if (new_value === null || new_value === undefined) {
        console.error(`The new value (${new_value}) is not processable.\nAborting function`);
        return;
    }
    MUSIC_LENGTH = new_value;
    update_notes()
}

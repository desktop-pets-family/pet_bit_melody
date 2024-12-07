function delete_track(TRACK_ID) {
    const track_node = document.getElementById(TRACK_ID);
    if (track_node === null || track_node === undefined) {
        console.error("track_node is null or undefined.\nAborting function.");
        return;
    }
    track_node.remove();
    editor_counter--;
    update_editor_counter();
}

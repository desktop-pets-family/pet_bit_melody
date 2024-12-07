function toggle_menu_button_state(ID) {
    reset_clicked_buttons()
    document.getElementById(ID).classList.toggle('active');
    set_current_mode_to_localstorage(EDIT_MODE_NODE, ID)
}
function set_current_mode_to_localstorage(node, mode) {
    localStorage.setItem(node, mode);
}
function delete_current_node_from_localstorage(node) {
    localStorage.removeItem(node);
}
function get_current_mode_from_localstorage_if_present(node) {
    return localStorage.getItem(node);
}
function reset_clicked_buttons() {
    for (var i = 0; i < BUTTON_IDS.length; i++) {
        document.getElementById(BUTTON_IDS[i]).classList.remove('active');
    }
}

function initialise_menu_editor() {
    var node = get_current_mode_from_localstorage_if_present(EDIT_MODE_NODE)
    console.log(`node = ${node}`);
    if (node === null || node === undefined) {
        node = "addNote";
    }
    toggle_menu_button_state(node);
}

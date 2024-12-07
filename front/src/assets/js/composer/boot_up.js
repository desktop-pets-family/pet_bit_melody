function boot_up() {
    initialise_menu_editor();
    set_music_length('music_length_toggle', 20)
    add_row('editors');
    add_row('editors');
}
document.addEventListener("DOMContentLoaded", boot_up);

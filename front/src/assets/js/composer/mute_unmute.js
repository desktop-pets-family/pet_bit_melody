const HIDE_CLASS_KEY = "visually-hidden";

function toggle_line_status(button_node) {
    const data_sound_node_key = "data-sound-on";
    const sound_on = button_node.getAttribute(data_sound_node_key) === DATA_TRUE_KEY;
    const volume_up_icon = button_node.querySelector(".fa-volume-up");
    const volume_mute_icon = button_node.querySelector(".fa-volume-mute");
    button_node.setAttribute(data_sound_node_key, !sound_on);
    volume_up_icon.classList.toggle(HIDE_CLASS_KEY, sound_on);
    volume_mute_icon.classList.toggle(HIDE_CLASS_KEY, !sound_on);
}

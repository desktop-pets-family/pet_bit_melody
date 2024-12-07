const DATA_NOTE_ACTIVE_KEY = "data-note-active"
const DATA_NOTE_MUTED_KEY = "data-note-muted"
const DATA_NOTE_NAME_KEY = "data-note-name"
const NOTE_TOOL_COLOUR_CORRESPONDANCE = {
    "addNote": "note_active",
    "deleteNote": "note_idle",
    "muteNote": "note_muted"
};

function clear_note_colour(note_node) {
    note_node.classList.remove(NOTE_TOOL_COLOUR_CORRESPONDANCE[ADD_NOTE]);
    note_node.classList.remove(NOTE_TOOL_COLOUR_CORRESPONDANCE[MUTE_NOTE]);
    note_node.classList.remove(NOTE_TOOL_COLOUR_CORRESPONDANCE[DELETE_NOTE]);
}

function toggle_note_status(note_node) {
    const current_tool = get_current_mode_from_localstorage_if_present(EDIT_MODE_NODE);
    var note_active = note_node.getAttribute(DATA_NOTE_ACTIVE_KEY) === DATA_TRUE_KEY,
        note_muted = note_node.getAttribute(DATA_NOTE_MUTED_KEY) === DATA_TRUE_KEY;

    clear_note_colour(note_node);
    if (current_tool === MUTE_NOTE) {
        if (note_muted === true) {
            note_node.setAttribute(DATA_NOTE_MUTED_KEY, DATA_FALSE_KEY);
            if (note_active === true) {
                note_node.classList.add(NOTE_TOOL_COLOUR_CORRESPONDANCE[ADD_NOTE]);
            } else {
                note_node.classList.add(NOTE_TOOL_COLOUR_CORRESPONDANCE[DELETE_NOTE]);
            }
        } else {
            note_node.classList.add(NOTE_TOOL_COLOUR_CORRESPONDANCE[MUTE_NOTE]);
            note_node.setAttribute(DATA_NOTE_MUTED_KEY, DATA_TRUE_KEY);
        }
    } else if (current_tool === ADD_NOTE) {
        if (note_active === true) {
            note_node.classList.add(NOTE_TOOL_COLOUR_CORRESPONDANCE[DELETE_NOTE]);
            note_node.setAttribute(DATA_NOTE_MUTED_KEY, DATA_FALSE_KEY);
            note_node.setAttribute(DATA_NOTE_ACTIVE_KEY, DATA_FALSE_KEY);
        } else {
            note_node.classList.add(NOTE_TOOL_COLOUR_CORRESPONDANCE[ADD_NOTE]);
            note_node.setAttribute(DATA_NOTE_MUTED_KEY, DATA_FALSE_KEY);
            note_node.setAttribute(DATA_NOTE_ACTIVE_KEY, DATA_TRUE_KEY);
        }
    } else if (current_tool === DELETE_NOTE) {
        note_node.classList.add(NOTE_TOOL_COLOUR_CORRESPONDANCE[DELETE_NOTE]);
        note_node.setAttribute(DATA_NOTE_MUTED_KEY, DATA_FALSE_KEY);
        note_node.setAttribute(DATA_NOTE_ACTIVE_KEY, DATA_FALSE_KEY);
    }
}

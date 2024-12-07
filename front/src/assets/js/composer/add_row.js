function add_row(ID) {
    var content = "";
    var node = document.getElementById(ID);
    if (node === null || node === undefined) {
        console.error(`Undefined id: ${ID}\nAborting function`);
    }
    editor_counter++;
    //for (var index = 0; index < used_ids.length; index++)
    //    const inner_editor_index = ;
    const TRACK_NUMBER = `track_nb_${editor_counter}`,
        NOTE_SECTION = `notes_${editor_counter}`,
        INSTRUMENT_ID = `instrument_selection_${editor_counter}`;
    content += `<section id="${TRACK_NUMBER}" class="track_line">`;
    content += `    <p>${editor_counter}</p>`;
    content += `    <section class="track_line_title">`;
    //content += `        <input list="instruments" id="${INSTRUMENT_ID}" placeholder="Instrument" alias="Instrument of choice" title="Instrument of choice" class="cell_title_instrument_option" onchange="update_notes('${NOTE_SECTION}', '${INSTRUMENT_ID}')">`;
    content += `        <select list="instruments" id="${INSTRUMENT_ID}" placeholder="Instrument" alias="Instrument of choice" title="Instrument of choice" class="cell_title_instrument_option" onchange="update_notes('${NOTE_SECTION}', '${INSTRUMENT_ID}')">`;
    for (var instrument in INSTRUMENT_NOTES) {
        content += `            <option value="${instrument}">${instrument}</option>`;
    }
    content += `</select>`;
    content += `        <button class="cell_title_sound_option" type="button" id="sound" alias="mute/unmute" title="mute/unmute" data-sound-on="true" onclick="toggle_line_status(this)">`;
    content += `            <i class="fas fa-volume-up cell_title_sound_option_icon"></i>`;
    content += `            <i class="fas fa-volume-mute cell_title_sound_option_icon visually-hidden"></i>`;
    content += `        </button>`;
    content += `        <button class="cell_title_track_delete" type="button" alias="delete track" title="delete track" onclick="delete_track('track_nb_${editor_counter}')">`;
    content += `            <i class="fas fa-trash-alt cell_title_track_delete_icon"></i>`;
    content += `        </button>`;
    content += `    </section>`;
    content += `    <section class="track_line_content">`;
    content += `        <aside class="user_notes" id="${NOTE_SECTION}">`;
    content += `        </aside>`;
    content += `    </section>`;
    content += `</section>`;
    update_editor_counter();
    node.innerHTML += content;
    update_notes(`${NOTE_SECTION}`, `${INSTRUMENT_ID}`);
}

const INSTRUMENT_NOTES = {
    "Piano": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P"],
    "8 bit": [],
    "16 bit": [],
    "32 bit": [],
    "Guitar": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P"],
    "Drums": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P"],
    "Cello": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P"]
}
console.log(`INSTRUMENT_NOTES = ${JSON.stringify(INSTRUMENT_NOTES)}`);
function add_notes(ID, name) {
    var content = "";
    const node = document.getElementById(ID);
    if (name in INSTRUMENT_NOTES === false) {
        console.error(`Instrument: ${name} is not present in the available instruments.`);
        return null;
    }
    if (node === null || node === undefined) {
        console.error(`Failed to find the name of the id ${ID}.\nAborting function.`);
        return;
    }
    for (var i = 0; i < INSTRUMENT_NOTES[name].length; i++) {
        content += `            <section class="note_line">`;
        content += `                <aside class="note_name">${INSTRUMENT_NOTES[name][i]}</aside>`;
        content += `                <aside class="note_toggles">`;
        for (var j = 0; j < MUSIC_LENGTH; j++) {
            content += `                    <span class="note_toggle_node" data-note-active="false" data-note-muted="false" data-note-name="${INSTRUMENT_NOTES[name][i]}" onclick="toggle_note_status(this)"></span>`;
        }
        content += `                </aside>`;
        content += `            </section>`;
    }
    node.innerHTML += content;
    set_instrument_notes_dimensions_via_id(ID);
}

function delete_notes(ID) {
    const node = document.getElementById(ID);
    if (node === null || node === undefined) {
        console.error(`Failed to find the name of the id ${ID}.\nAborting function`);
    }
    node.innerHTML = "";
}

function update_notes(ID, ID_name) {
    const instrument = document.getElementById(ID_name);
    if (instrument === null || instrument === undefined) {
        console.error(`Failed to find the name of the id ${ID_name}.\nAborting function.`);
        return;
    }
    delete_notes(ID);
    add_notes(ID, instrument.value);
}
//function place_notes_on_track(ID, notes)
//function update_while_retaining_position()

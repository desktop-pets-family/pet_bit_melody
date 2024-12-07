function set_note_name_width(note_line_node) {
    const noteNames = note_line_node.querySelectorAll('.note_name');
    let maxWidth = 0;

    // Get the provided padding
    const floatPaddingLeft = parseFloat(getComputedStyle(noteNames[0]).getPropertyValue('padding-left'));
    const floatPaddingRight = parseFloat(getComputedStyle(noteNames[0]).getPropertyValue('padding-right'));
    /*const paddingLeft = getComputedStyle(noteNames[0]).getPropertyValue('padding-left'),
    paddingRight = getComputedStyle(noteNames[0]).getPropertyValue('padding-right'),
    paddingTop = getComputedStyle(noteNames[0]).getPropertyValue('padding-top'),
    paddingBottom = getComputedStyle(noteNames[0]).getPropertyValue('padding-bottom');*/

    // Calculate the maximum width
    noteNames.forEach(note => {
        const width = note.scrollWidth;
        if (width > maxWidth) {
            maxWidth = width;
        }
    });

    // Apply the maximum width to all .note_name elements
    noteNames.forEach(note => {
        note.style.width = `${maxWidth + floatPaddingLeft + floatPaddingRight}px`;
        /*note.style.paddingLeft = paddingLeft;
        note.style.paddingRight = paddingRight;
        note.style.paddingTop = paddingTop;
        note.style.paddingBottom = paddingBottom;*/
    });
}

function set_instrument_notes() {
    // Select all containers with class `user_notes`
    const noteContainers = document.querySelectorAll('.user_notes');

    // Apply the width adjustment function for each container
    noteContainers.forEach(container => {
        set_note_name_width(container);
    });
};

function set_instrument_notes_dimensions_via_id(ID) {
    const noteContainer = document.getElementById(ID);
    set_note_name_width(noteContainer);
};

//document.addEventListener("DOMContentLoaded", set_instrument_notes);

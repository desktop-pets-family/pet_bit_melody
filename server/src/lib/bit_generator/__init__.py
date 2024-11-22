"""
    This is the file that will reference the music generators.
"""

from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME

from . import instrument_constants as ICONST
from .the_8_bit_range import NoteEquivalence8bit, Notes8bit
from .generic_generator import Notes

__all__ = [
    "Notes",
    "ICONST",
    "Notes8bit",
    "Notes16bit",
    "Notes24bit",
    "Notes32bit",
    "NotesPiano",
    "NotesHiHat",
    "NotesCello",
    "NotesGuitar",
    "NotesKickDrum",
    "NotesSnareDrum",
    "NotesLowTomDrum",
    "NotesMidTomDrum",
    "NotesHighTomDrum"
]


ICONST.NoteEquivalence8bit = NoteEquivalence8bit


class NotesGuitar(Notes, ICONST.NoteEquivalenceGuitar):
    """
    The class in charge of the guitar notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceGuitar.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceGuitar.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesGuitar"
    )


class NotesKickDrum(Notes, ICONST.NoteEquivalenceKickDrum):
    """
    The class in charge of the kick drum notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceKickDrum.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceKickDrum.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesKickDrum"
    )


class NotesSnareDrum(Notes, ICONST.NoteEquivalenceSnareDrum):
    """
    The class in charge of the snare drum notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceSnareDrum.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceSnareDrum.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesSnareDrum"
    )


class NotesHiHat(Notes, ICONST.NoteEquivalenceHiHat):
    """
    The class in charge of the hi-hat notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceHiHat.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceHiHat.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesHiHat"
    )


class NotesLowTomDrum(Notes, ICONST.NoteEquivalenceLowTomDrum):
    """
    The class in charge of the low tom drum notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceLowTomDrum.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceLowTomDrum.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesLowTomDrum"
    )


class NotesMidTomDrum(Notes, ICONST.NoteEquivalenceMidTomDrum):
    """
    The class in charge of the mid tom drum notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceMidTomDrum.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceMidTomDrum.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesMidTomDrum"
    )


class NotesHighTomDrum(Notes, ICONST.NoteEquivalenceHighTomDrum):
    """
    The class in charge of the high tom drum notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceHighTomDrum.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceHighTomDrum.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesHighTomDrum"
    )


class Notes16bit(Notes, ICONST.NoteEquivalence16bit):
    """
    The class in charge of the 32 bit notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalence16bit.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalence16bit.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="Notes16bit"
    )


class Notes24bit(Notes, ICONST.NoteEquivalence24bit):
    """
    The class in charge of the 32 bit notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalence24bit.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalence24bit.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="Notes24bit"
    )


class Notes32bit(Notes, ICONST.NoteEquivalence32bit):
    """
    The class in charge of the 32 bit notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalence32bit.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalence32bit.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="Notes32bit"
    )


class NotesCello(Notes, ICONST.NoteEquivalenceCello):
    """
    The class in charge of the cello notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalenceCello.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalenceCello.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesCello"
    )


class NotesPiano(Notes, ICONST.NoteEquivalencePiano):
    """
    The class in charge of the piano notes.

    Args:
        Notes (class): The base class for generating notes.
    """
    NOTE_EQUIVALENCE = ICONST.NoteEquivalencePiano.NOTE_EQUIVALENCE
    MUTE = ICONST.NoteEquivalencePiano.MUTE
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=False,
        logger="NotesPiano"
    )

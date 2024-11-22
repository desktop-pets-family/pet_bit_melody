"""
    The file in charge of containing the note equivalence for the instruments.
"""


# --------------------- The note that represents a silence ---------------------
DEFAULT_MUTE: int = 1

# -------------------------- The default sample rate  --------------------------

DEFAULT_SAMPLE_RATE: int = 44100

# ---------------- The default note frequencies to use as base  ----------------
# -1 is used to represent negative notes
DEFAULT_CN1 = 8.18
DEFAULT_CSHN1 = 8.66
DEFAULT_DBN1 = 8.66
DEFAULT_DN1 = 9.18
DEFAULT_DSHN1 = 9.72
DEFAULT_EBN1 = 9.72
DEFAULT_EN1 = 10.30
DEFAULT_FN1 = 10.91
DEFAULT_FSHN1 = 11.56
DEFAULT_GBN1 = 11.56
DEFAULT_GN1 = 12.25
DEFAULT_GSHN1 = 12.98
DEFAULT_ABN1 = 12.98
DEFAULT_AN1 = 13.75
DEFAULT_ASHN1 = 14.57
DEFAULT_BBN1 = 14.57
DEFAULT_BN1 = 15.43

# 0 is used to represent the base note
DEFAULT_C0 = 16.35
DEFAULT_CSH0 = 17.32
DEFAULT_DB0 = 17.32
DEFAULT_D0 = 18.35
DEFAULT_DSH0 = 19.45
DEFAULT_EB0 = 19.45
DEFAULT_E0 = 20.60
DEFAULT_F0 = 21.83
DEFAULT_FSH0 = 23.12
DEFAULT_GB0 = 23.12
DEFAULT_G0 = 24.50
DEFAULT_GSH0 = 25.96
DEFAULT_AB0 = 25.96
DEFAULT_A0 = 27.50
DEFAULT_ASH0 = 29.14
DEFAULT_BB0 = 29.14
DEFAULT_B0 = 30.87

# 1 is used to represent the first octave
DEFAULT_C1 = 32.70
DEFAULT_CSH1 = 34.65
DEFAULT_DB1 = 34.65
DEFAULT_D1 = 36.71
DEFAULT_DSH1 = 38.89
DEFAULT_EB1 = 38.89
DEFAULT_E1 = 41.20
DEFAULT_F1 = 43.65
DEFAULT_FSH1 = 46.25
DEFAULT_GB1 = 46.25
DEFAULT_G1 = 49.00
DEFAULT_GSH1 = 51.91
DEFAULT_AB1 = 51.91
DEFAULT_A1 = 55.00
DEFAULT_ASH1 = 58.27
DEFAULT_BB1 = 58.27
DEFAULT_B1 = 61.74

# 2 is used to represent the second octave
DEFAULT_C2 = 65.41
DEFAULT_CSH2 = 69.30
DEFAULT_DB2 = 69.30
DEFAULT_D2 = 73.42
DEFAULT_DSH2 = 77.78
DEFAULT_EB2 = 77.78
DEFAULT_E2 = 82.41
DEFAULT_F2 = 87.31
DEFAULT_FSH2 = 92.50
DEFAULT_GB2 = 92.50
DEFAULT_G2 = 98.00
DEFAULT_GSH2 = 103.83
DEFAULT_AB2 = 103.83
DEFAULT_A2 = 110.00
DEFAULT_ASH2 = 116.54
DEFAULT_BB2 = 116.54
DEFAULT_B2 = 123.47

# 3 is used to represent the third octave
DEFAULT_C3 = 130.81
DEFAULT_CSH3 = 138.59
DEFAULT_DB3 = 138.59
DEFAULT_D3 = 146.83
DEFAULT_DSH3 = 155.56
DEFAULT_EB3 = 155.56
DEFAULT_E3 = 164.81
DEFAULT_F3 = 174.61
DEFAULT_FSH3 = 185.00
DEFAULT_GB3 = 185.00
DEFAULT_G3 = 196.00
DEFAULT_GSH3 = 207.65
DEFAULT_AB3 = 207.65
DEFAULT_A3 = 220.00
DEFAULT_ASH3 = 233.08
DEFAULT_BB3 = 233.08
DEFAULT_B3 = 246.94

# 4 is used to represent the fourth octave
DEFAULT_C4 = 261.63
DEFAULT_CSH4 = 277.18
DEFAULT_DB4 = 277.18
DEFAULT_D4 = 293.66
DEFAULT_DSH4 = 311.13
DEFAULT_EB4 = 311.13
DEFAULT_E4 = 329.63
DEFAULT_F4 = 349.23
DEFAULT_FSH4 = 369.99
DEFAULT_GB4 = 369.99
DEFAULT_G4 = 392.00
DEFAULT_GSH4 = 415.30
DEFAULT_AB4 = 415.30
DEFAULT_A4 = 440.00
DEFAULT_ASH4 = 466.16
DEFAULT_BB4 = 466.16
DEFAULT_B4 = 493.88

# 5 is used to represent the fifth octave
DEFAULT_C5 = 523.25
DEFAULT_CSH5 = 554.37
DEFAULT_DB5 = 554.37
DEFAULT_D5 = 587.33
DEFAULT_DSH5 = 622.25
DEFAULT_EB5 = 622.25
DEFAULT_E5 = 659.25
DEFAULT_F5 = 698.46
DEFAULT_FSH5 = 739.99
DEFAULT_GB5 = 739.99
DEFAULT_G5 = 783.99
DEFAULT_GSH5 = 830.61
DEFAULT_AB5 = 830.61
DEFAULT_A5 = 880.00
DEFAULT_ASH5 = 932.33
DEFAULT_BB5 = 932.33
DEFAULT_B5 = 987.77

# 6 is used to represent the sixth octave
DEFAULT_C6 = 1046.50
DEFAULT_CSH6 = 1108.73
DEFAULT_DB6 = 1108.73
DEFAULT_D6 = 1174.66
DEFAULT_DSH6 = 1244.51
DEFAULT_EB6 = 1244.51
DEFAULT_E6 = 1318.51
DEFAULT_F6 = 1396.91
DEFAULT_FSH6 = 1479.98
DEFAULT_GB6 = 1479.98
DEFAULT_G6 = 1567.98
DEFAULT_GSH6 = 1661.22
DEFAULT_AB6 = 1661.22
DEFAULT_A6 = 1760.00
DEFAULT_ASH6 = 1864.66
DEFAULT_BB6 = 1864.66
DEFAULT_B6 = 1975.53

# 7 is used to represent the seventh octave
DEFAULT_C7 = 2093.00
DEFAULT_CSH7 = 2217.46
DEFAULT_DB7 = 2217.46
DEFAULT_D7 = 2349.32
DEFAULT_DSH7 = 2489.02
DEFAULT_EB7 = 2489.02
DEFAULT_E7 = 2637.02
DEFAULT_F7 = 2793.83
DEFAULT_FSH7 = 2959.96
DEFAULT_GB7 = 2959.96
DEFAULT_G7 = 3135.96
DEFAULT_GSH7 = 3322.44
DEFAULT_AB7 = 3322.44
DEFAULT_A7 = 3520.00
DEFAULT_ASH7 = 3729.31
DEFAULT_BB7 = 3729.31
DEFAULT_B7 = 3951.07

# 8 is used to represent the eighth octave
DEFAULT_C8 = 4186.01
DEFAULT_CSH8 = 4434.92
DEFAULT_DB8 = 4434.92
DEFAULT_D8 = 4698.63
DEFAULT_DSH8 = 4978.03
DEFAULT_EB8 = 4978.03
DEFAULT_E8 = 5274.04
DEFAULT_F8 = 5587.65
DEFAULT_FSH8 = 5919.91
DEFAULT_GB8 = 5919.91
DEFAULT_G8 = 6271.93
DEFAULT_GSH8 = 6644.88
DEFAULT_AB8 = 6644.88
DEFAULT_A8 = 7040.00
DEFAULT_ASH8 = 7458.62
DEFAULT_BB8 = 7458.62
DEFAULT_B8 = 7902.13

# 9 is used to represent the ninth octave
DEFAULT_C9 = 8372.02
DEFAULT_CSH9 = 8869.84
DEFAULT_DB9 = 8869.84
DEFAULT_D9 = 9397.27
DEFAULT_DSH9 = 9956.06
DEFAULT_EB9 = 9956.06
DEFAULT_E9 = 10548.08
DEFAULT_F9 = 11175.30
DEFAULT_FSH9 = 11839.82
DEFAULT_GB9 = 11839.82
DEFAULT_G9 = 12543.85
DEFAULT_GSH9 = 13289.75
DEFAULT_AB9 = 13289.75
DEFAULT_A9 = 14080.00
DEFAULT_ASH9 = 14917.24
DEFAULT_BB9 = 14917.24
DEFAULT_B9 = 15804.27

# Dictionary of notes
DEFAULT_NOTE_EQUIVALENCE = {
    "MUTE": DEFAULT_MUTE,
    "C": DEFAULT_C4, "C#": DEFAULT_CSH4, "D♭": DEFAULT_DB4, "D": DEFAULT_D4, "D#": DEFAULT_DSH4, "E♭": DEFAULT_EB4, "E": DEFAULT_E4, "F": DEFAULT_F4, "F#": DEFAULT_FSH4, "G♭": DEFAULT_GB4, "G": DEFAULT_G4, "G#": DEFAULT_GSH4, "A♭": DEFAULT_AB4, "A": DEFAULT_A4, "A#": DEFAULT_ASH4, "B♭": DEFAULT_BB4, "B": DEFAULT_B4,
    "C-1": DEFAULT_CN1, "C#-1": DEFAULT_CSHN1, "D♭-1": DEFAULT_DBN1, "D-1": DEFAULT_DN1, "D#-1": DEFAULT_DSHN1, "E♭-1": DEFAULT_EBN1, "E-1": DEFAULT_EN1, "F-1": DEFAULT_FN1, "F#-1": DEFAULT_FSHN1, "G♭-1": DEFAULT_GBN1, "G-1": DEFAULT_GN1, "G#-1": DEFAULT_GSHN1, "A♭-1": DEFAULT_ABN1, "A-1": DEFAULT_AN1, "A#-1": DEFAULT_ASHN1, "B♭-1": DEFAULT_BBN1, "B-1": DEFAULT_BN1,
    "C0": DEFAULT_C0, "C#0": DEFAULT_CSH0, "D♭0": DEFAULT_DB0, "D0": DEFAULT_D0, "D#0": DEFAULT_DSH0, "E♭0": DEFAULT_EB0, "E0": DEFAULT_E0, "F0": DEFAULT_F0, "F#0": DEFAULT_FSH0, "G♭0": DEFAULT_GB0, "G0": DEFAULT_G0, "G#0": DEFAULT_GSH0, "A♭0": DEFAULT_AB0, "A0": DEFAULT_A0, "A#0": DEFAULT_ASH0, "B♭0": DEFAULT_BB0, "B0": DEFAULT_B0,
    "C1": DEFAULT_C1, "C#1": DEFAULT_CSH1, "D♭1": DEFAULT_DB1, "D1": DEFAULT_D1, "D#1": DEFAULT_DSH1, "E♭1": DEFAULT_EB1, "E1": DEFAULT_E1, "F1": DEFAULT_F1, "F#1": DEFAULT_FSH1, "G♭1": DEFAULT_GB1, "G1": DEFAULT_G1, "G#1": DEFAULT_GSH1, "A♭1": DEFAULT_AB1, "A1": DEFAULT_A1, "A#1": DEFAULT_ASH1, "B♭1": DEFAULT_BB1, "B1": DEFAULT_B1,
    "C2": DEFAULT_C2, "C#2": DEFAULT_CSH2, "D♭2": DEFAULT_DB2, "D2": DEFAULT_D2, "D#2": DEFAULT_DSH2, "E♭2": DEFAULT_EB2, "E2": DEFAULT_E2, "F2": DEFAULT_F2, "F#2": DEFAULT_FSH2, "G♭2": DEFAULT_GB2, "G2": DEFAULT_G2, "G#2": DEFAULT_GSH2, "A♭2": DEFAULT_AB2, "A2": DEFAULT_A2, "A#2": DEFAULT_ASH2, "B♭2": DEFAULT_BB2, "B2": DEFAULT_B2,
    "C3": DEFAULT_C3, "C#3": DEFAULT_CSH3, "D♭3": DEFAULT_DB3, "D3": DEFAULT_D3, "D#3": DEFAULT_DSH3, "E♭3": DEFAULT_EB3, "E3": DEFAULT_E3, "F3": DEFAULT_F3, "F#3": DEFAULT_FSH3, "G♭3": DEFAULT_GB3, "G3": DEFAULT_G3, "G#3": DEFAULT_GSH3, "A♭3": DEFAULT_AB3, "A3": DEFAULT_A3, "A#3": DEFAULT_ASH3, "B♭3": DEFAULT_BB3, "B3": DEFAULT_B3,
    "C4": DEFAULT_C4, "C#4": DEFAULT_CSH4, "D♭4": DEFAULT_DB4, "D4": DEFAULT_D4, "D#4": DEFAULT_DSH4, "E♭4": DEFAULT_EB4, "E4": DEFAULT_E4, "F4": DEFAULT_F4, "F#4": DEFAULT_FSH4, "G♭4": DEFAULT_GB4, "G4": DEFAULT_G4, "G#4": DEFAULT_GSH4, "A♭4": DEFAULT_AB4, "A4": DEFAULT_A4, "A#4": DEFAULT_ASH4, "B♭4": DEFAULT_BB4, "B4": DEFAULT_B4,
    "C5": DEFAULT_C5, "C#5": DEFAULT_CSH5, "D♭5": DEFAULT_DB5, "D5": DEFAULT_D5, "D#5": DEFAULT_DSH5, "E♭5": DEFAULT_EB5, "E5": DEFAULT_E5, "F5": DEFAULT_F5, "F#5": DEFAULT_FSH5, "G♭5": DEFAULT_GB5, "G5": DEFAULT_G5, "G#5": DEFAULT_GSH5, "A♭5": DEFAULT_AB5, "A5": DEFAULT_A5, "A#5": DEFAULT_ASH5, "B♭5": DEFAULT_BB5, "B5": DEFAULT_B5,
    "C6": DEFAULT_C6, "C#6": DEFAULT_CSH6, "D♭6": DEFAULT_DB6, "D6": DEFAULT_D6, "D#6": DEFAULT_DSH6, "E♭6": DEFAULT_EB6, "E6": DEFAULT_E6, "F6": DEFAULT_F6, "F#6": DEFAULT_FSH6, "G♭6": DEFAULT_GB6, "G6": DEFAULT_G6, "G#6": DEFAULT_GSH6, "A♭6": DEFAULT_AB6, "A6": DEFAULT_A6, "A#6": DEFAULT_ASH6, "B♭6": DEFAULT_BB6, "B6": DEFAULT_B6,
    "C7": DEFAULT_C7, "C#7": DEFAULT_CSH7, "D♭7": DEFAULT_DB7, "D7": DEFAULT_D7, "D#7": DEFAULT_DSH7, "E♭7": DEFAULT_EB7, "E7": DEFAULT_E7, "F7": DEFAULT_F7, "F#7": DEFAULT_FSH7, "G♭7": DEFAULT_GB7, "G7": DEFAULT_G7, "G#7": DEFAULT_GSH7, "A♭7": DEFAULT_AB7, "A7": DEFAULT_A7, "A#7": DEFAULT_ASH7, "B♭7": DEFAULT_BB7, "B7": DEFAULT_B7,
    "C8": DEFAULT_C8, "C#8": DEFAULT_CSH8, "D♭8": DEFAULT_DB8, "D8": DEFAULT_D8, "D#8": DEFAULT_DSH8, "E♭8": DEFAULT_EB8, "E8": DEFAULT_E8, "F8": DEFAULT_F8, "F#8": DEFAULT_FSH8, "G♭8": DEFAULT_GB8, "G8": DEFAULT_G8, "G#8": DEFAULT_GSH8, "A♭8": DEFAULT_AB8, "A8": DEFAULT_A8, "A#8": DEFAULT_ASH8, "B♭8": DEFAULT_BB8, "B8": DEFAULT_B8,
    "C9": DEFAULT_C9, "C#9": DEFAULT_CSH9, "D♭9": DEFAULT_DB9, "D9": DEFAULT_D9, "D#9": DEFAULT_DSH9, "E♭9": DEFAULT_EB9, "E9": DEFAULT_E9, "F9": DEFAULT_F9, "F#9": DEFAULT_FSH9, "G♭9": DEFAULT_GB9, "G9": DEFAULT_G9, "G#9": DEFAULT_GSH9, "A♭9": DEFAULT_AB9, "A9": DEFAULT_A9, "A#9": DEFAULT_ASH9, "B♭9": DEFAULT_BB9, "B9": DEFAULT_B9
}

# --------------------- Guitar notes and their frequencies ---------------------


class NoteEquivalenceGuitar:
    """
    The class in charge of the guitar notes and their frequencies.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 32767
    # Around 82-330Hz
    # F2 to E4
    # 2 is used to represent the second octave
    F2 = DEFAULT_F2
    FSH2 = DEFAULT_FSH2
    GB2 = DEFAULT_GB2
    G2 = DEFAULT_G2
    GSH2 = DEFAULT_GSH2
    AB2 = DEFAULT_AB2
    A2 = DEFAULT_A2
    ASH2 = DEFAULT_ASH2
    BB2 = DEFAULT_BB2
    B2 = DEFAULT_B2

    # 3 is used to represent the third octave
    C3 = DEFAULT_C3
    CSH3 = DEFAULT_CSH3
    DB3 = DEFAULT_DB3
    D3 = DEFAULT_D3
    DSH3 = DEFAULT_DSH3
    EB3 = DEFAULT_EB3
    E3 = DEFAULT_E3
    F3 = DEFAULT_F3
    FSH3 = DEFAULT_FSH3
    GB3 = DEFAULT_GB3
    G3 = DEFAULT_G3
    GSH3 = DEFAULT_GSH3
    AB3 = DEFAULT_AB3
    A3 = DEFAULT_A3
    ASH3 = DEFAULT_ASH3
    BB3 = DEFAULT_BB3
    B3 = DEFAULT_B3

    # 4 is used to represent the fourth octave
    C4 = DEFAULT_C4
    CSH4 = DEFAULT_CSH4
    DB4 = DEFAULT_DB4
    D4 = DEFAULT_D4
    DSH4 = DEFAULT_DSH4
    EB4 = DEFAULT_EB4
    E4 = DEFAULT_E4
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "F": F2, "F#": FSH2, "G♭": GB2, "G": G2, "G#": GSH2, "A♭": AB2, "A": A2, "A#": ASH2, "B♭": BB2, "B": B2,
        "F2": F2, "F#2": FSH2, "G♭2": GB2, "G2": G2, "G#2": GSH2, "A♭2": AB2, "A2": A2, "A#2": ASH2, "B♭2": BB2, "B2": B2,
        "C3": C3, "C#3": CSH3, "D♭3": DB3, "D3": D3, "D#3": DSH3, "E♭3": EB3, "E3": E3, "F3": F3, "F#3": FSH3, "G♭3": GB3, "G3": G3, "G#3": GSH3, "A♭3": AB3, "A3": A3, "A#3": ASH3, "B♭3": BB3, "B3": B3,
    }

# ---------------------- Drum notes and their frequencies ----------------------


class NoteEquivalenceKickDrum:
    """
    The note equivalence for the Kick drum instrument.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535
    # Around 60-100Hz
    # E1 to G2
    E1 = DEFAULT_E1
    F1 = DEFAULT_F1
    FSH1 = DEFAULT_FSH1
    GB1 = DEFAULT_GB1
    G1 = DEFAULT_G1
    GSH1 = DEFAULT_GSH1
    AB1 = DEFAULT_AB1
    A1 = DEFAULT_A1
    ASH1 = DEFAULT_ASH1
    BB1 = DEFAULT_BB1
    B1 = DEFAULT_B1

    # 2 is used to represent the second octave
    C2 = DEFAULT_C2
    CSH2 = DEFAULT_CSH2
    DB2 = DEFAULT_DB2
    D2 = DEFAULT_D2
    DSH2 = DEFAULT_DSH2
    EB2 = DEFAULT_EB2
    E2 = DEFAULT_E2
    F2 = DEFAULT_F2
    FSH2 = DEFAULT_FSH2
    GB2 = DEFAULT_GB2
    G2 = DEFAULT_G2
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": E1, "C#": F1, "D♭": F1, "D": FSH1, "D#": GB1, "E♭": G1, "E": GSH1, "F": AB1, "F#": A1, "G♭": ASH1, "G": BB1, "G#": B1,
        "E1": E1, "F1": F1, "F#1": FSH1, "G♭1": GB1, "G1": G1, "G#1": GSH1, "A♭1": AB1, "A1": A1, "A#1": ASH1, "B♭1": BB1, "B1": B1,
        "C2": C2, "C#2": CSH2, "D♭2": DB2, "D2": D2, "D#2": DSH2, "E♭2": EB2, "E2": E2, "F2": F2, "F#2": FSH2, "G♭2": GB2, "G2": G2
    }


class NoteEquivalenceSnareDrum:
    """
    The note equivalence for the Snare drum instrument.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535

    # Around 120-250Hz
    # Smaller snare drums (e.g., 10"–12") have a higher fundamental pitch (closer to G3–B3).
    # Standard snare drums(e.g., 14") usually fall around E3–B3.
    # Larger, deeper snares may dip closer to B2–D3.
    # 2 is used to represent the second octave
    B2 = DEFAULT_B2

    # 3 is used to represent the third octave
    C3 = DEFAULT_C3
    CSH3 = DEFAULT_CSH3
    DB3 = DEFAULT_DB3
    D3 = DEFAULT_D3
    DSH3 = DEFAULT_DSH3
    EB3 = DEFAULT_EB3
    E3 = DEFAULT_E3
    F3 = DEFAULT_F3
    FSH3 = DEFAULT_FSH3
    GB3 = DEFAULT_GB3
    G3 = DEFAULT_G3
    GSH3 = DEFAULT_GSH3
    AB3 = DEFAULT_AB3
    A3 = DEFAULT_A3
    ASH3 = DEFAULT_ASH3
    BB3 = DEFAULT_BB3
    B3 = DEFAULT_B3
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": C3, "C#": CSH3, "D♭": DB3, "D": D3, "D#": DSH3, "E♭": EB3, "E": E3, "F": F3, "F#": FSH3, "G♭": GB3, "G": G3, "G#": GSH3, "A♭": AB3, "A": A3, "A#": ASH3, "B♭": BB3, "B": B3,
        "B2": B2,
        "C3": C3, "C#3": CSH3, "D♭3": DB3, "D3": D3, "D#3": DSH3, "E♭3": EB3, "E3": E3, "F3": F3, "F#3": FSH3, "G♭3": GB3, "G3": G3, "G#3": GSH3, "A♭3": AB3, "A3": A3, "A#3": ASH3, "B♭3": BB3, "B3": B3
    }


class NoteEquivalenceHiHat:
    """
    The note equivalence for the HiHat drum instrument.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535

    # Around 250-500Hz
    # C4 to B4
    # 4 is used to represent the fourth octave
    C4 = DEFAULT_C4
    CSH4 = DEFAULT_CSH4
    DB4 = DEFAULT_DB4
    D4 = DEFAULT_D4
    DSH4 = DEFAULT_DSH4
    EB4 = DEFAULT_EB4
    E4 = DEFAULT_E4
    F4 = DEFAULT_F4
    FSH4 = DEFAULT_FSH4
    GB4 = DEFAULT_GB4
    G4 = DEFAULT_G4
    GSH4 = DEFAULT_GSH4
    AB4 = DEFAULT_AB4
    A4 = DEFAULT_A4
    ASH4 = DEFAULT_ASH4
    BB4 = DEFAULT_BB4
    B4 = DEFAULT_B4
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": C4, "C#": CSH4, "D♭": DB4, "D": D4, "D#": DSH4, "E♭": EB4, "E": E4, "F": F4, "F#": FSH4, "G♭": GB4, "G": G4, "G#": GSH4, "A♭": AB4, "A": A4, "A#": ASH4, "B♭": BB4, "B": B4,
        "C4": C4, "C#4": CSH4, "D♭4": DB4, "D4": D4, "D#4": DSH4, "E♭4": EB4, "E4": E4, "F4": F4, "F#4": FSH4, "G♭4": GB4, "G4": G4, "G#4": GSH4, "A♭4": AB4, "A4": A4, "A#4": ASH4, "B♭4": BB4, "B4": B4
    }


class NoteEquivalenceLowTomDrum:
    """
    The note equivalence for the low tom drum instrument.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535
    # Around 80-120Hz
    # E2 to B2
    # 2 is used to represent the second octave
    E2 = DEFAULT_E2
    F2 = DEFAULT_F2
    FSH2 = DEFAULT_FSH2
    GB2 = DEFAULT_GB2
    G2 = DEFAULT_G2
    GSH2 = DEFAULT_GSH2
    AB2 = DEFAULT_AB2
    A2 = DEFAULT_A2
    ASH2 = DEFAULT_ASH2
    BB2 = DEFAULT_BB2
    B2 = DEFAULT_B2
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "E": E2, "F": F2, "F#": FSH2, "G♭": GB2, "G": G2, "G#": GSH2, "A♭": AB2, "A": A2, "A#": ASH2, "B♭": BB2, "B": B2,
        # "E2": E2, "F2": F2, "F#2": FSH2, "G♭2": GB2, "G2": G2, "G#2": GSH2, "A♭2": AB2, "A2": A2, "A#2": ASH2, "B♭2": BB2, "B2": B2
    }


class NoteEquivalenceMidTomDrum:
    """
    The note equivalence for the mid tom drum instrument.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535
    # Around 120-200Hz
    # C3 to A3
    # 3 is used to represent the third octave
    C3 = DEFAULT_C3
    CSH3 = DEFAULT_CSH3
    DB3 = DEFAULT_DB3
    D3 = DEFAULT_D3
    DSH3 = DEFAULT_DSH3
    EB3 = DEFAULT_EB3
    E3 = DEFAULT_E3
    F3 = DEFAULT_F3
    FSH3 = DEFAULT_FSH3
    GB3 = DEFAULT_GB3
    G3 = DEFAULT_G3
    GSH3 = DEFAULT_GSH3
    AB3 = DEFAULT_AB3
    A3 = DEFAULT_A3
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": C3, "C#": CSH3, "D♭": DB3, "D": D3, "D#": DSH3, "E♭": EB3, "E": E3, "F": F3, "F#": FSH3, "G♭": GB3, "G": G3, "G#": GSH3, "A♭": AB3, "A": A3,
        # "C3": C3, "C#3": CSH3, "D♭3": DB3, "D3": D3, "D#3": DSH3, "E♭3": EB3, "E3": E3, "F3": F3, "F#3": FSH3, "G♭3": GB3, "G3": G3, "G#3": GSH3, "A♭3": AB3, "A3": A3
    }


class NoteEquivalenceHighTomDrum:
    """
    The note equivalence for the high tom drum instrument.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535
    # Around 200-400Hz
    # C4 to G4
    # 4 is used to represent the fourth octave
    C4 = DEFAULT_C4
    CSH4 = DEFAULT_CSH4
    DB4 = DEFAULT_DB4
    D4 = DEFAULT_D4
    DSH4 = DEFAULT_DSH4
    EB4 = DEFAULT_EB4
    E4 = DEFAULT_E4
    F4 = DEFAULT_F4
    FSH4 = DEFAULT_FSH4
    GB4 = DEFAULT_GB4
    G4 = DEFAULT_G4
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": C4, "C#": CSH4, "D♭": DB4, "D": D4, "D#": DSH4, "E♭": EB4, "E": E4, "F": F4, "F#": FSH4, "G♭": GB4, "G": G4,
        # "C4": C4, "C#4": CSH4, "D♭4": DB4, "D4": D4, "D#4": DSH4, "E♭4": EB4, "E4": E4, "F4": F4, "F#4": FSH4, "G♭4": GB4, "G4": G4
    }

# ----------------------------------- Cello  -----------------------------------


class NoteEquivalenceCello:
    """
    The note equivalence for the cello instrument.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535
    # Around 65-130Hz
    # C2 to A3
    # 2 is used to represent the second octave
    C2 = DEFAULT_C2
    CSH2 = DEFAULT_CSH2
    DB2 = DEFAULT_DB2
    D2 = DEFAULT_D2
    DSH2 = DEFAULT_DSH2
    EB2 = DEFAULT_EB2
    E2 = DEFAULT_E2
    F2 = DEFAULT_F2
    FSH2 = DEFAULT_FSH2
    GB2 = DEFAULT_GB2
    G2 = DEFAULT_G2
    GSH2 = DEFAULT_GSH2
    AB2 = DEFAULT_AB2
    A2 = DEFAULT_A2
    ASH2 = DEFAULT_ASH2
    BB2 = DEFAULT_BB2
    B2 = DEFAULT_B2

    # 3 is used to represent the third octave
    C3 = DEFAULT_C3
    CSH3 = DEFAULT_CSH3
    DB3 = DEFAULT_DB3
    D3 = DEFAULT_D3
    DSH3 = DEFAULT_DSH3
    EB3 = DEFAULT_EB3
    E3 = DEFAULT_E3
    F3 = DEFAULT_F3
    FSH3 = DEFAULT_FSH3
    GB3 = DEFAULT_GB3
    G3 = DEFAULT_G3
    GSH3 = DEFAULT_GSH3
    AB3 = DEFAULT_AB3
    A3 = DEFAULT_A3
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": C2, "C#": CSH2, "D♭": DB2, "D": D2, "D#": DSH2, "E♭": EB2, "E": E2, "F": F2, "F#": FSH2, "G♭": GB2, "G": G2, "G#": GSH2, "A♭": AB2, "A": A2, "A#": ASH2, "B♭": BB2, "B": B2,
        "C2": C2, "C#2": CSH2, "D♭2": DB2, "D2": D2, "D#2": DSH2, "E♭2": EB2, "E2": E2, "F2": F2, "F#2": FSH2, "G♭2": GB2, "G2": G2, "G#2": GSH2, "A♭2": AB2, "A2": A2, "A#2": ASH2, "B♭2": BB2, "B2": B2,
        "C3": C3, "C#3": CSH3, "D♭3": DB3, "D3": D3, "D#3": DSH3, "E♭3": EB3, "E3": E3, "F3": F3, "F#3": FSH3, "G♭3": GB3, "G3": G3, "G#3": GSH3, "A♭3": AB3, "A3": A3
    }

# ----------------------------- 24 bit frequencies -----------------------------


class NoteEquivalence24bit:
    """
    The note equivalence for 24 bit frequencies.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = 48000
    MAX_BIT_VALUE = 65535

    # -1 is used to represent negative notes
    CN1 = DEFAULT_CN1
    CSHN1 = DEFAULT_CSHN1
    DBN1 = DEFAULT_DBN1
    DN1 = DEFAULT_DN1
    DSHN1 = DEFAULT_DSHN1
    EBN1 = DEFAULT_EBN1
    EN1 = DEFAULT_EN1
    FN1 = DEFAULT_FN1
    FSHN1 = DEFAULT_FSHN1
    GBN1 = DEFAULT_GBN1
    GN1 = DEFAULT_GN1
    GSHN1 = DEFAULT_GSHN1
    ABN1 = DEFAULT_ABN1
    AN1 = DEFAULT_AN1
    ASHN1 = DEFAULT_ASHN1
    BBN1 = DEFAULT_BBN1
    BN1 = DEFAULT_BN1

    # 0 is used to represent the base note
    C0 = DEFAULT_C0
    CSH0 = DEFAULT_CSH0
    DB0 = DEFAULT_DB0
    D0 = DEFAULT_D0
    DSH0 = DEFAULT_DSH0
    EB0 = DEFAULT_EB0
    E0 = DEFAULT_E0
    F0 = DEFAULT_F0
    FSH0 = DEFAULT_FSH0
    GB0 = DEFAULT_GB0
    G0 = DEFAULT_G0
    GSH0 = DEFAULT_GSH0
    AB0 = DEFAULT_AB0
    A0 = DEFAULT_A0
    ASH0 = DEFAULT_ASH0
    BB0 = DEFAULT_BB0
    B0 = DEFAULT_B0

    # 1 is used to represent the first octave
    C1 = DEFAULT_C1
    CSH1 = DEFAULT_CSH1
    DB1 = DEFAULT_DB1
    D1 = DEFAULT_D1
    DSH1 = DEFAULT_DSH1
    EB1 = DEFAULT_EB1
    E1 = DEFAULT_E1
    F1 = DEFAULT_F1
    FSH1 = DEFAULT_FSH1
    GB1 = DEFAULT_GB1
    G1 = DEFAULT_G1
    GSH1 = DEFAULT_GSH1
    AB1 = DEFAULT_AB1
    A1 = DEFAULT_A1
    ASH1 = DEFAULT_ASH1
    BB1 = DEFAULT_BB1
    B1 = DEFAULT_B1

    # 2 is used to represent the second octave
    C2 = DEFAULT_C2
    CSH2 = DEFAULT_CSH2
    DB2 = DEFAULT_DB2
    D2 = DEFAULT_D2
    DSH2 = DEFAULT_DSH2
    EB2 = DEFAULT_EB2
    E2 = DEFAULT_E2
    F2 = DEFAULT_F2
    FSH2 = DEFAULT_FSH2
    GB2 = DEFAULT_GB2
    G2 = DEFAULT_G2
    GSH2 = DEFAULT_GSH2
    AB2 = DEFAULT_AB2
    A2 = DEFAULT_A2
    ASH2 = DEFAULT_ASH2
    BB2 = DEFAULT_BB2
    B2 = DEFAULT_B2

    # 3 is used to represent the third octave
    C3 = DEFAULT_C3
    CSH3 = DEFAULT_CSH3
    DB3 = DEFAULT_DB3
    D3 = DEFAULT_D3
    DSH3 = DEFAULT_DSH3
    EB3 = DEFAULT_EB3
    E3 = DEFAULT_E3
    F3 = DEFAULT_F3
    FSH3 = DEFAULT_FSH3
    GB3 = DEFAULT_GB3
    G3 = DEFAULT_G3
    GSH3 = DEFAULT_GSH3
    AB3 = DEFAULT_AB3
    A3 = DEFAULT_A3
    ASH3 = DEFAULT_ASH3
    BB3 = DEFAULT_BB3
    B3 = DEFAULT_B3

    # 4 is used to represent the fourth octave
    C4 = DEFAULT_C4
    CSH4 = DEFAULT_CSH4
    DB4 = DEFAULT_DB4
    D4 = DEFAULT_D4
    DSH4 = DEFAULT_DSH4
    EB4 = DEFAULT_EB4
    E4 = DEFAULT_E4
    F4 = DEFAULT_F4
    FSH4 = DEFAULT_FSH4
    GB4 = DEFAULT_GB4
    G4 = DEFAULT_G4
    GSH4 = DEFAULT_GSH4
    AB4 = DEFAULT_AB4
    A4 = DEFAULT_A4
    ASH4 = DEFAULT_ASH4
    BB4 = DEFAULT_BB4
    B4 = DEFAULT_B4

    # 5 is used to represent the fifth octave
    C5 = DEFAULT_C5
    CSH5 = DEFAULT_CSH5
    DB5 = DEFAULT_DB5
    D5 = DEFAULT_D5
    DSH5 = DEFAULT_DSH5
    EB5 = DEFAULT_EB5
    E5 = DEFAULT_E5
    F5 = DEFAULT_F5
    FSH5 = DEFAULT_FSH5
    GB5 = DEFAULT_GB5
    G5 = DEFAULT_G5
    GSH5 = DEFAULT_GSH5
    AB5 = DEFAULT_AB5
    A5 = DEFAULT_A5
    ASH5 = DEFAULT_ASH5
    BB5 = DEFAULT_BB5
    B5 = DEFAULT_B5

    # 6 is used to represent the sixth octave
    C6 = DEFAULT_C6
    CSH6 = DEFAULT_CSH6
    DB6 = DEFAULT_DB6
    D6 = DEFAULT_D6
    DSH6 = DEFAULT_DSH6
    EB6 = DEFAULT_EB6
    E6 = DEFAULT_E6
    F6 = DEFAULT_F6
    FSH6 = DEFAULT_FSH6
    GB6 = DEFAULT_GB6
    G6 = DEFAULT_G6
    GSH6 = DEFAULT_GSH6
    AB6 = DEFAULT_AB6
    A6 = DEFAULT_A6
    ASH6 = DEFAULT_ASH6
    BB6 = DEFAULT_BB6
    B6 = DEFAULT_B6

    # 7 is used to represent the seventh octave
    C7 = DEFAULT_C7
    CSH7 = DEFAULT_CSH7
    DB7 = DEFAULT_DB7
    D7 = DEFAULT_D7
    DSH7 = DEFAULT_DSH7
    EB7 = DEFAULT_EB7
    E7 = DEFAULT_E7
    F7 = DEFAULT_F7
    FSH7 = DEFAULT_FSH7
    GB7 = DEFAULT_GB7
    G7 = DEFAULT_G7
    GSH7 = DEFAULT_GSH7
    AB7 = DEFAULT_AB7
    A7 = DEFAULT_A7
    ASH7 = DEFAULT_ASH7
    BB7 = DEFAULT_BB7
    B7 = DEFAULT_B7

    # 8 is used to represent the eighth octave
    C8 = DEFAULT_C8
    CSH8 = DEFAULT_CSH8
    DB8 = DEFAULT_DB8
    D8 = DEFAULT_D8
    DSH8 = DEFAULT_DSH8
    EB8 = DEFAULT_EB8
    E8 = DEFAULT_E8
    F8 = DEFAULT_F8
    FSH8 = DEFAULT_FSH8
    GB8 = DEFAULT_GB8
    G8 = DEFAULT_G8
    GSH8 = DEFAULT_GSH8
    AB8 = DEFAULT_AB8
    A8 = DEFAULT_A8
    ASH8 = DEFAULT_ASH8
    BB8 = DEFAULT_BB8
    B8 = DEFAULT_B8

    # 9 is used to represent the ninth octave
    C9 = DEFAULT_C9
    CSH9 = DEFAULT_CSH9
    DB9 = DEFAULT_DB9
    D9 = DEFAULT_D9
    DSH9 = DEFAULT_DSH9
    EB9 = DEFAULT_EB9
    E9 = DEFAULT_E9
    F9 = DEFAULT_F9
    FSH9 = DEFAULT_FSH9
    GB9 = DEFAULT_GB9
    G9 = DEFAULT_G9
    GSH9 = DEFAULT_GSH9
    AB9 = DEFAULT_AB9
    A9 = DEFAULT_A9
    ASH9 = DEFAULT_ASH9
    BB9 = DEFAULT_BB9
    B9 = DEFAULT_B9
    NOTE_EQUIVALENCE = DEFAULT_NOTE_EQUIVALENCE

# ----------------------------- 32 bit frequencies -----------------------------


class NoteEquivalence32bit:
    """
    The class in charge of containing the note equivalence for the 32 bit instruments.
    """
    MUTE = DEFAULT_MUTE
    SAMPLE_RATE = 192000
    MAX_BIT_VALUE = 65535

    # -1 is used to represent negative notes
    CN1 = DEFAULT_CN1
    CSHN1 = DEFAULT_CSHN1
    DBN1 = DEFAULT_DBN1
    DN1 = DEFAULT_DN1
    DSHN1 = DEFAULT_DSHN1
    EBN1 = DEFAULT_EBN1
    EN1 = DEFAULT_EN1
    FN1 = DEFAULT_FN1
    FSHN1 = DEFAULT_FSHN1
    GBN1 = DEFAULT_GBN1
    GN1 = DEFAULT_GN1
    GSHN1 = DEFAULT_GSHN1
    ABN1 = DEFAULT_ABN1
    AN1 = DEFAULT_AN1
    ASHN1 = DEFAULT_ASHN1
    BBN1 = DEFAULT_BBN1
    BN1 = DEFAULT_BN1

    # 0 is used to represent the base note
    C0 = DEFAULT_C0
    CSH0 = DEFAULT_CSH0
    DB0 = DEFAULT_DB0
    D0 = DEFAULT_D0
    DSH0 = DEFAULT_DSH0
    EB0 = DEFAULT_EB0
    E0 = DEFAULT_E0
    F0 = DEFAULT_F0
    FSH0 = DEFAULT_FSH0
    GB0 = DEFAULT_GB0
    G0 = DEFAULT_G0
    GSH0 = DEFAULT_GSH0
    AB0 = DEFAULT_AB0
    A0 = DEFAULT_A0
    ASH0 = DEFAULT_ASH0
    BB0 = DEFAULT_BB0
    B0 = DEFAULT_B0

    # 1 is used to represent the first octave
    C1 = DEFAULT_C1
    CSH1 = DEFAULT_CSH1
    DB1 = DEFAULT_DB1
    D1 = DEFAULT_D1
    DSH1 = DEFAULT_DSH1
    EB1 = DEFAULT_EB1
    E1 = DEFAULT_E1
    F1 = DEFAULT_F1
    FSH1 = DEFAULT_FSH1
    GB1 = DEFAULT_GB1
    G1 = DEFAULT_G1
    GSH1 = DEFAULT_GSH1
    AB1 = DEFAULT_AB1
    A1 = DEFAULT_A1
    ASH1 = DEFAULT_ASH1
    BB1 = DEFAULT_BB1
    B1 = DEFAULT_B1

    # 2 is used to represent the second octave
    C2 = DEFAULT_C2
    CSH2 = DEFAULT_CSH2
    DB2 = DEFAULT_DB2
    D2 = DEFAULT_D2
    DSH2 = DEFAULT_DSH2
    EB2 = DEFAULT_EB2
    E2 = DEFAULT_E2
    F2 = DEFAULT_F2
    FSH2 = DEFAULT_FSH2
    GB2 = DEFAULT_GB2
    G2 = DEFAULT_G2
    GSH2 = DEFAULT_GSH2
    AB2 = DEFAULT_AB2
    A2 = DEFAULT_A2
    ASH2 = DEFAULT_ASH2
    BB2 = DEFAULT_BB2
    B2 = DEFAULT_B2

    # 3 is used to represent the third octave
    C3 = DEFAULT_C3
    CSH3 = DEFAULT_CSH3
    DB3 = DEFAULT_DB3
    D3 = DEFAULT_D3
    DSH3 = DEFAULT_DSH3
    EB3 = DEFAULT_EB3
    E3 = DEFAULT_E3
    F3 = DEFAULT_F3
    FSH3 = DEFAULT_FSH3
    GB3 = DEFAULT_GB3
    G3 = DEFAULT_G3
    GSH3 = DEFAULT_GSH3
    AB3 = DEFAULT_AB3
    A3 = DEFAULT_A3
    ASH3 = DEFAULT_ASH3
    BB3 = DEFAULT_BB3
    B3 = DEFAULT_B3

    # 4 is used to represent the fourth octave
    C4 = DEFAULT_C4
    CSH4 = DEFAULT_CSH4
    DB4 = DEFAULT_DB4
    D4 = DEFAULT_D4
    DSH4 = DEFAULT_DSH4
    EB4 = DEFAULT_EB4
    E4 = DEFAULT_E4
    F4 = DEFAULT_F4
    FSH4 = DEFAULT_FSH4
    GB4 = DEFAULT_GB4
    G4 = DEFAULT_G4
    GSH4 = DEFAULT_GSH4
    AB4 = DEFAULT_AB4
    A4 = DEFAULT_A4
    ASH4 = DEFAULT_ASH4
    BB4 = DEFAULT_BB4
    B4 = DEFAULT_B4

    # 5 is used to represent the fifth octave
    C5 = DEFAULT_C5
    CSH5 = DEFAULT_CSH5
    DB5 = DEFAULT_DB5
    D5 = DEFAULT_D5
    DSH5 = DEFAULT_DSH5
    EB5 = DEFAULT_EB5
    E5 = DEFAULT_E5
    F5 = DEFAULT_F5
    FSH5 = DEFAULT_FSH5
    GB5 = DEFAULT_GB5
    G5 = DEFAULT_G5
    GSH5 = DEFAULT_GSH5
    AB5 = DEFAULT_AB5
    A5 = DEFAULT_A5
    ASH5 = DEFAULT_ASH5
    BB5 = DEFAULT_BB5
    B5 = DEFAULT_B5

    # 6 is used to represent the sixth octave
    C6 = DEFAULT_C6
    CSH6 = DEFAULT_CSH6
    DB6 = DEFAULT_DB6
    D6 = DEFAULT_D6
    DSH6 = DEFAULT_DSH6
    EB6 = DEFAULT_EB6
    E6 = DEFAULT_E6
    F6 = DEFAULT_F6
    FSH6 = DEFAULT_FSH6
    GB6 = DEFAULT_GB6
    G6 = DEFAULT_G6
    GSH6 = DEFAULT_GSH6
    AB6 = DEFAULT_AB6
    A6 = DEFAULT_A6
    ASH6 = DEFAULT_ASH6
    BB6 = DEFAULT_BB6
    B6 = DEFAULT_B6

    # 7 is used to represent the seventh octave
    C7 = DEFAULT_C7
    CSH7 = DEFAULT_CSH7
    DB7 = DEFAULT_DB7
    D7 = DEFAULT_D7
    DSH7 = DEFAULT_DSH7
    EB7 = DEFAULT_EB7
    E7 = DEFAULT_E7
    F7 = DEFAULT_F7
    FSH7 = DEFAULT_FSH7
    GB7 = DEFAULT_GB7
    G7 = DEFAULT_G7
    GSH7 = DEFAULT_GSH7
    AB7 = DEFAULT_AB7
    A7 = DEFAULT_A7
    ASH7 = DEFAULT_ASH7
    BB7 = DEFAULT_BB7
    B7 = DEFAULT_B7

    # 8 is used to represent the eighth octave
    C8 = DEFAULT_C8
    CSH8 = DEFAULT_CSH8
    DB8 = DEFAULT_DB8
    D8 = DEFAULT_D8
    DSH8 = DEFAULT_DSH8
    EB8 = DEFAULT_EB8
    E8 = DEFAULT_E8
    F8 = DEFAULT_F8
    FSH8 = DEFAULT_FSH8
    GB8 = DEFAULT_GB8
    G8 = DEFAULT_G8
    GSH8 = DEFAULT_GSH8
    AB8 = DEFAULT_AB8
    A8 = DEFAULT_A8
    ASH8 = DEFAULT_ASH8
    BB8 = DEFAULT_BB8
    B8 = DEFAULT_B8

    # 9 is used to represent the ninth octave
    C9 = DEFAULT_C9
    CSH9 = DEFAULT_CSH9
    DB9 = DEFAULT_DB9
    D9 = DEFAULT_D9
    DSH9 = DEFAULT_DSH9
    EB9 = DEFAULT_EB9
    E9 = DEFAULT_E9
    F9 = DEFAULT_F9
    FSH9 = DEFAULT_FSH9
    GB9 = DEFAULT_GB9
    G9 = DEFAULT_G9
    GSH9 = DEFAULT_GSH9
    AB9 = DEFAULT_AB9
    A9 = DEFAULT_A9
    ASH9 = DEFAULT_ASH9
    BB9 = DEFAULT_BB9
    B9 = DEFAULT_B9
    NOTE_EQUIVALENCE = DEFAULT_NOTE_EQUIVALENCE

# --------------------- Piano notes and their frequencies. ---------------------


class NoteEquivalencePiano:
    """
        The class in charge of the piano notes and their frequencies.
    """
    SAMPLE_RATE = DEFAULT_SAMPLE_RATE
    MAX_BIT_VALUE = 65535

    MUTE = DEFAULT_MUTE

    # 0 is used to represent the base note.
    C0 = 16.35
    CSH0 = 17.32
    D0 = 18.35
    Eb0 = 19.45
    E0 = 20.6
    F0 = 21.83
    FSH0 = 23.12
    G0 = 24.5
    Ab0 = 25.96
    A0 = 27.5
    Bb0 = 29.14
    B0 = 30.87

    # 1 is used to represent the first octave.
    C1 = 32.7
    CSH1 = 34.65
    D1 = 36.71
    Eb1 = 38.89
    E1 = 41.2
    F1 = 43.65
    FSH1 = 46.25
    G1 = 49
    Ab1 = 51.91
    A1 = 55
    Bb1 = 58.27
    B1 = 61.74

    # 2 is used to represent the second octave.
    C2 = 65.41
    CSH2 = 69.3
    D2 = 73.42
    Eb2 = 77.78
    E2 = 82.41
    F2 = 87.31
    FSH2 = 92.5
    G2 = 98
    Ab2 = 103.83
    A2 = 110
    Bb2 = 116.54
    B2 = 123.47

    # 3 is used to represent the third octave.
    C3 = 130.81
    CSH3 = 138.59
    D3 = 146.83
    Eb3 = 155.56
    E3 = 164.81
    F3 = 174.61
    FSH3 = 185
    G3 = 196
    Ab3 = 207.65
    A3 = 220
    Bb3 = 233.08
    B3 = 246.94

    # 4 is used to represent the fourth octave.
    C4 = 261.63
    CSH4 = 277.18
    D4 = 293.66
    Eb4 = 311.13
    E4 = 329.63
    F4 = 349.23
    FSH4 = 369.99
    G4 = 392
    Ab4 = 415.3
    A4 = 440
    Bb4 = 466.16
    B4 = 493.88

    # 5 is used to represent the fifth octave.
    C5 = 523.25
    CSH5 = 554.37
    D5 = 587.33
    Eb5 = 622.25
    E5 = 659.25
    F5 = 698.46
    FSH5 = 739.99
    G5 = 783.99
    Ab5 = 830.61
    A5 = 880
    Bb5 = 932.33
    B5 = 987.77

    # 6 is used to represent the sixth octave.
    C6 = 1046.5
    CSH6 = 1108.73
    D6 = 1174.66
    Eb6 = 1244.51
    E6 = 1318.51
    F6 = 1396.91
    FSH6 = 1479.98
    G6 = 1567.98
    Ab6 = 1661.22
    A6 = 1760
    Bb6 = 1864.66
    B6 = 1975.53

    # 7 is used to represent the seventh octave.
    C7 = 2093
    CSH7 = 2217.46
    D7 = 2349.32
    Eb7 = 2489.02
    E7 = 2637.02
    F7 = 2793.83
    FSH7 = 2959.96
    G7 = 3135.96
    Ab7 = 3322.44
    A7 = 3520
    Bb7 = 3729.31
    B7 = 3951.07

    # 8 is used to represent the eighth octave.
    C8 = 4186.01
    CSH8 = 4434.92
    D8 = 4698.63
    Eb8 = 4978.03
    E8 = 5274.04
    F8 = 5587.65
    FSH8 = 5919.91
    G8 = 6271.93
    Ab8 = 6644.88
    A8 = 7040
    Bb8 = 7458.62
    B8 = 7902.13

    # Dictionary of notes
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": C4, "C#": CSH4, "D": D4, "D#": Eb4, "E": E4, "F": F4, "F#": FSH4, "G": G4, "G#": Ab4, "A": A4, "A#": Bb4, "B": B4,
        "C0": C0, "C#0": CSH0, "D0": D0, "D#0": Eb0, "E0": E0, "F0": F0, "F#0": FSH0, "G0": G0, "G#0": Ab0, "A0": A0, "A#0": Bb0, "B0": B0,
        "C1": C1, "C#1": CSH1, "D1": D1, "D#1": Eb1, "E1": E1, "F1": F1, "F#1": FSH1, "G1": G1, "G#1": Ab1, "A1": A1, "A#1": Bb1, "B1": B1,
        "C2": C2, "C#2": CSH2, "D2": D2, "D#2": Eb2, "E2": E2, "F2": F2, "F#2": FSH2, "G2": G2, "G#2": Ab2, "A2": A2, "A#2": Bb2, "B2": B2,
        "C3": C3, "C#3": CSH3, "D3": D3, "D#3": Eb3, "E3": E3, "F3": F3, "F#3": FSH3, "G3": G3, "G#3": Ab3, "A3": A3, "A#3": Bb3, "B3": B3,
        "C4": C4, "C#4": CSH4, "D4": D4, "D#4": Eb4, "E4": E4, "F4": F4, "F#4": FSH4, "G4": G4, "G#4": Ab4, "A4": A4, "A#4": Bb4, "B4": B4,
        "C5": C5, "C#5": CSH5, "D5": D5, "D#5": Eb5, "E5": E5, "F5": F5, "F#5": FSH5, "G5": G5, "G#5": Ab5, "A5": A5, "A#5": Bb5, "B5": B5,
        "C6": C6, "C#6": CSH6, "D6": D6, "D#6": Eb6, "E6": E6, "F6": F6, "F#6": FSH6, "G6": G6, "G#6": Ab6, "A6": A6, "A#6": Bb6, "B6": B6,
        "C7": C7, "C#7": CSH7, "D7": D7, "D#7": Eb7, "E7": E7, "F7": F7, "F#7": FSH7, "G7": G7, "G#7": Ab7, "A7": A7, "A#7": Bb7, "B7": B7,
        "C8": C8, "C#8": CSH8, "D8": D8, "D#8": Eb8, "E8": E8, "F8": F8, "F#8": FSH8, "G8": G8, "G#8": Ab8, "A8": A8, "A#8": Bb8, "B8": B8
    }

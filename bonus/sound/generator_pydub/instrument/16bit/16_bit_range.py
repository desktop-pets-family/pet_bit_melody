"""
    This script generates a range of 8 bit sounds
"""
import os
import sys
from typing import List, Union
from platform import system

# Audio generation libraries
import numpy as np


def process_ffmpeg_path():
    """
    This function processes the path to the FFmpeg executable.
    """
    print("Adding local ff family binaries to path.")
    ffmpeg_base_path = os.path.join(
        "..", "..", "..", "..", "server", "ff_family"
    )
    if system() == "Windows":
        sys_name = "windows"
        final_ffmpeg_path = os.path.join(
            ffmpeg_base_path, "ffmpeg", sys_name, "ffmpeg.exe"
        )
        final_ffprobe_path = os.path.join(
            ffmpeg_base_path, "ffprobe", sys_name, "ffprobe.exe"
        )
        final_ffplay_path = os.path.join(
            ffmpeg_base_path, "ffplay", sys_name
        )
    elif system() == "Linux":
        sys_name = "linux"
        final_ffmpeg_path = os.path.join(
            ffmpeg_base_path, "ffmpeg", sys_name, "ffmpeg"
        )
        final_ffprobe_path = os.path.join(
            ffmpeg_base_path, "ffprobe", sys_name, "ffprobe"
        )
        final_ffplay_path = os.path.join(
            ffmpeg_base_path, "ffplay", sys_name
        )
    elif system() == "Darwin":
        sys_name = "darwin"
        final_ffmpeg_path = os.path.join(
            ffmpeg_base_path, "ffmpeg", sys_name, "ffmpeg"
        )
        final_ffprobe_path = os.path.join(
            ffmpeg_base_path, "ffprobe", sys_name, "ffprobe"
        )
        final_ffplay_path = os.path.join(
            ffmpeg_base_path, "ffplay", sys_name
        )
    else:
        raise RuntimeWarning("Unsupported operating system.")
    sys.path.append(final_ffmpeg_path)
    sys.path.append(final_ffprobe_path)
    sys.path.append(final_ffplay_path)
    os.environ['PATH'] = final_ffmpeg_path + os.pathsep + final_ffprobe_path + \
        os.pathsep + final_ffplay_path + os.pathsep + os.environ['PATH']
    AudioSegment.ffmpeg = final_ffmpeg_path
    print("FFmpeg path set to:", AudioSegment.ffmpeg)


# Attempting to import pydub
try:
    from pydub import AudioSegment
    from pydub import playback
    from pydub.generators import Sine
    process_ffmpeg_path()
except ImportError:
    print("PyDub is not installed. Please install it using 'pip install pydub'.")
except Exception as e:
    print("An error occurred:", e)
    process_ffmpeg_path()


class NoteEquivalence16bit:
    """
    This class contains the equivalence of the notes in the 16-bit range.
    All frequencies are scaled to fit within the range of 8.18–65535 Hz.
    """
    MUTE = 1

    # Notes in the 16-bit range

    # -1 is used to represent negative notes
    CN1 = 8.18
    CSHN1 = 8.66
    DBN1 = 8.66
    DN1 = 9.18
    DSHN1 = 9.72
    EBN1 = 9.72
    EN1 = 10.30
    FN1 = 10.91
    FSHN1 = 11.56
    GBN1 = 11.56
    GN1 = 12.25
    GSHN1 = 12.98
    ABN1 = 12.98
    AN1 = 13.75
    ASHN1 = 14.57
    BBN1 = 14.57
    BN1 = 15.43

    # 0 is used to represent the base note
    C0 = 16.35
    CSH0 = 17.32
    DB0 = 17.32
    D0 = 18.35
    DSH0 = 19.45
    EB0 = 19.45
    E0 = 20.60
    F0 = 21.83
    FSH0 = 23.12
    GB0 = 23.12
    G0 = 24.50
    GSH0 = 25.96
    AB0 = 25.96
    A0 = 27.50
    ASH0 = 29.14
    BB0 = 29.14
    B0 = 30.87

    # 1 is used to represent the first octave
    C1 = 32.70
    CSH1 = 34.65
    DB1 = 34.65
    D1 = 36.71
    DSH1 = 38.89
    EB1 = 38.89
    E1 = 41.20
    F1 = 43.65
    FSH1 = 46.25
    GB1 = 46.25
    G1 = 49.00
    GSH1 = 51.91
    AB1 = 51.91
    A1 = 55.00
    ASH1 = 58.27
    BB1 = 58.27
    B1 = 61.74

    # 2 is used to represent the second octave
    C2 = 65.41
    CSH2 = 69.30
    DB2 = 69.30
    D2 = 73.42
    DSH2 = 77.78
    EB2 = 77.78
    E2 = 82.41
    F2 = 87.31
    FSH2 = 92.50
    GB2 = 92.50
    G2 = 98.00
    GSH2 = 103.83
    AB2 = 103.83
    A2 = 110.00
    ASH2 = 116.54
    BB2 = 116.54
    B2 = 123.47

    # 3 is used to represent the third octave
    C3 = 130.81
    CSH3 = 138.59
    DB3 = 138.59
    D3 = 146.83
    DSH3 = 155.56
    EB3 = 155.56
    E3 = 164.81
    F3 = 174.61
    FSH3 = 185.00
    GB3 = 185.00
    G3 = 196.00
    GSH3 = 207.65
    AB3 = 207.65
    A3 = 220.00
    ASH3 = 233.08
    BB3 = 233.08
    B3 = 246.94

    # 4 is used to represent the fourth octave
    C4 = 261.63
    CSH4 = 277.18
    DB4 = 277.18
    D4 = 293.66
    DSH4 = 311.13
    EB4 = 311.13
    E4 = 329.63
    F4 = 349.23
    FSH4 = 369.99
    GB4 = 369.99
    G4 = 392.00
    GSH4 = 415.30
    AB4 = 415.30
    A4 = 440.00
    ASH4 = 466.16
    BB4 = 466.16
    B4 = 493.88

    # 5 is used to represent the fifth octave
    C5 = 523.25
    CSH5 = 554.37
    DB5 = 554.37
    D5 = 587.33
    DSH5 = 622.25
    EB5 = 622.25
    E5 = 659.25
    F5 = 698.46
    FSH5 = 739.99
    GB5 = 739.99
    G5 = 783.99
    GSH5 = 830.61
    AB5 = 830.61
    A5 = 880.00
    ASH5 = 932.33
    BB5 = 932.33
    B5 = 987.77

    # 6 is used to represent the sixth octave
    C6 = 1046.50
    CSH6 = 1108.73
    DB6 = 1108.73
    D6 = 1174.66
    DSH6 = 1244.51
    EB6 = 1244.51
    E6 = 1318.51
    F6 = 1396.91
    FSH6 = 1479.98
    GB6 = 1479.98
    G6 = 1567.98
    GSH6 = 1661.22
    AB6 = 1661.22
    A6 = 1760.00
    ASH6 = 1864.66
    BB6 = 1864.66
    B6 = 1975.53

    # 7 is used to represent the seventh octave
    C7 = 2093.00
    CSH7 = 2217.46
    DB7 = 2217.46
    D7 = 2349.32
    DSH7 = 2489.02
    EB7 = 2489.02
    E7 = 2637.02
    F7 = 2793.83
    FSH7 = 2959.96
    GB7 = 2959.96
    G7 = 3135.96
    GSH7 = 3322.44
    AB7 = 3322.44
    A7 = 3520.00
    ASH7 = 3729.31
    BB7 = 3729.31
    B7 = 3951.07

    # 8 is used to represent the eighth octave
    C8 = 4186.01
    CSH8 = 4434.92
    DB8 = 4434.92
    D8 = 4698.63
    DSH8 = 4978.03
    EB8 = 4978.03
    E8 = 5274.04
    F8 = 5587.65
    FSH8 = 5919.91
    GB8 = 5919.91
    G8 = 6271.93
    GSH8 = 6644.88
    AB8 = 6644.88
    A8 = 7040.00
    ASH8 = 7458.62
    BB8 = 7458.62
    B8 = 7902.13

    # 9 is used to represent the ninth octave
    C9 = 8372.02
    CSH9 = 8869.84
    DB9 = 8869.84
    D9 = 9397.27
    DSH9 = 9956.06
    EB9 = 9956.06
    E9 = 10548.08
    F9 = 11175.30
    FSH9 = 11839.82
    GB9 = 11839.82
    G9 = 12543.85
    GSH9 = 13289.75
    AB9 = 13289.75
    A9 = 14080.00
    ASH9 = 14917.24
    BB9 = 14917.24
    B9 = 15804.27

    # Dictionary of notes
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C": C4, "C#": CSH4, "D♭": DB4, "D": D4, "D#": DSH4, "E♭": EB4, "E": E4, "F": F4, "F#": FSH4, "G♭": GB4, "G": G4, "G#": GSH4, "A♭": AB4, "A": A4, "A#": ASH4, "B♭": BB4, "B": B4,
        "C-1": CN1, "C#-1": CSHN1, "D♭-1": DBN1, "D-1": DN1, "D#-1": DSHN1, "E♭-1": EBN1, "E-1": EN1, "F-1": FN1, "F#-1": FSHN1, "G♭-1": GBN1, "G-1": GN1, "G#-1": GSHN1, "A♭-1": ABN1, "A-1": AN1, "A#-1": ASHN1, "B♭-1": BBN1, "B-1": BN1,
        "C0": C0, "C#0": CSH0, "D♭0": DB0, "D0": D0, "D#0": DSH0, "E♭0": EB0, "E0": E0, "F0": F0, "F#0": FSH0, "G♭0": GB0, "G0": G0, "G#0": GSH0, "A♭0": AB0, "A0": A0, "A#0": ASH0, "B♭0": BB0, "B0": B0,
        "C1": C1, "C#1": CSH1, "D♭1": DB1, "D1": D1, "D#1": DSH1, "E♭1": EB1, "E1": E1, "F1": F1, "F#1": FSH1, "G♭1": GB1, "G1": G1, "G#1": GSH1, "A♭1": AB1, "A1": A1, "A#1": ASH1, "B♭1": BB1, "B1": B1,
        "C2": C2, "C#2": CSH2, "D♭2": DB2, "D2": D2, "D#2": DSH2, "E♭2": EB2, "E2": E2, "F2": F2, "F#2": FSH2, "G♭2": GB2, "G2": G2, "G#2": GSH2, "A♭2": AB2, "A2": A2, "A#2": ASH2, "B♭2": BB2, "B2": B2,
        "C3": C3, "C#3": CSH3, "D♭3": DB3, "D3": D3, "D#3": DSH3, "E♭3": EB3, "E3": E3, "F3": F3, "F#3": FSH3, "G♭3": GB3, "G3": G3, "G#3": GSH3, "A♭3": AB3, "A3": A3, "A#3": ASH3, "B♭3": BB3, "B3": B3,
        "C4": C4, "C#4": CSH4, "D♭4": DB4, "D4": D4, "D#4": DSH4, "E♭4": EB4, "E4": E4, "F4": F4, "F#4": FSH4, "G♭4": GB4, "G4": G4, "G#4": GSH4, "A♭4": AB4, "A4": A4, "A#4": ASH4, "B♭4": BB4, "B4": B4,
        "C5": C5, "C#5": CSH5, "D♭5": DB5, "D5": D5, "D#5": DSH5, "E♭5": EB5, "E5": E5, "F5": F5, "F#5": FSH5, "G♭5": GB5, "G5": G5, "G#5": GSH5, "A♭5": AB5, "A5": A5, "A#5": ASH5, "B♭5": BB5, "B5": B5,
        "C6": C6, "C#6": CSH6, "D♭6": DB6, "D6": D6, "D#6": DSH6, "E♭6": EB6, "E6": E6, "F6": F6, "F#6": FSH6, "G♭6": GB6, "G6": G6, "G#6": GSH6, "A♭6": AB6, "A6": A6, "A#6": ASH6, "B♭6": BB6, "B6": B6,
        "C7": C7, "C#7": CSH7, "D♭7": DB7, "D7": D7, "D#7": DSH7, "E♭7": EB7, "E7": E7, "F7": F7, "F#7": FSH7, "G♭7": GB7, "G7": G7, "G#7": GSH7, "A♭7": AB7, "A7": A7, "A#7": ASH7, "B♭7": BB7, "B7": B7,
        "C8": C8, "C#8": CSH8, "D♭8": DB8, "D8": D8, "D#8": DSH8, "E♭8": EB8, "E8": E8, "F8": F8, "F#8": FSH8, "G♭8": GB8, "G8": G8, "G#8": GSH8, "A♭8": AB8, "A8": A8, "A#8": ASH8, "B♭8": BB8, "B8": B8,
        "C9": C9, "C#9": CSH9, "D♭9": DB9, "D9": D9, "D#9": DSH9, "E♭9": EB9, "E9": E9, "F9": F9, "F#9": FSH9, "G♭9": GB9, "G9": G9, "G#9": GSH9, "A♭9": AB9, "A9": A9, "A#9": ASH9, "B♭9": BB9, "B9": B9
    }


# The function that generates the 8 bit notes


class Note16bit(NoteEquivalence16bit):
    """_summary_
    This class generates 16-bit audio notes.

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    NOTE_DURATION = 1.0
    SAMPLE_RATE = 44100
    MAX_16BIT_VALUE = 65535

    def __init__(self, note: Union[List[int], int] = 80, duration: float = 3.0, amplitude: float = 0.5, sample_rate: int = 44100, base_track: Union[AudioSegment, None] = None) -> AudioSegment:
        if isinstance(note, list) is False:
            note = [note]
        self.note = note
        self.duration = duration
        self.amplitude = amplitude
        self.sample_rate = sample_rate
        self.base_track = base_track
        self.sixteen_bit_range = self.generate_16bit_frequencies()
        self.sixteen_bit_frequencies = Note16bit.NOTE_EQUIVALENCE

    def __call__(self, note: Union[List[int], int], duration: float = None, amplitude: float = None, sample_rate: int = None, base_audio: Union[AudioSegment, None] = None) -> AudioSegment:
        """
        Allows the class to be called like a function to generate audio for given parameters.

        Args:
            note (Union[List[int], int]): A single frequency or list of frequencies.
            duration (float, optional): Duration of the note(s). Defaults to the instance's duration.
            amplitude (float, optional): Amplitude of the note(s). Defaults to the instance's amplitude.
            sample_rate (int, optional): Sample rate of the audio. Defaults to the instance's sample rate.
            base_audio (Union[AudioSegment, None], optional): The existing audio segment to append the note to. Pass None to start a new sequence. Defaults to None.

        Returns:
            AudioSegment: The generated audio.
        """
        if isinstance(note, list) is False:
            note = [note]
        if duration is None:
            duration = self.duration
        if amplitude is None:
            amplitude = self.amplitude
        if sample_rate is None:
            sample_rate = self.sample_rate
        if base_audio is None:
            base_audio = self.base_track

        for item in note:
            if item not in self.sixteen_bit_range:
                raise ValueError(
                    f"Frequency must be present in {self.sixteen_bit_range}."
                )
            base_audio = self.add_note(
                base_audio,
                item,
                self.duration,
                self.amplitude,
                self.sample_rate
            )
        return base_audio

    @staticmethod
    def generate_16bit_frequencies() -> List[int]:
        """_summary_
            The function in charge of generating the 16 bit frequencies.

        Returns:
            List[int]: The list of the 16 bit frequencies.
        """
        return list(range(1, Note16bit.MAX_16BIT_VALUE + 1))

    @staticmethod
    def get_available_notes() -> List[str]:
        """_summary_
        Get the available notes in the 16-bit range.

        Returns:
            Dict[str, int]: The available notes in the 16-bit range.
        """
        return list(Note16bit.NOTE_EQUIVALENCE)

    @staticmethod
    def create_note(frequency: Union[float, int, str] = 80, duration: float = 3.0, amplitude: float = 0.5, sample_rate: int = 44100) -> AudioSegment:
        """
            Generates a single note as an AudioSegment.

        Args:
            frequency (float, int, str, optional): The frequency of the note to generate. Defaults to 80.
            duration (float, optional): The duration of that note. Defaults to 3.0.
            amplitude (float, optional): The amplitude of the note. Defaults to 0.5.
            sample_rate (int, optional): The sample rate. Defaults to 44100.

        Returns:
            AudioSegment: A single note as an AudioSegment.
        """

        if isinstance(frequency, str):
            frequency = Note16bit.NOTE_EQUIVALENCE.get(frequency.upper())

        if frequency is None or frequency <= 0 or frequency > Note16bit.MAX_16BIT_VALUE:
            msg = "Frequency must be a note or between 0"
            msg += f" and {Note16bit.MAX_16BIT_VALUE}."
            raise ValueError(msg)

        if duration < 0:
            raise ValueError("Duration must be greater than 0.")

        if amplitude < 0 or amplitude > 1:
            raise ValueError("Amplitude must be between 0 and 1.")

        # Generate time array
        t = np.linspace(
            0,
            duration,
            int(sample_rate * duration),
            endpoint=False
        )

        # Generate sine wave
        waveform = amplitude * np.sin(2 * np.pi * frequency * t)

        # Convert waveform to 16-bit PCM format
        waveform_integers = np.int16(waveform * 32767)

        # Create an AudioSegment from the waveform
        note_audio = AudioSegment(
            waveform_integers.tobytes(),
            frame_rate=sample_rate,
            sample_width=waveform_integers.dtype.itemsize,
            channels=1
        )

        return note_audio

    @staticmethod
    def append_node(base_audio: AudioSegment, note: AudioSegment) -> AudioSegment:
        """Append a note to the current audio.

        Args:
            base_audio (AudioSegment): The current audio.
            note (AudioSegment): The note to append.

        Raises:
            ValueError: If both base_audio and note are None.

        Returns:
            AudioSegment: The updated audio.
        """
        if base_audio is not None and note is not None:
            return base_audio + note
        if base_audio is None and note is not None:
            return note
        if base_audio is not None and note is None:
            return base_audio
        raise ValueError("Both base_audio and note are None.")

    @staticmethod
    def add_note(base_audio: Union[AudioSegment, None] = None, frequency: Union[float, int, str] = 80, duration: float = 3.0, amplitude: float = 0.5, sample_rate: int = 44100) -> AudioSegment:
        """_summary_
        Adds a note of a given frequency and duration to the audio sequence.

        Args:
            base_audio (Union[AudioSegment, None], optional): The existing audio segment to append the note to. Pass None to start a new sequence. Defaults to None.
            frequency (float, int, str, optional): The frequency of the note in Hz. Defaults to 80.
            duration (float, optional): The duration of the note in seconds. Defaults to 3.0.
            amplitude (float, optional): The amplitude of the note (0.0 to 1.0). Defaults to 0.5.
            sample_rate (int, optional): The sample rate for the audio. Defaults to 44100.

        Raises:
            ValueError: If the frequency is less than 0, the duration is less than 0, or the amplitude is not between 0 and 1.

        Returns:
            AudioSegment: The updated audio segment with the note added.
        """
        note_audio = Note16bit.create_note(
            frequency, duration, amplitude, sample_rate
        )
        return Note16bit.append_node(base_audio, note_audio)

    @staticmethod
    def play(audio: AudioSegment):
        """
        Play the audio.

        Args:
            audio (AudioSegment): The audio to play.
        """
        playback.play(audio)

    @staticmethod
    def save(audio: AudioSegment, filename: str):
        """
            Save the audio to a file

        Args:
            audio (AudioSegment): The audio to save
            filename (str): The filename to save the audio to
        """
        audio.export(filename, format="wav")
        print(f"Audio saved to {filename}")

    @staticmethod
    def test_range(file_name: str = "./16bit_range.wav", silence_duration: float = 0.2) -> None:
        """_summary_
        This function tests the generation of the 8 bit range.

        Args:
            file_name (str, optional): The name of the file to save the audio to. Defaults to "./16bit_range.wav".
            silence_duration (float, optional): The duration of the silence between the notes. Defaults to 0.2.
        """
        # Generate the 16 bit range
        sixteen_bit_range = Note16bit.generate_16bit_frequencies()

        # Generate the audio
        audio = None
        for frequency in sixteen_bit_range:
            print(f"Generating note for frequency {frequency}")
            audio = Note16bit.add_note(
                audio, frequency, Note16bit.NOTE_DURATION
            )
            audio = Note16bit.add_note(
                audio,
                Note16bit.MUTE,
                silence_duration
            )

        # Export the audio
        Note16bit.save(audio, file_name)

    @staticmethod
    def test_notes(file_name: str = "./16bit_notes.wav", silence_duration: float = 0.2) -> None:
        """_summary_
        This function tests the generation of a single note.

        Args:
            file_name (str, optional): The name of the file to save the audio to. Defaults to "./16bit_notes.wav".
            silence_duration (float, optional): The duration of the silence between the notes. Defaults to 0.2.
        """
        # Get the available notes
        notes = Note16bit.get_available_notes()

        audio = None
        for note in notes:
            print(f"Generating note for {note}")
            audio = Note16bit.add_note(audio, note, Note16bit.NOTE_DURATION)
            audio = Note16bit.add_note(
                audio,
                Note16bit.MUTE,
                silence_duration
            )

        # Export the audio
        Note16bit.save(audio, file_name)


if __name__ == "__main__":
    NODE = Note16bit
    NODE.NOTE_DURATION = 0.2
    SILENCE_DURATION = 0.1
    # NODE.test_range(silence_duration=SILENCE_DURATION)
    NODE.test_notes(silence_duration=SILENCE_DURATION)
    twinkle_music_list = [
        "C3", "C3", "G3", "G3", "A3", "A3", "G3", "MUTE",  # Twinkle, Twinkle Little Star
        "F3", "F3", "E3", "E3", "D3", "D3", "C3", "MUTE",  # How I Wonder What You Are
        "G3", "G3", "F3", "F3", "E3", "E3", "D3", "MUTE",  # Up Above The World So High
        "G3", "G3", "F3", "F3", "E3", "E3", "D3", "MUTE",  # Like a diamond in the sky
        "C3", "C3", "G3", "G3", "A3", "A3", "G3", "MUTE",  # Twinkle, Twinkle Little Star
        "F3", "F3", "E3", "E3", "D3", "D3", "C3", "MUTE",  # How I Wonder What You Are
    ]
    MUSIC = None
    for i in twinkle_music_list:
        MUSIC = NODE.add_note(MUSIC, i, 0.4)
        # MUSIC = NODE.add_note(MUSIC, "MUTE", 0.1)
    NODE.save(MUSIC, "twinkle_little_star.wav")

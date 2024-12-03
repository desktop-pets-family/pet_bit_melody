"""
    This script generates a range of 8 bit sounds
"""
import os
import sys
from typing import List, Union
from platform import system

# Audio generation libraries
import numpy as np
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME


def process_ffmpeg_path():
    """
    This function processes the path to the FFmpeg executable.
    """
    print("Adding local ff family binaries to path.")
    ffmpeg_base_path = os.path.join(
        "..", "..", "..", "server", "ff_family"
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

DEFAULT_MUTE: int = -1
DEFAULT_SAMPLE_RATE: int = 44100


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


DEBUG = True


class Notes:
    """_summary_
    This class generates 16-bit audio notes.

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    NOTE_DURATION = 1.0
    SAMPLE_RATE = 44100
    MAX_BIT_VALUE = 65535
    NOTE_EQUIVALENCE = {}
    MUTE = 1
    INNER_DISP: Disp = Disp(
        TOML_CONF,
        FILE_DESCRIPTOR,
        SAVE_TO_FILE,
        FILE_NAME,
        debug=DEBUG,
        logger="Notes"
    )

    def __init__(self, note: Union[List[int], int] = 80, duration: float = 3.0, amplitude: float = 0.5, sample_rate: int = 44100, base_track: Union[AudioSegment, None] = None, debug: bool = False) -> AudioSegment:
        if isinstance(note, list) is False:
            note = [note]
        self.note = note
        self.duration = duration
        self.amplitude = amplitude
        self.sample_rate = sample_rate
        self.base_track = base_track
        self.generated_bit_range = self.generate_bit_frequencies()
        self.debug = debug
        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )

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
            if item not in self.generated_bit_range:
                raise ValueError(
                    f"Frequency must be present in {self.generated_bit_range}."
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
    def generate_bit_frequencies() -> List[int]:
        """_summary_
            The function in charge of generating the 16 bit frequencies.

        Returns:
            List[int]: The list of the 16 bit frequencies.
        """
        return list(range(1, Notes.MAX_BIT_VALUE + 1))

    @staticmethod
    def get_available_notes() -> List[str]:
        """_summary_
        Get the available notes in the 16-bit range.

        Returns:
            Dict[str, int]: The available notes in the 16-bit range.
        """
        return list(Notes.NOTE_EQUIVALENCE)

    @staticmethod
    def create_smooth_transition(audio: AudioSegment, fade_duration: int = 10) -> AudioSegment:
        """
        Adds a fade-out effect to the audio to avoid abrupt transitions.

        Args:
            audio (AudioSegment): The audio to process.
            fade_duration (int): The duration of the fade-out in milliseconds.

        Returns:
            AudioSegment: The audio with a smooth fade-out.
        """
        return audio.fade_out(fade_duration)

    @staticmethod
    def create_silent_note(duration: float = 1.0, sample_rate: int = 44100) -> AudioSegment:
        """
        Create a silent note of the given duration.

        Args:
            duration (float, optional): The duration of the silence. Defaults to 1.0.
            sample_rate (int, optional): The sampling rate used. Defaults to 44100.

        Returns:
            AudioSegment: The silent note.
        """
        # Notes.create_smooth_transition()
        # Create a silent AudioSegment of the given duration
        silent_note = AudioSegment.silent(
            duration=duration * 1000,
            frame_rate=sample_rate
        )
        # duration in milliseconds
        return silent_note

    @staticmethod
    def create_note(frequency: Union[float, int, str] = 80, duration: float = 3.0, amplitude: float = 0.5, velocity: int = 100, sample_rate: int = 44100) -> AudioSegment:
        """
            Generates a single note as an AudioSegment.

        Args:
            frequency (float, int, str, optional): The frequency of the note to generate. Defaults to 80.
            duration (float, optional): The duration of that note. Defaults to 3.0.
            amplitude (float, optional): The amplitude of the note. Defaults to 0.5.
            velocity (int, optional): The velocity of the note. Defaults to 100.
            sample_rate (int, optional): The sample rate. Defaults to 44100.

        Returns:
            AudioSegment: A single note as an AudioSegment.
        """

        if isinstance(frequency, str):
            frequency = Notes.NOTE_EQUIVALENCE.get(frequency.upper())

        if frequency == Notes.MUTE or isinstance(frequency, str) and frequency.upper() == "MUTE":
            return Notes.create_silent_note(duration, sample_rate)

        if frequency is None or frequency <= 0 or frequency > Notes.MAX_BIT_VALUE:
            msg = "Frequency must be a note or between 0"
            msg += f" and {Notes.MAX_BIT_VALUE}."
            raise ValueError(msg)

        if duration < 0:
            raise ValueError("Duration must be greater than 0.")

        if amplitude < 0 or amplitude > 1:
            raise ValueError("Amplitude must be between 0 and 1.")

        if not (0 <= velocity <= 127):
            raise ValueError("Velocity must be between 0 and 127.")

        # Normalize velocity (0-127) to amplitude (0.0-1.0)
        amplitude = velocity / 127.0

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
    def add_note(base_audio: Union[AudioSegment, None] = None, frequency: Union[float, int, str] = 80, duration: float = 3.0, amplitude: float = 0.5, velocity: int = 100, sample_rate: int = 44100) -> AudioSegment:
        """_summary_
        Adds a note of a given frequency and duration to the audio sequence.

        Args:
            base_audio (Union[AudioSegment, None], optional): The existing audio segment to append the note to. Pass None to start a new sequence. Defaults to None.
            frequency (float, int, str, optional): The frequency of the note in Hz. Defaults to 80.
            duration (float, optional): The duration of the note in seconds. Defaults to 3.0.
            amplitude (float, optional): The amplitude of the note (0.0 to 1.0). Defaults to 0.5.
            velocity (int, optional): The velocity of the note (0 to 127). Defaults to
            sample_rate (int, optional): The sample rate for the audio. Defaults to 44100.

        Raises:
            ValueError: If the frequency is less than 0, the duration is less than 0, or the amplitude is not between 0 and 1.

        Returns:
            AudioSegment: The updated audio segment with the note added.
        """
        note_audio = Notes.create_note(
            frequency, duration, amplitude, velocity, sample_rate
        )
        return Notes.append_node(base_audio, note_audio)

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
        Notes.INNER_DISP.log_debug(f"Audio saved to {filename}")

    @staticmethod
    def test_range(file_name: str = "./bit_range.wav", silence_duration: float = 0.2) -> None:
        """_summary_
        This function tests the generation of the 8 bit range.

        Args:
            file_name (str, optional): The name of the file to save the audio to. Defaults to "./16bit_range.wav".
            silence_duration (float, optional): The duration of the silence between the notes. Defaults to 0.2.
        """
        # Generate the bit range
        generated_bit_range = Notes.generate_bit_frequencies()

        # Generate the audio
        audio = None
        for frequency in generated_bit_range:
            Notes.INNER_DISP.log_debug(
                f"Generating note for frequency {frequency}",
                "test_range"
            )
            audio = Notes.add_note(
                audio, frequency, Notes.NOTE_DURATION
            )
            audio = Notes.add_note(
                audio,
                Notes.MUTE,
                silence_duration
            )

        # Export the audio
        Notes.save(audio, file_name)

    @staticmethod
    def test_notes(file_name: str = "./notes.wav", silence_duration: float = 0.2) -> None:
        """_summary_
        This function tests the generation of a single note.

        Args:
            file_name (str, optional): The name of the file to save the audio to. Defaults to "./16bit_notes.wav".
            silence_duration (float, optional): The duration of the silence between the notes. Defaults to 0.2.
        """
        # Get the available notes
        notes = Notes.get_available_notes()

        audio = None
        for note in notes:
            Notes.INNER_DISP.log_debug(
                f"Generating note for {note}",
                "test_notes"
            )
            audio = Notes.add_note(audio, note, Notes.NOTE_DURATION)
            audio = Notes.add_note(
                audio,
                Notes.MUTE,
                silence_duration
            )

        # Export the audio
        Notes.save(audio, file_name)


if __name__ == "__main__":
    NODE = Notes
    NODE.MUTE = NoteEquivalencePiano.MUTE
    NODE.NOTE_EQUIVALENCE = NoteEquivalencePiano.NOTE_EQUIVALENCE
    NODE.NOTE_DURATION = 0.2
    SILENCE_DURATION = 0.1
    # NODE.test_range(silence_duration=SILENCE_DURATION)
    NODE.test_notes(
        file_name="notes_piano.wav",
        silence_duration=SILENCE_DURATION
    )
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
        NODE.INNER_DISP.log_debug(f"Adding note {i}", "__main__")
        MUSIC = NODE.add_note(MUSIC, i, 0.5, 0.4)
    NODE.save(MUSIC, "twinkle_little_star_piano.wav")

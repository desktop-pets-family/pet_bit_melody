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

try:
    from instrument_constants import NoteEquivalencePiano
except ImportError as e:
    raise Warning("Piano note equivalence not found.") from e


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
        debug=False,
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
    def create_silent_note(duration: float = 1.0, sample_rate: int = 44100) -> AudioSegment:
        # Create a silent AudioSegment of the given duration
        silent_note = AudioSegment.silent(
            duration=duration * 1000)
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

        if frequency is None or (frequency <= 0 or frequency > Notes.MAX_BIT_VALUE) and frequency != Notes.MUTE:
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
        MUSIC = NODE.add_note(MUSIC, i, 100, 0.4)
    NODE.save(MUSIC, "twinkle_little_star_piano.wav")

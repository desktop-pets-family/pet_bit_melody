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
    process_ffmpeg_path()
except ImportError:
    print("PyDub is not installed. Please install it using 'pip install pydub'.")
except Exception as e:
    print("An error occurred:", e)
    process_ffmpeg_path()


class NoteEquivalence8bit:
    """
    This class contains the equivalence of the notes in the 8-bit range.
    All frequencies are scaled to fit within the range of 31–255 Hz.
    """
    MUTE = 1

    # Notes in the 8-bit range
    C0 = 31
    CSH0 = 31
    D0 = 31
    DSH0 = 31
    E0 = 31
    F0 = 31
    FSH0 = 31
    G0 = 31
    GSH0 = 31
    A0 = 31
    ASH0 = 31
    B0 = 31
    C1 = 32
    CSH1 = 35
    D1 = 37
    DSH1 = 39
    E1 = 41
    F1 = 44
    FSH1 = 46
    G1 = 49
    GSH1 = 52
    A1 = 55
    ASH1 = 58
    B1 = 62
    C2 = 65
    CSH2 = 69
    D2 = 73
    DSH2 = 78
    E2 = 82
    F2 = 87
    FSH2 = 93
    G2 = 98
    GSH2 = 104
    A2 = 110
    ASH2 = 117
    B2 = 123
    C3 = 131
    CSH3 = 139
    D3 = 147
    DSH3 = 156
    E3 = 165
    F3 = 175
    FSH3 = 185
    G3 = 196
    GSH3 = 208
    A3 = 220
    ASH3 = 233
    B3 = 247

    # Frequencies above 255 Hz are clipped to the max 8-bit value
    C4 = 255
    CSH4 = 255
    D4 = 255
    DSH4 = 255
    E4 = 255
    F4 = 255
    FSH4 = 255
    G4 = 255
    GSH4 = 255
    A4 = 255
    ASH4 = 255
    B4 = 255

    # Dictionary of notes
    NOTE_EQUIVALENCE = {
        "MUTE": MUTE,
        "C0": C0, "CSH0": CSH0, "D0": D0, "DSH0": DSH0, "E0": E0, "F0": F0, "FSH0": FSH0, "G0": G0, "GSH0": GSH0, "A0": A0, "ASH0": ASH0, "B0": B0,
        "C1": C1, "CSH1": CSH1, "D1": D1, "DSH1": DSH1, "E1": E1, "F1": F1, "FSH1": FSH1, "G1": G1, "GSH1": GSH1, "A1": A1, "ASH1": ASH1, "B1": B1,
        "C2": C2, "CSH2": CSH2, "D2": D2, "DSH2": DSH2, "E2": E2, "F2": F2, "FSH2": FSH2, "G2": G2, "GSH2": GSH2, "A2": A2, "ASH2": ASH2, "B2": B2,
        "C3": C3, "CSH3": CSH3, "D3": D3, "DSH3": DSH3, "E3": E3, "F3": F3, "FSH3": FSH3, "G3": G3, "GSH3": GSH3, "A3": A3, "ASH3": ASH3, "B3": B3,
        "C4": C4, "CSH4": CSH4, "D4": D4, "DSH4": DSH4, "E4": E4, "F4": F4, "FSH4": FSH4, "G4": G4, "GSH4": GSH4, "A4": A4, "ASH4": ASH4, "B4": B4
    }


# The function that generates the 8 bit notes

class Note8bit(NoteEquivalence8bit):
    """_summary_
    This class generates 8-bit audio notes.

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    NOTE_DURATION = 1.0
    SAMPLE_RATE = 44100
    MAX_8BIT_VALUE = 255

    def __init__(self, note: Union[List[int], int] = 80, duration: float = 3.0, amplitude: float = 0.5, sample_rate: int = 44100, base_track: Union[AudioSegment, None] = None) -> AudioSegment:
        if isinstance(note, list) is False:
            note = [note]
        self.note = note
        self.duration = duration
        self.amplitude = amplitude
        self.sample_rate = sample_rate
        self.base_track = base_track
        self.eight_bit_range = self.generate_8bit_frequencies()
        self.eight_bit_frequencies = Note8bit.NOTE_EQUIVALENCE

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
        notes = note if isinstance(note, list) else [note]
        duration = duration or self.duration
        amplitude = amplitude or self.amplitude
        sample_rate = sample_rate or self.sample_rate
        base_audio = base_audio or self.base_track

        for current_note in notes:
            if current_note not in self.eight_bit_range:
                raise ValueError(
                    f"Frequency must be present in {self.eight_bit_range}."
                )
            base_audio = self.add_note(
                base_audio,
                current_note,
                self.duration,
                self.amplitude,
                self.sample_rate
            )
        return base_audio

    @staticmethod
    def generate_8bit_frequencies() -> List[int]:
        """_summary_
            The function in charge of generating the 8 bit frequencies.

        Returns:
            List[int]: The list of the 8 bit frequencies.
        """
        return list(range(1, 256))

    @staticmethod
    def get_available_notes() -> List[str]:
        """_summary_
        Get the available notes in the 8-bit range.

        Returns:
            Dict[str, int]: The available notes in the 8-bit range.
        """
        return list(Note8bit.NOTE_EQUIVALENCE)

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
            frequency = Note8bit.NOTE_EQUIVALENCE.get(frequency.upper())

        if frequency is None or frequency <= 0 or frequency > Note8bit.MAX_8BIT_VALUE:
            raise ValueError("Frequency must be a note or greater than 0.")

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
        note_audio = Note8bit.create_note(
            frequency, duration, amplitude, sample_rate
        )
        return Note8bit.append_node(base_audio, note_audio)

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
    def test_range(file_name: str = "./8bit_range.wav", silence_duration: float = 0.2) -> None:
        """_summary_
        This function tests the generation of the 8 bit range.

        Args:
            file_name (str, optional): The name of the file to save the audio to. Defaults to "./8bit_range.wav".
            silence_duration (float, optional): The duration of the silence between the notes. Defaults to 0.2.
        """
        # Generate the 8 bit range
        eight_bit_range = Note8bit.generate_8bit_frequencies()

        # Generate the audio
        audio = None
        for frequency in eight_bit_range:
            print(f"Generating note for frequency {frequency}")
            audio = Note8bit.add_note(audio, frequency, Note8bit.NOTE_DURATION)
            audio = Note8bit.add_note(
                audio,
                Note8bit.MUTE,
                silence_duration
            )

        # Export the audio
        Note8bit.save(audio, file_name)

    @staticmethod
    def test_notes(file_name: str = "./8bit_notes.wav", silence_duration: float = 0.2) -> None:
        """_summary_
        This function tests the generation of a single note.

        Args:
            file_name (str, optional): The name of the file to save the audio to. Defaults to "./8bit_notes.wav".
            silence_duration (float, optional): The duration of the silence between the notes. Defaults to 0.2.
        """
        # Get the available notes
        notes = Note8bit.get_available_notes()

        audio = None
        for note in notes:
            print(f"Generating note for {note}")
            audio = Note8bit.add_note(audio, note, Note8bit.NOTE_DURATION)
            audio = Note8bit.add_note(
                audio,
                Note8bit.MUTE,
                silence_duration
            )

        # Export the audio
        Note8bit.save(audio, file_name)


if __name__ == "__main__":
    NODE = Note8bit
    NODE.NOTE_DURATION = 0.2
    SILENCE_DURATION = 0.1
    NODE.test_range(silence_duration=SILENCE_DURATION)
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

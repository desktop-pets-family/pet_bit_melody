"""
    This script generates a 80 Hz sine wave using PyDub and saves it to a WAV file.
"""
import os
import sys
from platform import system
import numpy as np


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


try:
    from pydub import AudioSegment
    from pydub import playback
    process_ffmpeg_path()
except ImportError:
    print("PyDub is not installed. Please install it using 'pip install pydub'.")
except Exception as e:
    print("An error occurred:", e)
    process_ffmpeg_path()


# Parameters
FREQUENCY = 80  # FREQUENCY in Hz
DURATION = 3.0  # Duration in seconds
SAMPLE_RATE = 44100  # Samples per second (standard for audio)

# Generate the samples for the sine wave
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
# 0.5 to keep volume manageable
waveform = 0.5 * np.sin(2 * np.pi * FREQUENCY * t)

# Convert to 16-bit PCM (required by PyDub)
waveform_integers = np.int16(waveform * 32767)

# Create an AudioSegment from the waveform
audio_segment = AudioSegment(
    waveform_integers.tobytes(),  # raw audio data
    frame_rate=SAMPLE_RATE,
    sample_width=waveform_integers.dtype.itemsize,
    channels=1
)

# Export or play the audio
audio_segment.export("80Hz_sine_wave.wav", format="wav")  # To save to a file
print("80 Hz sine wave saved to '80Hz_sine_wave.wav'.")
playback.play(audio_segment)  # To play the sound

"""
This module is the main entry point for the ffmpeg family of tools.
"""

from .downloader import FFMPEGDownloader

if __name__ == "__main__":
    FDI = FFMPEGDownloader()
    FDI.main()
    AUDIO_WAVE = 440
    AUDIO_SAMPLE_PATH = f"./{AUDIO_WAVE}.wav"
    AUDIO_SAMPLE = FDI.generate_audio_sample(AUDIO_WAVE)
    FDI.save_audio_sample(AUDIO_SAMPLE, AUDIO_SAMPLE_PATH)
    FDI.play_audio_sample(AUDIO_SAMPLE)

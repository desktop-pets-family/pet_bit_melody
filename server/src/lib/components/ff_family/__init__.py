"""
    File in charge of relaying the components for downloading the ffmpeg library to the server class so that they can be imported.
"""
import os
from .downloader import ArchitectureNotSupported, PackageNotInstalled, PackageNotSupported, FFMPEG_KEY, FFPROBE_KEY, FFPLAY_KEY, WINDOWS_KEY, LINUX_KEY, MAC_KEY, FILE_PATH_TOKEN, FILE_URL_TOKEN, QUERY_TIMEOUT, CWD, BUNDLE_DOWNLOAD, FFFamilyDownloader, AudioSegment


class FFFamily:
    """
    This class is used to import the components for downloading the ff* libraries to the server class.
    """
    ArchitectureNotSupported = ArchitectureNotSupported
    PackageNotInstalled = PackageNotInstalled
    PackageNotSupported = PackageNotSupported
    FFMPEG_KEY = FFMPEG_KEY
    FFPROBE_KEY = FFPROBE_KEY
    FFPLAY_KEY = FFPLAY_KEY
    WINDOWS_KEY = WINDOWS_KEY
    LINUX_KEY = LINUX_KEY
    MAC_KEY = MAC_KEY
    FILE_PATH_TOKEN = FILE_PATH_TOKEN
    FILE_URL_TOKEN = FILE_URL_TOKEN
    QUERY_TIMEOUT = QUERY_TIMEOUT
    CWD = CWD
    BUNDLE_DOWNLOAD = BUNDLE_DOWNLOAD
    FFMPEGDownloader = FFFamilyDownloader

    @staticmethod
    def download(cwd: str = os.getcwd(), query_timeout: int = 10, success: int = 0, error: int = 84, debug: bool = False, audio_segment_node: AudioSegment = None) -> int:
        """
        This method is used to download the ff* libraries.
        """
        node = FFFamilyDownloader(
            cwd,
            query_timeout,
            success,
            error,
            debug
        )
        return node(audio_segment_node)


__all__ = [
    'ArchitectureNotSupported',
    'PackageNotInstalled',
    'PackageNotSupported',
    'FFMPEG_KEY',
    'FFPROBE_KEY',
    'FFPLAY_KEY',
    'WINDOWS_KEY',
    'LINUX_KEY',
    'MAC_KEY',
    'FILE_PATH_TOKEN',
    'FILE_URL_TOKEN',
    'QUERY_TIMEOUT',
    'CWD',
    'BUNDLE_DOWNLOAD',
    'FFFamilyDownloader',
    'FFFamily'
]

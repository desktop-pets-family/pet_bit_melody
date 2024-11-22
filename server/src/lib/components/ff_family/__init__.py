"""
    File in charge of relaying the components for downloading the ffmpeg library to the server class so that they can be imported.
"""

from .downloader import ArchitectureNotSupported, PackageNotInstalled, PackageNotSupported, FFMPEG_KEY, FFPROBE_KEY, FFPLAY_KEY, WINDOWS_KEY, LINUX_KEY, MAC_KEY, FILE_PATH_TOKEN, FILE_URL_TOKEN, QUERY_TIMEOUT, CWD, BUNDLE_DOWNLOAD, FFMPEGDownloader


class ff_family:
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
    FFMPEGDownloader = FFMPEGDownloader


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
    'FFMPEGDownloader',
    'ff_family'
]

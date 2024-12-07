"""
    File in charge of relaying the components for downloading the ffmpeg library to the server class so that they can be imported.
"""
import os
from typing import Dict, Union
from .downloader import ArchitectureNotSupported, PackageNotInstalled, PackageNotSupported, FFMPEG_KEY, FFPROBE_KEY, FFPLAY_KEY, WINDOWS_KEY, LINUX_KEY, MAC_KEY, FILE_PATH_TOKEN, FILE_URL_TOKEN, QUERY_TIMEOUT, CWD, BUNDLE_DOWNLOAD, FF_FAMILY_DISP, FFFamilyDownloader, AudioSegment


class FFFamily:
    """
    This class is used to import the components for downloading the ff* libraries to the server class.
    """

    def __init__(self, cwd: str = os.getcwd(), query_timeout: int = 10, success: int = 0, error: int = 84, debug: bool = False, bundle_download: Union[Dict[str, Dict[str, Dict[str, Dict[str, str]]]], None] = None) -> None:
        self.cwd: str = CWD
        self.mac_key: str = MAC_KEY
        self.linux_key: str = LINUX_KEY
        self.ffmpeg_key: str = FFMPEG_KEY
        self.ffplay_key: str = FFPLAY_KEY
        self.ffprobe_key: str = FFPROBE_KEY
        self.windows_key: str = WINDOWS_KEY
        self.ff_family_disp = FF_FAMILY_DISP
        self.bundle_download = BUNDLE_DOWNLOAD
        self.query_timeout: int = QUERY_TIMEOUT
        self.file_url_token: str = FILE_URL_TOKEN
        self.file_path_token: str = FILE_PATH_TOKEN
        self.package_not_installed: PackageNotInstalled = PackageNotInstalled
        self.package_not_supported: PackageNotSupported = PackageNotSupported
        self.architecture_not_supported: ArchitectureNotSupported = ArchitectureNotSupported
        if debug:
            FF_FAMILY_DISP.debug = debug
            self.ff_family_disp.debug = debug
        self.ff_family_downloader: FFFamilyDownloader = FFFamilyDownloader
        node: Dict[str, Dict[str, Dict[str, Dict[str, str]]]] = BUNDLE_DOWNLOAD
        if bundle_download is not None and isinstance(bundle_download, dict):
            node = bundle_download
        self.ff_family_downloader_initialised: FFFamilyDownloader = FFFamilyDownloader(
            cwd=cwd,
            query_timeout=query_timeout,
            success=success,
            error=error,
            bundle_download=node,
            debug=debug
        )

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
            BUNDLE_DOWNLOAD,
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

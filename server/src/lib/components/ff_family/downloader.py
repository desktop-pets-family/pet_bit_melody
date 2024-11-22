"""
File in charge of downloading and extracting the FFmpeg binaries for the current system.

Raises:
    ArchitectureNotSupported: _description_
    PackageNotSupported: _description_
    PackageNotInstalled: _description_
    NotImplementedError: _description_
    ValueError: _description_
    PackageNotSupported: _description_
    PackageNotInstalled: _description_
"""
import os
import sys
import math
import struct
import shutil
import zipfile
import tarfile
import platform
import requests
from pydub import AudioSegment, playback

from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME


class ArchitectureNotSupported(Exception):
    """
    Exception raised when the current system architecture is not supported.

    Args:
        Exception (Exception): The base exception class.
    """


class PackageNotInstalled(Exception):
    """
    Exception raised when the package is not installed.

    Args:
        Exception (Exception): The base exception class.
    """


class PackageNotSupported(Exception):
    """
    Exception raised when the package is not supported.

    Args:
        Exception (Exception): The base exception class.
    """


# Function to extract files based on archive type

FFMPEG_KEY = "ffmpeg"
FFPROBE_KEY = "ffprobe"
FFPLAY_KEY = "ffplay"

WINDOWS_KEY = "windows"
LINUX_KEY = "linux"
MAC_KEY = "darwin"

FILE_URL_TOKEN = "file_url"
FILE_PATH_TOKEN = "file_path"
QUERY_TIMEOUT = 10

CWD = os.getcwd()

BUNDLE_DOWNLOAD = {
    FFMPEG_KEY: {
        WINDOWS_KEY: {
            "i686": {
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.zip",  # 32-bit Windows
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "windows", "ffmpeg-release-i686-static.zip"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-x86_64-static.zip",  # 64-bit Windows
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "windows", "ffmpeg-release-x86_64-static.zip"
                )
            }
        },
        LINUX_KEY: {
            "i686": {
                # 32-bit Linux (x86)
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffmpeg-release-i686-static.tar.xz"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz",  # 64-bit Linux
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffmpeg-release-x86_64-static.tar.xz"
                )
            },
            "arm64": {
                # 64-bit Linux (arm64)
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-arm64-static.tar.xz",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffprobe-release-arm64-static.tar.xz"
                )
            }
        },
        MAC_KEY: {
            "i686": {
                FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/get/zip",  # 32-bit macOS
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffmpeg-latest.zip"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/get/zip",  # 64-bit macOS
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffmpeg-latest-amd64.zip"
                )
            },
            "arm64": {
                # 64-bit macOS (arm64),
                FILE_URL_TOKEN: "https://ffmpeg.martin-riedl.de/redirect/latest/macos/arm64/release/ffmpeg.zip",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffmpeg-latest-arm64.zip"
                )
            }
        },
    },
    FFPROBE_KEY: {
        WINDOWS_KEY: {
            "i686": {
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.zip",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "windows", "ffprobe-release-i686-static.zip"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-x86_64-static.zip",  # 64-bit Windows
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "windows", "ffprobe-release-x86_64-static.zip"
                )
            }
        },
        LINUX_KEY: {
            "i686": {
                # 32-bit Linux (x86)
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffprobe-release-i686-static.tar.xz"
                )
            },
            "64": {
                # 64-bit Linux
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffprobe_x64.tar.xz"
                )
            },
            "arm64": {
                # 64-bit Linux (arm 64)
                FILE_URL_TOKEN: "https://ffmpeg.martin-riedl.de/redirect/latest/linux/arm64/release/ffprobe.zip",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffprobe_arm64.zip"
                )
            },
        },
        MAC_KEY: {
            "i686": {
                FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/getrelease/ffprobe/zip",  # 32-bit macOS
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffprobe-latest.zip"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/getrelease/ffprobe/zip",  # 64-bit macOS
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffprobe-latest-amd64.zip"
                )
            },
            "arm64": {
                # 64-bit macOS (arm64),
                FILE_URL_TOKEN: "https://ffmpeg.martin-riedl.de/redirect/latest/macos/arm64/release/ffprobe.zip",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffprobe-latest-arm64.zip"
                )
            }
        },
    },
    FFPLAY_KEY: {
        WINDOWS_KEY: {
            "i686": {
                FILE_URL_TOKEN: "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n4.4-32bit-static.zip",  # 32-bit Windows
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "windows", "ffplay-release-i686-static.zip"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-x86_64-static.zip",  # 64-bit Windows
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "windows", "ffplay-release-x86_64-static.zip"
                )
            }
        },
        LINUX_KEY: {
            "i686": {
                # 32-bit Linux (x86)
                FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffplay-release-i686-static.tar.xz"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://ffmpeg.martin-riedl.de/redirect/latest/linux/amd64/release/ffplay.zip",  # 64-bit Linux
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffplay-latest-amd64.zip"
                )
            },
            "arm64": {
                FILE_URL_TOKEN: "https://ffmpeg.martin-riedl.de/redirect/latest/linux/arm64/release/ffplay.zip",  # 64-bit Linux
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "linux", "ffplay-latest-arm64.zip"
                )
            }
        },
        MAC_KEY: {
            "i686": {
                FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/getrelease/ffplay/zip",  # 32-bit macOS
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffplay-latest.zip"
                )
            },
            "64": {
                FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/getrelease/ffplay/zip",  # 64-bit macOS
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffplay-latest.zip"
                )
            },
            "arm64": {
                # 64-bit macOS (arm64)
                FILE_URL_TOKEN: "https://ffmpeg.martin-riedl.de/redirect/latest/macos/arm64/release/ffplay.zip",
                FILE_PATH_TOKEN: os.path.join(
                    CWD, "downloads", "macos", "ffplay-latest-arm64.zip"
                )
            }
        }
    }
}

# ------------------------ The logging function ------------------------
FF_FAMILY_DISP: Disp = Disp(
    TOML_CONF,
    FILE_DESCRIPTOR,
    SAVE_TO_FILE,
    FILE_NAME,
    debug=False,
    logger="FF_FAMILY"
)


class FFFamilyDownloader:
    """
        The class in charge of downloading and extracting the FFmpeg binaries for the current system.
        This class is there so that ffmpeg (and it's familly binaries) ca be run without requiring the user to install it.

    Raises:
        NotImplementedError: _description_
        ValueError: _description_
        ArchitectureNotSupported: _description_
        PackageNotSupported: _description_
        PackageNotInstalled: _description_
        PackageNotSupported: _description_
        PackageNotSupported: _description_
        PackageNotInstalled: _description_
        RuntimeError: _description_
    """

    available_binaries: list = [FFMPEG_KEY, FFPROBE_KEY, FFPLAY_KEY]

    def __init__(self, cwd: str = os.getcwd(), query_timeout: int = 10, success: int = 0, error: int = 84, debug: bool = False):
        self.cwd: str = cwd
        self.error: int = error
        self.debug: bool = debug
        self.success: int = success
        self.file_url: str = None
        self.file_path: str = None
        self.fold_path: str = None
        self.query_timeout: int = query_timeout
        self.new_folder_path: str = None
        self.extracted_folder: str = None
        self.system: str = self.get_system_name()
        self.architecture: str = self.get_platform()
        self.available_binaries: list = FFFamilyDownloader.available_binaries
        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    @staticmethod
    def generate_audio_sample(tone: int) -> AudioSegment:
        """
        Generates a pure tone audio sample using the pydub library.

        Args:
            tone (int): Frequency of the tone in Hz.

        Returns:
            AudioSegment: The generated audio segment.
        """
        title = "generate_audio_sample"
        FF_FAMILY_DISP.log_debug(
            f"Generating audio sample for tone {tone} Hz",
            title
        )
        sample_rate = 44100  # Hz
        frequency = tone  # Hz
        duration = 3.0  # seconds

        # Generate samples manually
        num_samples = int(sample_rate * duration)
        samples = []
        for i in range(num_samples):
            t = i / sample_rate
            # Generate a sine wave
            sample_value = 0.5 * math.sin(2 * math.pi * frequency * t)
            # Convert to 16-bit integer
            waveform_integer = int(sample_value * 32767)
            samples.append(waveform_integer)

        # Pack the waveform integers into a byte array
        raw_audio_data = struct.pack("<" + "h" * len(samples), *samples)

        # Create the AudioSegment
        audio_segment = AudioSegment(
            raw_audio_data,
            frame_rate=sample_rate,
            sample_width=2,  # 16-bit audio is 2 bytes
            channels=1  # Mono audio
        )
        FF_FAMILY_DISP.log_debug("Audio sample generated", title)
        return audio_segment

    @staticmethod
    def play_audio_sample(audio_segment: AudioSegment) -> None:
        """
        Plays an audio sample using the pydub library.

        Args:
            audio_segment (AudioSegment): The audio segment to play.
        """
        title = "play_audio_sample"
        FF_FAMILY_DISP.log_debug("Playing audio sample", title)
        playback.play(audio_segment)
        FF_FAMILY_DISP.log_debug("Audio sample played", title)

    @staticmethod
    def save_audio_sample(audio_segment: AudioSegment, file_path: str) -> None:
        """
            Saves an audio sample to a file using the pydub library.

        Args:
            audio_segment (AudioSegment): _description_
            file_path (str): _description_

        Returns:
            _type_: _description_
        """
        title = "save_audio_sample"
        FF_FAMILY_DISP.log_debug(f"Saving audio sample to {file_path}", title)
        audio_segment.export(file_path, format="wav")
        FF_FAMILY_DISP.log_debug(f"Audio sample saved to {file_path}", title)

    @staticmethod
    def _extract_package(file_path: str, destination: str) -> None:
        """
            Extracts a package from a file using different unpacking libraries.

        Args:
            file_path (_type_): _description_
            destination (_type_): _description_

        Raises:
            NotImplementedError: _description_
            ValueError: _description_
        """
        title = "_extract_package"
        FF_FAMILY_DISP.log_debug(
            f"Extracting {file_path} to {destination}",
            title
        )
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(destination)
        elif file_path.endswith(".tar.xz"):
            with tarfile.open(file_path, 'r:xz') as tar_ref:
                tar_ref.extractall(destination)
        elif file_path.endswith(".7z"):
            # Handling 7z files
            raise NotImplementedError("7z extraction not implemented")
        else:
            raise ValueError("Unsupported file format")
        FF_FAMILY_DISP.log_debug("Extraction complete", title)

    @staticmethod
    def get_system_name() -> str:
        """
            Get the name of the current system.

        Returns:
            str: _description_
        """
        return platform.system().lower()

    @staticmethod
    def get_platform() -> str:
        """
            Get the platform of the current system.

        Returns:
            str: _description_
        """
        return platform.architecture()[0]

    @staticmethod
    def _create_path_if_not_exists(path: str) -> None:
        """
        Create a directory if it does not exist.

        Args:
            path (str): The path to create.

        """
        title = "_create_path_if_not_exists"
        if not os.path.exists(path):
            FF_FAMILY_DISP.log_debug(f"Creating directory: {path}", title)
            os.makedirs(path, exist_ok=True)

    @staticmethod
    def _download_file(file_url: str, file_path: str, query_timeout: int = 10) -> None:
        """
        Download a file from a URL.

        Args:
            file_url (str): The URL of the file to download.
            file_path (str): The path to save the downloaded file.
            query_timeout (int, optional): The timeout for the query. Defaults to 10.

        Raises:
            PackageNotInstalled: If the package could not be downloaded.
        """
        title = "_download_file"
        FF_FAMILY_DISP.log_info(f"Downloading FFmpeg from {file_url}", title)
        response_data = requests.get(file_url, timeout=query_timeout)
        if response_data.status_code != 200:
            FF_FAMILY_DISP.log_error(
                "Failed to download FFmpeg." +
                f"Status code: {response_data.status_code}",
                title
            )
            raise PackageNotInstalled("Could not download the package")
        FF_FAMILY_DISP.log_info(f"Saving to {file_path}", title)
        with open(file_path, "wb") as file_descriptor:
            file_descriptor.write(response_data.content)
        FF_FAMILY_DISP.log_info("Download complete", title)

    @staticmethod
    def _grant_executable_rights(file_path: str = None) -> None:
        """
        Grant executable rights to a file

        Args:
            file_path (str, optional): The path to the file. Defaults to None.
        """
        title = "_grant_executable_rights"
        if file_path is None:
            return
        FF_FAMILY_DISP.log_debug(
            f"Giving executable rights to {file_path}",
            title
        )
        if os.path.exists(file_path):
            os.chmod(file_path, 0o755)
            FF_FAMILY_DISP.log_debug(
                f"Executable rights granted to {file_path}",
                title
            )
        else:
            FF_FAMILY_DISP.log_error(
                f"{file_path} does not exist, could not grant executable rights",
                title
            )

    @staticmethod
    def _rename_extracted_folder(old_name: str, new_name: str) -> None:
        """
        Rename an extracted folder.

        Args:
            old_name (str): The old name of the folder.
            new_name (str): The new name of the folder.
        """
        title = "_rename_extracted_folder"
        if os.path.exists(old_name):
            FF_FAMILY_DISP.log_debug(
                f"Renaming {old_name} to {new_name}", title
            )
            shutil.move(old_name, new_name)

    @staticmethod
    def get_ff_family_path(download_if_not_present: bool = True, cwd: str = os.getcwd(), query_timeout: int = 10,  success: int = 0, error: int = 1, debug: bool = False) -> str:
        """
            The general path for ff related libraries

        Args:
            download_if_not_present (bool, optional): Download the binary if it is not found. Defaults to True.
            cwd (str, optional): The current working directory. Defaults to os.getcwd().
            query_timeout (int, optional): The time before a package is considered lost. Defaults to 10.
            success (int, optional): The success status. Defaults to 0.
            error (int, optional): The error status. Defaults to 1.
            debug (bool, optional): The debug variable. Defaults to False.

        Raises:
            PackageNotSupported: Unsupported system
            PackageNotInstalled: FF_family not found
            ArchitectureNotSupported: Unsupported architecture
            PackageNotSupported: Unsupported system
            RuntimeError: FF_family could not be installed

        Returns:
            str: The path to the FF family.
        """
        system = FFFamilyDownloader.get_system_name()
        if system not in ("windows", "linux", "darwin"):
            raise PackageNotSupported("Unsupported system")
        precompiled_ffmpeg = os.path.join(cwd, "ffmpeg", system)
        precompiled_ffprobe = os.path.join(cwd, "ffprobe", system)
        precompiled_ffplay = os.path.join(cwd, "ffplay", system)
        if not os.path.isdir(precompiled_ffmpeg) or not os.path.isdir(precompiled_ffprobe) or not os.path.isdir(precompiled_ffplay):
            if not download_if_not_present:
                raise PackageNotInstalled("FF_family not found")
            print("FF_family not found in precompiled paths, setting up")
            fdi = FFFamilyDownloader(
                cwd=cwd,
                query_timeout=query_timeout,
                success=success,
                error=error,
                debug=debug
            )
            status = fdi.main()
            if status != 0:
                raise RuntimeError("FF_family could not be installed")
        if os.path.exists(cwd) and os.path.isdir(cwd):
            return cwd
        raise PackageNotInstalled("FF_family not found")

    @staticmethod
    def get_ffmpeg_binary_path(download_if_not_present: bool = True, cwd: str = os.getcwd(), query_timeout: int = 10,  success: int = 0, error: int = 1, debug: bool = False) -> str:
        """
        Get the path to the FFmpeg binary.

        Args:
            download_if_not_present (bool, optional): Download the binary if it is not found. Defaults to True.
            cwd (str, optional): The current working directory. Defaults to os.getcwd().
            query_timeout (int, optional): The time before a package is considered lost. Defaults to 10.
            success (int, optional): The success status. Defaults to 0.
            error (int, optional): The error status. Defaults to 1.
            debug (bool, optional): The debug variable. Defaults to False.

        Raises:
            PackageNotSupported: Unsupported system
            PackageNotInstalled: FF_family not found
            ArchitectureNotSupported: Unsupported architecture
            PackageNotSupported: Unsupported system
            RuntimeError: FF_family could not be installed

        Returns:
            str: The path to the FF family.
        """
        system = FFFamilyDownloader.get_system_name()
        ffmpeg_system_path = FFFamilyDownloader.get_ff_family_path(
            download_if_not_present=download_if_not_present,
            cwd=cwd,
            query_timeout=query_timeout,
            success=success,
            error=error,
            debug=debug
        )
        ffmpeg_precompiled_path = os.path.join(
            ffmpeg_system_path, "ffmpeg", system
        )
        path = None
        if system == "windows":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffmpeg.exe"
            )
        elif system == "linux":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffmpeg"
            )
            FFFamilyDownloader._grant_executable_rights(path)
        elif system == "darwin":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffmpeg"
            )
            FFFamilyDownloader._grant_executable_rights(path)
        else:
            raise PackageNotSupported("Unsupported OS")
        FF_FAMILY_DISP.log_debug(
            f"FFmpeg path = '{path}'",
            "get_ffmpeg_binary_path"
        )
        if os.path.exists(path):
            if os.path.isfile(path):
                return path
            raise PackageNotSupported("Path is not a file")
        raise PackageNotInstalled("ffmpeg is not properly installed")

    @staticmethod
    def get_ffplay_binary_path(download_if_not_present: bool = True, cwd: str = os.getcwd(), query_timeout: int = 10,  success: int = 0, error: int = 1, debug: bool = False) -> str:
        """
        Get the path to the FFplay binary.

        Args:
            download_if_not_present (bool, optional): Download the binary if it is not found. Defaults to True.
            cwd (str, optional): The current working directory. Defaults to os.getcwd().
            query_timeout (int, optional): The time before a package is considered lost. Defaults to 10.
            success (int, optional): The success status. Defaults to 0.
            error (int, optional): The error status. Defaults to 1.
            debug (bool, optional): The debug variable. Defaults to False.

        Raises:
            PackageNotSupported: Unsupported system
            PackageNotInstalled: FF_family not found
            ArchitectureNotSupported: Unsupported architecture
            PackageNotSupported: Unsupported system
            RuntimeError: FF_family could not be installed

        Returns:
            str: The path to the FF family.
        """
        system = FFFamilyDownloader.get_system_name()
        ffmpeg_system_path = FFFamilyDownloader.get_ff_family_path(
            download_if_not_present=download_if_not_present,
            cwd=cwd,
            query_timeout=query_timeout,
            success=success,
            error=error,
            debug=debug
        )
        ffmpeg_precompiled_path = os.path.join(
            ffmpeg_system_path, "ffplay", system
        )
        path = None
        if system == "windows":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffplay.exe"
            )
        elif system == "linux":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffplay"
            )
            FFFamilyDownloader._grant_executable_rights(path)
        elif system == "darwin":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffplay"
            )
            FFFamilyDownloader._grant_executable_rights(path)
        else:
            raise PackageNotSupported("Unsupported OS")
        FF_FAMILY_DISP.log_debug(
            f"FFplay path = '{path}'",
            "get_ffplay_binary_path"
        )
        if os.path.exists(path):
            if os.path.isfile(path):
                return path
            raise PackageNotSupported("Path is not a file")
        raise PackageNotInstalled("ffplay is not properly installed")

    @staticmethod
    def get_ffprobe_binary_path(download_if_not_present: bool = True, cwd: str = os.getcwd(), query_timeout: int = 10,  success: int = 0, error: int = 1, debug: bool = False) -> str:
        """
        Get the path to the ffprobe binary.

        Args:
            download_if_not_present (bool, optional): Download the binary if it is not found. Defaults to True.
            cwd (str, optional): The current working directory. Defaults to os.getcwd().
            query_timeout (int, optional): The time before a package is considered lost. Defaults to 10.
            success (int, optional): The success status. Defaults to 0.
            error (int, optional): The error status. Defaults to 1.
            debug (bool, optional): The debug variable. Defaults to False.

        Raises:
            PackageNotSupported: Unsupported system
            PackageNotInstalled: FF_family not found
            ArchitectureNotSupported: Unsupported architecture
            PackageNotSupported: Unsupported system
            RuntimeError: FF_family could not be installed

        Returns:
            str: The path to the FF family.
        """
        system = FFFamilyDownloader.get_system_name()
        ffmpeg_system_path = FFFamilyDownloader.get_ff_family_path(
            download_if_not_present=download_if_not_present,
            cwd=cwd,
            query_timeout=query_timeout,
            success=success,
            error=error,
            debug=debug
        )
        ffmpeg_precompiled_path = os.path.join(
            ffmpeg_system_path, "ffprobe", system
        )
        path = None
        if system == "windows":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffprobe.exe"
            )
        elif system == "linux":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffprobe"
            )
            FFFamilyDownloader._grant_executable_rights(path)
        elif system == "darwin":
            path = os.path.join(
                ffmpeg_precompiled_path,
                "ffprobe"
            )
            FFFamilyDownloader._grant_executable_rights(path)
        else:
            raise PackageNotSupported("Unsupported OS")
        FF_FAMILY_DISP.log_debug(
            f"FFprobe path = '{path}'",
            "get_ffprobe_binary_path"
        )
        if os.path.exists(path):
            if os.path.isfile(path):
                return path
            raise PackageNotSupported("Path is not a file")
        raise PackageNotInstalled("ffprobe is not properly installed")

    @staticmethod
    def add_ff_family_to_path(ffmpeg_path: str = None, ffplay_path: str = None, ffprobe_path: str = None, download_if_not_present: bool = True, cwd: str = os.getcwd(), query_timeout: int = 10,  success: int = 0, error: int = 1, debug: bool = False) -> None:
        """_summary_
            Add the FF family to the system path.

        Args:
            ffmpeg_path (str, optional): The path to the ffmpeg library. Defaults to None.
            ffplay_path (str, optional): The path to the ffplay library. Defaults to None.
            ffprobe_path (str, optional): The path to the ffprobe library. Defaults to None.
            download_if_not_present (bool, optional): _description_. Defaults to True.
            cwd (str, optional): The current working directory. Defaults to os.getcwd().
            query_timeout (int, optional): The delay before a paquet is considered invalid. Defaults to 10.
            success (int, optional): The default success status. Defaults to 0.
            error (int, optional): The default error status. Defaults to 1.
            debug (bool, optional): If to activate debug or not. Defaults to False.
        """
        title = "add_ff_family_to_path"
        if ffmpeg_path is None:
            FF_FAMILY_DISP.log_debug("Getting ffmpeg path", title)
            ffmpeg_path = FFFamilyDownloader.get_ffmpeg_binary_path(
                download_if_not_present=download_if_not_present,
                cwd=cwd,
                query_timeout=query_timeout,
                success=success,
                error=error,
                debug=debug
            )
        if ffplay_path is None:
            FF_FAMILY_DISP.log_debug("Getting ffplay path", title)
            ffplay_path = FFFamilyDownloader.get_ffplay_binary_path(
                download_if_not_present=download_if_not_present,
                cwd=cwd,
                query_timeout=query_timeout,
                success=success,
                error=error,
                debug=debug
            )
        if ffprobe_path is None:
            FF_FAMILY_DISP.log_debug("Getting ffprobe path", title)
            ffprobe_path = FFFamilyDownloader.get_ffprobe_binary_path(
                download_if_not_present=download_if_not_present,
                cwd=cwd,
                query_timeout=query_timeout,
                success=success,
                error=error,
                debug=debug
            )
        msg = "Converting the direct paths (which include the binaries at the end) into system paths (which only include the directories containing the binaries)"
        FF_FAMILY_DISP.log_debug(msg, title)
        ffmpeg_path = os.path.dirname(ffmpeg_path)
        ffplay_path = os.path.dirname(ffplay_path)
        ffprobe_path = os.path.dirname(ffprobe_path)
        FF_FAMILY_DISP.log_debug("Adding FF family to PATH", title)
        for ff_path in [ffmpeg_path, ffplay_path, ffprobe_path]:
            if ff_path not in os.environ["PATH"]:
                FF_FAMILY_DISP.log_debug(f"Adding {ff_path} to PATH", title)
                os.environ["PATH"] = ff_path + os.pathsep + os.environ["PATH"]
                FF_FAMILY_DISP.log_debug(f"Added {ff_path} to PATH", title)
            else:
                FF_FAMILY_DISP.log_debug(
                    f"{ff_path} is already in PATH", title
                )
            if ff_path not in sys.path:
                FF_FAMILY_DISP.log_debug(
                    f"Adding {ff_path} to sys.path", title
                )
                sys.path.append(ff_path)
                FF_FAMILY_DISP.log_debug(f"Added {ff_path} to sys.path", title)
            else:
                FF_FAMILY_DISP.log_debug(
                    f"{ff_path} is already in sys.path", title
                )

    def _clean_platform_name(self) -> None:
        """
        Clean the platform name to remove any unnecessary characters.
        """
        title = "_clean_platform_name"
        msg = "Current system (before filtering): "
        msg += f"{self.system} {self.architecture}"
        self.disp.log_debug(msg, title)

        if "bit" in self.architecture:
            self.architecture = self.architecture.replace("bit", "")
        elif "x" in self.architecture:
            self.architecture = self.architecture.replace("x", "")

        msg = "Current system (after filtering): "
        msg += f"{self.system} {self.architecture}"
        self.disp.log_debug(msg, title)

    def _get_correct_download_and_file_path(self, binary_name: str = FFMPEG_KEY) -> None:
        """
        Get the correct download and file path for the binary.

        Args:
            binary_name (str, optional): The name of the binary to download. Defaults to FFMPEG_KEY.

        Raises:
            PackageNotSupported: Unknown binary choice
            ArchitectureNotSupported: Unknown architecture
            PackageNotSupported: Unknown system
        """
        if binary_name not in BUNDLE_DOWNLOAD:
            raise PackageNotSupported("Unknown binary choice" + binary_name)
        if self.system in BUNDLE_DOWNLOAD[binary_name]:
            if self.architecture in BUNDLE_DOWNLOAD[binary_name][self.system]:
                self.file_path = BUNDLE_DOWNLOAD[binary_name][self.system][self.architecture][FILE_PATH_TOKEN]
                self.file_url = BUNDLE_DOWNLOAD[binary_name][self.system][self.architecture][FILE_URL_TOKEN]
            else:
                raise ArchitectureNotSupported("Unknown architecture")
        else:
            raise PackageNotSupported("Unknown system")

    def _get_all_binaries(self) -> None:
        """
        Get all the binaries available for download.
        """
        title = "_get_all_binaries"
        for binary in self.available_binaries:
            self.disp.log_debug(f"Downloading {binary}", title)
            self._get_correct_download_and_file_path(binary)
            self.fold_path = os.path.dirname(self.file_path)
            self._create_path_if_not_exists(self.fold_path)
            if os.path.exists(self.file_path):
                self.disp.log_debug(f"{binary} already downloaded", title)
                continue
            self._download_file(
                self.file_url,
                self.file_path,
                self.query_timeout
            )

    def _install_all_binaries(self) -> None:
        """_summary_
            This is the function that will install all the FF_family binaries is they are already downloaded.
        """
        title = "_install_all_binaries"
        for binary in self.available_binaries:
            self.disp.log_debug(f"Installing {binary}", title)
            self._get_correct_download_and_file_path(binary)
            self.fold_path = os.path.dirname(self.file_path)
            extract_to = os.path.join(
                self.cwd,
                binary
            )
            final_name = os.path.join(
                extract_to,
                self.system
            )
            if os.path.isdir(final_name):
                self.disp.log_debug(f"{binary} already installed", title)
                continue
            if binary == FFPLAY_KEY:
                extract_to = os.path.join(
                    extract_to,
                    self.system
                )
            self._create_path_if_not_exists(extract_to)
            self._extract_package(self.file_path, extract_to)
            self.extracted_folder = os.listdir(extract_to)[0]
            new_folder_path = os.path.join(
                self.cwd,
                binary,
                self.system
            )
            old_folder_path = os.path.join(
                extract_to,
                self.extracted_folder
            )
            if binary != FFPLAY_KEY:
                self._rename_extracted_folder(
                    old_folder_path,
                    new_folder_path
                )
            self.disp.log_debug(f"{binary} installed", title)

    def __call__(self, audio_segment_node: AudioSegment = None) -> int:
        """
        This is the main function that will be called when the class is instantiated.

        Args:
            audio_segment_node (AudioSegment, optional): The audio segment in which you wish to set the path to the ffmpeg library. Defaults to None.

        Returns:
            int: The status of the function.
        """
        title = "__call__"
        self.disp.log_debug(f"Starting {title}", title)
        status = self.main(audio_segment_node)
        self.disp.log_debug(f"Ending {title} with status {status}", title)
        return status

    def main(self, audio_segment_node: AudioSegment = None) -> int:
        """
            The function in charge of downloading and extracting the FF_family binaries for the current system.

        Args:
            audio_segment_node (AudioSegment, optional): The audio segment in which you wish to set the path to the ffmpeg library. Defaults to None.

        Raises:
            RuntimeError: FFmpeg cannot be installed on this device because the system is unknown to this script.

        Returns:
            int: The status of the function.
        """
        title = "main"
        try:
            found_path = self.get_ff_family_path(download_if_not_present=False)
            self.disp.log_info(
                f"FF_family already installed at {found_path}",
                title
            )
            ffmpeg_path = self.get_ffmpeg_binary_path(
                download_if_not_present=False
            )
            ffplay_path = self.get_ffplay_binary_path(
                download_if_not_present=False
            )
            ffprobe_path = self.get_ffprobe_binary_path(
                download_if_not_present=False
            )
            self.disp.log_info("Updating pydub ffmpeg path", title)
            if audio_segment_node is not None:
                audio_segment_node.ffmpeg = ffmpeg_path
            AudioSegment.ffmpeg = ffmpeg_path
            self.add_ff_family_to_path(
                ffmpeg_path, ffplay_path, ffprobe_path, download_if_not_present=False
            )
            self.disp.log_info(
                "FF_family already installed and ready to use!", title
            )
            return self.success
        except PackageNotInstalled:
            self.disp.log_warning("FFmpeg not found. Installing...", title)
        except PackageNotSupported as e:
            raise RuntimeError(
                "FFmpeg cannot be installed on this device because the system is unknown to this script."
            ) from e
        self._clean_platform_name()
        self._get_all_binaries()
        self._install_all_binaries()
        ffmpeg_path = self.get_ffmpeg_binary_path(
            download_if_not_present=False
        )
        ffplay_path = self.get_ffplay_binary_path(
            download_if_not_present=False
        )
        ffprobe_path = self.get_ffprobe_binary_path(
            download_if_not_present=False
        )
        self.disp.log_info(f"FFmpeg installed at {ffmpeg_path}", title)
        self.disp.log_info(f"FFplay installed at {ffplay_path}", title)
        self.disp.log_info(f"FFprobe installed at {ffprobe_path}", title)
        if audio_segment_node is not None:
            audio_segment_node.ffmpeg = ffmpeg_path
        AudioSegment.ffmpeg = ffmpeg_path
        self.add_ff_family_to_path(
            ffmpeg_path, ffplay_path, ffprobe_path, download_if_not_present=False
        )
        self.disp.log_info("FF_family installed and ready to use!", title)
        return self.success


if __name__ == "__main__":
    FDI = FFFamilyDownloader()
    FDI.main()
    AUDIO_WAVE = 440
    AUDIO_SAMPLE_PATH = f"./{AUDIO_WAVE}.wav"
    AUDIO_SAMPLE = FDI.generate_audio_sample(AUDIO_WAVE)
    FDI.save_audio_sample(AUDIO_SAMPLE, AUDIO_SAMPLE_PATH)
    FDI.play_audio_sample(AUDIO_SAMPLE)

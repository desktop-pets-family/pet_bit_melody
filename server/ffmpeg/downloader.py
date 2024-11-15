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
import shutil
import zipfile
import tarfile
import platform
import requests
from pydub import AudioSegment


class ArchitectureNotSupported(Exception):
    pass


class PackageNotInstalled(Exception):
    pass


class PackageNotSupported(Exception):
    pass


# Function to extract files based on archive type


FILE_URL_TOKEN = "file_url"
FILE_PATH_TOKEN = "file_path"
QUERY_TIMEOUT = 10

CWD = os.getcwd()

BUNDLE_DOWNLOAD = {
    "windows": {
        "86": {
            FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.zip",  # 32-bit Windows
            FILE_PATH_TOKEN: f"{CWD}/windows/ffmpeg-release-i686-static.zip"
        },
        "64": {
            FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-x86_64-static.zip",  # 64-bit Windows
            FILE_PATH_TOKEN: f"{CWD}/windows/ffmpeg-release-x86_64-static.zip"
        }
    },
    "linux": {
        "86": {
            # 32-bit Linux (x86)
            FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz",
            FILE_PATH_TOKEN: f"{CWD}/linux/ffmpeg-release-i686-static.tar.xz"
        },
        "64": {
            FILE_URL_TOKEN: "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz",  # 64-bit Linux
            FILE_PATH_TOKEN: f"{CWD}/linux/ffmpeg-release-x86_64-static.tar.xz"
        }
    },
    "darwin": {
        "86": {
            FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/ffmpeg-7.1.zip",  # 32-bit macOS
            FILE_PATH_TOKEN: f"{CWD}/macos/ffmpeg-7.1.zip"
        },
        "64": {
            FILE_URL_TOKEN: "https://evermeet.cx/ffmpeg/ffmpeg-7.1.zip",  # 64-bit macOS
            FILE_PATH_TOKEN: f"{CWD}/macos/ffmpeg-7.1.zip"
        }
    }
}


class FFMPEGDownloader:
    """_summary_

    Raises:
        NotImplementedError: _description_
        ValueError: _description_
    """

    ffmpeg_folder_name: str = "ffmpeg"

    def __init__(self, query_timeout: int = 10, success: int = 0, error: int = 84, debug: bool = False):
        self.success: int = success
        self.error: int = error
        self.debug: bool = debug
        self.cwd: str = os.getcwd()
        self.system: str = self.get_system_name()
        self.architecture: str = self.get_platform()
        self.file_path: str = None
        self.file_url: str = None
        self.fold_path: str = None
        self.query_timeout: int = query_timeout
        self.ffmpeg_folder_name: str = FFMPEGDownloader.ffmpeg_folder_name
        self.extract_to: str = os.path.join(self.cwd, self.ffmpeg_folder_name)
        self.extracted_folder: str = None
        self.new_folder_name: str = f"{self.ffmpeg_folder_name}_{self.system}"
        self.new_folder_path: str = None

    @staticmethod
    def extract_package(file_path: str, destination: str) -> None:
        """_summary_

        Args:
            file_path (_type_): _description_
            destination (_type_): _description_

        Raises:
            NotImplementedError: _description_
            ValueError: _description_
        """
        print(f"Extracting {file_path} to {destination}")
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
        print("Extraction complete")

    @staticmethod
    def get_system_name() -> str:
        """_summary_

        Raises:
            ArchitectureNotSupported: _description_
            PackageNotSupported: _description_
            PackageNotInstalled: _description_
            PackageNotSupported: _description_
            PackageNotInstalled: _description_

        Returns:
            str: _description_
        """
        return platform.system().lower()

    @staticmethod
    def get_platform() -> str:
        """_summary_

        Raises:
            NotImplementedError: _description_
            ValueError: _description_

        Returns:
            str: _description_
        """
        return platform.architecture()[0]

    def clean_platform_name(self) -> None:
        """_summary_

        Raises:
            NotImplementedError: _description_
            ValueError: _description_
        """
        msg = "Current system (before filtering): "
        msg += f"{self.system} {self.architecture}"
        print(msg)

        if "bit" in self.architecture:
            self.architecture = self.architecture.replace("bit", "")
        elif "x" in self.architecture:
            self.architecture = self.architecture.replace("x", "")

        msg = "Current system (after filtering): "
        msg += f"{self.system} {self.architecture}"
        print(msg)

    def get_correct_download_and_file_path(self) -> None:
        """_summary_

        Raises:
            ArchitectureNotSupported: _description_
            PackageNotSupported: _description_
            PackageNotInstalled: _description_
        """
        if self.system in BUNDLE_DOWNLOAD:
            if self.architecture in BUNDLE_DOWNLOAD[self.system]:
                self.file_path = BUNDLE_DOWNLOAD[self.system][self.architecture][FILE_PATH_TOKEN]
                self.file_url = BUNDLE_DOWNLOAD[self.system][self.architecture][FILE_URL_TOKEN]
            else:
                raise ArchitectureNotSupported("Unknown architecture")
        else:
            raise PackageNotSupported("Unknown system")

    @staticmethod
    def create_path_if_not_exists(path: str) -> None:
        """_summary_

        Args:
            path (_type_): _description_

        Raises:
            NotImplementedError: _description_
            ValueError: _description_
        """
        if not os.path.exists(path):
            print(f"Creating directory: {path}")
            os.makedirs(path, exist_ok=True)

    @staticmethod
    def download_file(file_url: str, file_path: str, query_timeout: int = 10) -> None:
        """_summary_

        Args:
            file_url (_type_): _description_
            file_path (_type_): _description_

        Raises:
            PackageNotInstalled: _description_
        """
        print(f"Downloading FFmpeg from {file_url}")
        response_data = requests.get(file_url, timeout=query_timeout)
        if response_data.status_code != 200:
            raise PackageNotInstalled("Could not download the package")
        print(f"Saving to {file_path}")
        with open(file_path, "wb") as file_descriptor:
            file_descriptor.write(response_data.content)
        print("Download complete")

    @staticmethod
    def rename_extracted_folder(old_name: str, new_name: str) -> None:
        """_summary_

        Args:
            old_name (str): _description_
            new_name (str): _description_
        """

        if os.path.exists(old_name):
            print(f"Renaming {old_name} to {new_name}")
            shutil.move(old_name, new_name)

    @staticmethod
    def get_ffmpeg_path() -> str:
        """_summary_

        Returns:
            str: _description_
        """
        system = FFMPEGDownloader.get_system_name()
        cwd = os.getcwd()
        ffmpeg_folder_name = FFMPEGDownloader.ffmpeg_folder_name
        new_folder_name: str = f"ffmpeg_{system}"
        precompiled_path = os.path.join(
            cwd,
            ffmpeg_folder_name,
            new_folder_name
        )
        path = None
        if system == "windows":
            path = os.path.join(
                precompiled_path,
                "ffmpeg.exe"
            )
        elif system == "linux":
            path = os.path.join(
                precompiled_path,
                "ffmpeg"
            )
        elif system == "darwin":
            path = os.path.join(
                precompiled_path,
                "ffmpeg"
            )
        else:
            raise PackageNotSupported("Unsupported OS")
        print(f"FFmpeg path = '{path}'")
        if os.path.exists(path):
            if os.path.isfile(path):
                return path
            raise PackageNotSupported("Path is not a file")
        raise PackageNotInstalled("ffmpeg is not properly installed")

    def main(self, audio_segement_node: AudioSegment = None) -> int:
        """_summary_

        Raises:
            PackageNotInstalled: _description_
            PackageNotSupported: _description_
            PackageNotInstalled: _description_

        Returns:
            int: _description_
        """
        try:
            found_path = self.get_ffmpeg_path()
            print(f"FFmpeg already installed at {found_path}")
            print("Updating pydub ffmpeg path")
            if audio_segement_node is not None:
                audio_segement_node.ffmpeg = found_path
            AudioSegment.ffmpeg = found_path
            return self.success
        except PackageNotInstalled:
            print("FFmpeg not found. Installing...")
        except PackageNotSupported as e:
            raise RuntimeError(
                "FFmpeg cannot be installed on this device because the system is unknown to this script."
            ) from e
        self.clean_platform_name()
        self.get_correct_download_and_file_path()
        self.fold_path = os.path.dirname(self.file_path)
        self.create_path_if_not_exists(self.fold_path)
        if not os.path.exists(self.file_path):
            self.download_file(
                self.file_url,
                self.file_path,
                self.query_timeout
            )
        self.create_path_if_not_exists(self.extract_to)
        self.extract_package(self.file_path, self.extract_to)
        self.extracted_folder = os.listdir(self.extract_to)[0]
        self.new_folder_path = os.path.join(
            self.cwd,
            self.ffmpeg_folder_name,
            self.new_folder_name
        )
        old_folder_path = os.path.join(
            self.extract_to,
            self.extracted_folder
        )
        self.rename_extracted_folder(
            old_folder_path,
            self.new_folder_path
        )
        ffmpeg_path = self.get_ffmpeg_path()
        print(f"Ffmpeg installed at {ffmpeg_path}")
        if audio_segement_node is not None:
            audio_segement_node.ffmpeg = ffmpeg_path
        AudioSegment.ffmpeg = ffmpeg_path
        print("FFmpeg installed and ready to use!")
        return self.success


if __name__ == "__main__":
    FDI = FFMPEGDownloader()
    FDI.main()

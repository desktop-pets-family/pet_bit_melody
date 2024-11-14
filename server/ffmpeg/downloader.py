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
import platform
import requests
import zipfile
import tarfile
# import shutil
# from pydub import AudioSegment


class ArchitectureNotSupported(Exception):
    pass


class PackageNotInstalled(Exception):
    pass


class PackageNotSupported(Exception):
    pass


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

SYSTEM = platform.system().lower()
ARCHITECTURE = platform.architecture()[0]

print(f"Current system (before filtering): {SYSTEM} {ARCHITECTURE}")

if "bit" in ARCHITECTURE:
    ARCHITECTURE = ARCHITECTURE.replace("bit", "")
elif "x" in ARCHITECTURE:
    ARCHITECTURE = ARCHITECTURE.replace("x", "")

print(f"Current system (after filtering): {SYSTEM} {ARCHITECTURE}")

FILE_PATH = None
FILE_URL = None

if SYSTEM in BUNDLE_DOWNLOAD:
    if ARCHITECTURE in BUNDLE_DOWNLOAD[SYSTEM]:
        FILE_PATH = BUNDLE_DOWNLOAD[SYSTEM][ARCHITECTURE][FILE_PATH_TOKEN]
        FILE_URL = BUNDLE_DOWNLOAD[SYSTEM][ARCHITECTURE][FILE_URL_TOKEN]
    else:
        raise ArchitectureNotSupported("Unknown architecture")
else:
    raise PackageNotSupported("Unknown system")

# Ensure the target directory exists
FOLD_PATH = os.path.dirname(FILE_PATH)

if not os.path.exists(FOLD_PATH):
    print(f"Creating directory: {FOLD_PATH}")
    os.makedirs(FOLD_PATH, exist_ok=True)

# Download the file if it doesn't exist
if not os.path.exists(FILE_PATH):
    print(f"Downloading FFmpeg from {FILE_URL}")
    response = requests.get(FILE_URL, timeout=QUERY_TIMEOUT)
    if response.status_code != 200:
        raise PackageNotInstalled("Could not download the package")
    print(f"Saving to {FILE_PATH}")
    with open(FILE_PATH, "wb") as file:
        file.write(response.content)
    print("Download complete")

# Function to extract files based on archive type


def extract_package(file_path: str, destination: str) -> None:
    """_summary_

    Args:
        file_path (_type_): _description_
        destination (_type_): _description_

    Raises:
        NotImplementedError: _description_
        ValueError: _description_
    """
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


# Extract the downloaded package
EXTRACT_TO = os.path.join(FOLD_PATH, 'ffmpeg')
if not os.path.exists(EXTRACT_TO):
    print(f"Creating directory: {EXTRACT_TO}")
    os.makedirs(EXTRACT_TO)

extract_package(FILE_PATH, EXTRACT_TO)

# Assuming the executable is inside the extracted folder, set path to ffmpeg
if SYSTEM == "windows":
    ffmpeg_path = os.path.join(EXTRACT_TO, "ffmpeg", "bin", "ffmpeg.exe")
elif SYSTEM == "darwin" or SYSTEM == "linux":
    ffmpeg_path = os.path.join(EXTRACT_TO, "ffmpeg", "bin", "ffmpeg")
else:
    raise PackageNotSupported("Unsupported OS")

# Check if ffmpeg is available and can be executed
if not os.path.exists(ffmpeg_path):
    raise PackageNotInstalled("ffmpeg is not properly installed")

# # Set the local ffmpeg binary in PyDub
# AudioSegment.ffmpeg = ffmpeg_path

# Now ffmpeg is ready to use!
print("FFmpeg installed and ready to use!")

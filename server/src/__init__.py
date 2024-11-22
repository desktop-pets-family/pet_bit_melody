"""
The file in charge of referencing the python files for the server
This also contains the files in charge of animating a character
"""

import sys

if __name__ == "__main__":
    print("Please run python3 ./src")
    sys.exit(1)

from .server_main import CONST
from .server_main import Main as ServerMain

__all__ = ["CONST", "ServerMain"]

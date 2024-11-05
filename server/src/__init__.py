"""
The file in charge of referencing the python files for the server
This also contains the files in charge of animating a character
"""

if __name__ != "__main__":
    from .lib import HCI, HttpCodes, Server, CONST
else:
    print("Please run python3 ./src")

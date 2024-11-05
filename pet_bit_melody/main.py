"""
    File in charge of setting up the environement for the server when it is run as a library and not a full stack application.
"""

import sys
from typing import Any, List


class Main:
    def __init__(self) -> None:
        """_summary_
        """
        self.error: int = 84
        self.success: int = 0
        self.args: List[Any] = sys.argv
        self.argc: int = len(self.args)

    def run(self) -> None:
        """_summary_
        """
        print("Noting to run yet, please check back later.")
        print("You have entered the following arguments: ", self.args)
        sys.exit(self.success)


if __name__ == "__main__":
    main = Main()
    main.run()

"""
    File in charge of setting up the environement for the server when it is run as a library and not a full stack application.
"""

import sys
from typing import Any, List
from src import ServerMain, CONST


class Main:
    """_summary_
    """

    def __init__(self) -> None:
        """_summary_
        """
        self.error: int = CONST.ERROR
        self.success: int = CONST.SUCCESS
        self.args: List[Any] = sys.argv
        self.argc: int = len(self.args)

    def run(self) -> None:
        """_summary_
        """
        SMI = ServerMain(
            success=self.success,
            error=self.error
        )
        sys.exit(SMI.main())


if __name__ == "__main__":
    main = Main()
    main.run()

"""_summary_
    The file that contains mandatory endpoints
"""


import time
from fastapi import Response, Request
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .. import constants as CONST
from ..runtime_data import RuntimeData
from ..http_codes import HCI


class Mandatory:
    """
        The class that contains mandatory endpoints
    """

    def __init__(self, runtime_data: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_
            The class in charge of the mandatory endpoints

        Args:
            runtime_data (RuntimeData): _description_
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
            debug (bool, optional): _description_. Defaults to False.
        """
        # ------------------------ Inherited variables  ------------------------
        self.debug: bool = debug
        self.success: int = success
        self.error: int = error
        self.runtime_data_initialised: RuntimeData = runtime_data
        # ------------------------- The visual logger  -------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def get_about(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/about'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "get_about"
        self.disp.log_debug(title, "Gathering data")
        host = request.client.host
        current_time = int(time.time())
        self.disp.log_debug(f"host = {host}", title)
        self.disp.log_debug(f"current_time = {current_time}", title)
        json_body = {
            " client ": {
                " host ": host
            },
            " server ": {
                " current_time ": current_time,
                " services ": self.runtime_data_initialised.boilerplate_non_http_initialised.get_services()
            }
        }
        self.disp.log_debug(f"json_body = {json_body}", title)
        outgoing = HCI.success(
            json_body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )
        self.disp.log_debug(f"ready_to_go: {outgoing}", title)
        return outgoing

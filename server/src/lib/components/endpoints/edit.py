##
# EPITECH PROJECT, 2024
# pet_bit_melody
# File description:
# project.py
##

from typing import List, Dict, Any, Union
from fastapi import Response, Request
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from ..http_codes import HCI
from .. import constants as CONST
from ..runtime_data import RuntimeData


class Edit:
    """_summary_
    """

    def __init__(self, runtime_data: RuntimeData, error: int = 84, success: int = 0, debug: bool = False) -> None:
        """_summary_
        """
        # -------------------------- Inherited values --------------------------
        self.runtime_data_initialised: RuntimeData = runtime_data
        self.error: int = error
        self.success: int = success
        self.debug: bool = debug
        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    async def get_edit_instruments(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/edit/instruments'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "edit_instruments"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(instruments) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="edit_instruments",
            message="Hello World!",
            resp="",
            token=token,
            error=False
        )
        self.disp.log_debug(f"sent body : {body}", title)
        self.disp.log_debug(
            f"header = {self.runtime_data_initialised.json_header}", title)
        outgoing = HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header)
        self.disp.log_debug(f"ready_to_go : {outgoing}",  title)
        return outgoing

    async def get_edit_instruments_range(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/edit/instruments_range'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "edit_instruments_range"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(instruments) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="edit_instruments_range",
            message="Hello World!",
            resp="",
            token=token,
            error=False
        )
        self.disp.log_debug(f"sent body : {body}", title)
        self.disp.log_debug(
            f"header = {self.runtime_data_initialised.json_header}", title)
        outgoing = HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header)
        self.disp.log_debug(f"ready_to_go : {outgoing}",  title)
        return outgoing

    async def put_edit_undo(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/edit/undo'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "undo"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(instruments) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="undo",
            message="Hello World!",
            resp="",
            token=token,
            error=False
        )
        self.disp.log_debug(f"sent body : {body}", title)
        self.disp.log_debug(
            f"header = {self.runtime_data_initialised.json_header}", title)
        outgoing = HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header)
        self.disp.log_debug(f"ready_to_go : {outgoing}",  title)
        return outgoing

    async def put_edit_redo(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/edit/redo'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "redo"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(instruments) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="redo",
            message="Hello World!",
            resp="",
            token=token,
            error=False
        )
        self.disp.log_debug(f"sent body : {body}", title)
        self.disp.log_debug(
            f"header = {self.runtime_data_initialised.json_header}", title)
        outgoing = HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header)
        self.disp.log_debug(f"ready_to_go : {outgoing}",  title)
        return outgoing

    async def put_edit_repeat(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/edit/repeat'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "repeat"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(instruments) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="repeat",
            message="Hello World!",
            resp="",
            token=token,
            error=False
        )
        self.disp.log_debug(f"sent body : {body}", title)
        self.disp.log_debug(
            f"header = {self.runtime_data_initialised.json_header}", title)
        outgoing = HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header)
        self.disp.log_debug(f"ready_to_go : {outgoing}",  title)
        return outgoing

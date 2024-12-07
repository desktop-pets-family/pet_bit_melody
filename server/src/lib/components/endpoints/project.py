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


class Project:
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

    async def post_project_new(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/project/new'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "project_new"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(project_new) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="project_new",
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

    async def post_project_reset(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/project/reset'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "project_reset"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(project_reset) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="project_reset",
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

    async def post_project_play(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/project/play'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "project_play"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(project_play) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="project_play",
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

    async def post_project_save(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/project/save'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "project_save"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(project_save) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="project_save",
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

    async def post_project_stop(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/api/v1/project/stop'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "project_stop"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(project_stop) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="project_stop",
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

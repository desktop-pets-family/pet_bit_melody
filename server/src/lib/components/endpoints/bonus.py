"""_summary_
"""

import signal
from fastapi import Response, Request
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .. import constants as CONST
from ..runtime_data import RuntimeData
from ..http_codes import HCI


class Bonus:
    """_summary_
    """

    def __init__(self, runtime_data: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_

        Args:
            runtime_data (RuntimeData): _description_
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
            debug (bool, optional): _description_. Defaults to False.
        """
        self.debug: bool = debug
        self.success: int = success
        self.error: int = error
        self.runtime_data_initialised: RuntimeData = runtime_data
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def get_welcome(self, request: Request) -> Response:
        """_summary_
            The endpoint corresponding to '/'.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "get_welcome"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f'(get_welcome) token = {token}', title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="Home",
            message="Welcome to the control server.",
            resp="",
            token=token,
            error=False
        )
        self.disp.log_debug(f"sent body : {body}", title)
        self.disp.log_debug(
            f"header = {self.runtime_data_initialised.json_header}", title
        )
        outgoing = HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )
        self.disp.log_debug(f"ready_to_go: {outgoing}", title)
        return outgoing

    def get_s3_bucket_names(self, request: Request) -> Response:
        """
            The endpoint to get every bucket data
        """
        title = "get_s3_bucket"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f"Token = {token}", title)
        if token is None:
            return self.runtime_data_initialised.boilerplate_responses_initialised.unauthorized(title, token)
        bucket_names = self.runtime_data_initialised.bucket_link.get_bucket_names()
        self.disp.log_debug(f"Bucket names: {bucket_names}", title)
        if isinstance(bucket_names, int):
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, token)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=bucket_names,
            resp="success",
            token=token,
            error=False
        )
        return HCI.success(body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)

    def get_table(self, request: Request) -> Response:
        """
            table
        """
        title = "get_table"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request)
        self.disp.log_debug(f"Token = {token}", title)
        if token is None:
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="Authorisation required.",
                resp="error",
                token=token,
                error=True
            )
            return HCI.unauthorized(body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)
        table = self.runtime_data_initialised.database_link.get_table_names()
        self.disp.log_debug(f"received in {title}", table)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=table,
            resp="success",
            token=token,
            error=False
        )
        return HCI.success(body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)

    async def post_stop_server(self, request: Request) -> Response:
        """_summary_
            The endpoint allowing a user to stop the server.

        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        title = "Stop server"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_admin(token) is False:
            self.disp.log_error(
                "Non-admin user tried to stop the server.", title
            )
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="You do not have enough privileges to run this endpoint.",
                resp="privilege to low",
                token=token,
                error=True
            )
            return HCI.unauthorized(content=body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message="The server is stopping",
            resp="success",
            token=token,
            error=False
        )
        self.disp.log_debug("Server shutting down...", f"{title}")
        self.runtime_data_initialised.server_running = False
        self.runtime_data_initialised.continue_running = False
        self.runtime_data_initialised.server.handle_exit(signal.SIGTERM, None)
        status = self.runtime_data_initialised.background_tasks_initialised.safe_stop()
        if status != self.success:
            msg = "The server is stopping with errors, cron exited "
            msg += f"with {status}."
            self.disp.log_error(
                msg,
                "post_stop_server"
            )
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message=msg,
                resp="error",
                token=token,
                error=True
            )
            del self.runtime_data_initialised.background_tasks_initialised
            self.runtime_data_initialised.background_tasks_initialised = None
            return HCI.internal_server_error(content=body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)
        return HCI.success(content=body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)

    async def trigger_endpoint(self, id: str, request: Request) -> Response:
        """_summary_
            The endpoint to trigger a specific action.

        Args:
            id (str): _description_
            request (Request): _description_

        Returns:
            Response: _description_
        """
        title = "trigger_endpoint"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if token is None:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(title)
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_admin(token) is False:
            self.disp.log_error(
                "Non-admin user tried to trigger an action.", title
            )
            return self.runtime_data_initialised.boilerplate_responses_initialised.insuffisant_rights(
                title, token
            )
        node = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_ACTIONS,
            column="*",
            where=f"id='{id}'",
            beautify=True
        )
        if isinstance(node, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message=f"The action {id} does not exist.",
                resp="error",
                token=token,
                error=True
            )
            return HCI.not_found(body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)
        data = self.runtime_data_initialised.actions_main_initialised.process_action_node(
            id
        )
        run_data = self.runtime_data_initialised.actions_main_initialised.logger.get_logs(
            id, beautify=True
        )
        self.disp.log_debug(f"run_data = {run_data}", title)
        run_data = self.runtime_data_initialised.actions_main_initialised.variables.sanitize_for_json(
            run_data, False
        )
        self.disp.log_debug(f"run_data_sanitised = {run_data}", title)
        content = {
            "action_data": node,
            "run_status": data,
            "run_data": run_data
        }
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=content,
            resp="success",
            token=token,
            error=False
        )
        return HCI.success(body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)

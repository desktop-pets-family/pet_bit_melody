"""
The file that contains every endpoints for applets
"""

from fastapi import Response, Request
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .. import constants as CONST
from ..runtime_data import RuntimeData
from ..http_codes import HCI

class Applets:
    """
    The class that contains every methods for applets
    """
    def __init__(self, runtime_data: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """
        The constructor of the Applets class
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

    def create_applet(self, request: Request) -> Response:
        """
        Create applet by id
        """
        title = "Create applet"
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="create_applet",
            message="Not implemented yet",
            resp="not implemented",
            token=None,
            error= True
        )
        return HCI.not_implemented(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def put_applet_by_id(self, request: Request, id: str) -> Response:
        """
        Modify applet by id
        """
        title = "Put applet by id"
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="create_applet",
            message="Not implemented yet",
            resp="not implemented",
            token=None,
            error= True
        )
        return HCI.not_implemented(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def get_applet_by_id(self, request: Request, id: int) -> Response:
        """
        Get applet by id
        """
        title = "Get applet by id"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        self.disp.log_debug(f"Token = {token}", title)
        id_str = str(id)
        applet_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_ACTIONS,
            "*",
            f"id='{id_str}'"
        )
        if not applet_data or isinstance(applet_data, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="Applet not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        self.disp.log_debug(f"Applet found: {applet_data}", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=applet_data,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def get_all_applets(self, request: Request) -> Response:
        """
        Get all applets
        """
        title = "Get all applets"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        self.disp.log_debug(f"Token = {token}", title)
        applets_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_ACTIONS,
            "*"
        )
        if not applets_data or isinstance(applets_data, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="Applets not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        self.disp.log_debug(f"Applet found: {applets_data}", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=applets_data,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def get_user_applets(self, request: Request) -> Response:
        """
        Get user applets
        """
        title = "Get user applets"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        self.disp.log_debug(f"Token = {token}", title)
        user_id = self.runtime_data_initialised.boilerplate_non_http_initialised.get_user_id_from_token(
            title,
            token
        )
        if isinstance(user_id, Response):
            return user_id
        applets_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_USER_SERVICES,
            "*",
            f"user_id='{user_id}'"
        )
        if not applets_data or isinstance(applets_data, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="Applets not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=applets_data,
            resp="success",
            token=token
        )
        return HCI.not_implemented(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def get_applets_by_tags(self, request: Request, tags: str) -> Response:
        """
        Get applets by tags
        """
        title = "Get applets by tags"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        self.disp.log_debug(f"Token = {token}", title)
        if not tags or tags == "":
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title,
                token
            )
        tags_list = tags.split(":")
        applets_data = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_ACTIONS,
            "*"
        )
        if not applets_data or isinstance(applets_data, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="Applets not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        self.disp.log_debug(f"Applet found: {applets_data}", title)
        filtered_applets: list[dict] = []
        for _, applet in enumerate(applets_data):
            for _, element in enumerate(tags_list):
                if element in applet["tags"]:
                    filtered_applets.append(applet)
        self.disp.log_debug(f"Applet found with tags: {filtered_applets}", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message=filtered_applets,
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def get_recent_applets(self, request: Request) -> Response:
        """
        Get recent applets
        """
        title = "Get recent applets"
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="create_applet",
            message="Not implemented yet",
            resp="not implemented",
            token=None,
            error= True
        )
        return HCI.not_implemented(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def post_connect_applet(self, request: Request, id: int) -> Response:
        """
        Connect user to an applet
        """
        title = "Connect user to an applet"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        self.disp.log_debug(f"Token = {token}", title)
        id_str = str(id)
        applet_id = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_ACTIONS,
            "id",
            f"id='{id_str}'"
        )
        if not applet_id or isinstance(applet_id, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="Applet not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        self.disp.log_debug(f"Applet id found: {applet_id}", title)
        user_id = self.runtime_data_initialised.boilerplate_non_http_initialised.get_user_id_from_token(
            title,
            token
        )
        if isinstance(user_id, Response):
            return user_id
        self.disp.log_debug(f"User id found: {user_id}", title)
        data: list = [user_id, applet_id]
        columns: list = self.runtime_data_initialised.database_link.get_table_column_names(
            CONST.TAB_USER_SERVICES
        )
        if not columns or isinstance(columns, int):
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        columns.pop(0)
        self.disp.log_debug(f"Got columns: {columns}", title)
        self.runtime_data_initialised.database_link.insert_data_into_table(
            CONST.TAB_USER_SERVICES,
            data,
            columns
        )
        self.disp.log_debug("Connected", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message="You are connected to the applet successfully.",
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def delete_disconnect_applet(self, request: Request, id: int) -> Response:
        """
        Disconnect user to an applet
        """
        title = "Disconnect user to an applet"
        token = self.runtime_data_initialised.boilerplate_incoming_initialised.get_token_if_present(
            request
        )
        if not token:
            return self.runtime_data_initialised.boilerplate_responses_initialised.bad_request(
                title
            )
        if self.runtime_data_initialised.boilerplate_non_http_initialised.is_token_correct(
            token
        ) is False:
            return self.runtime_data_initialised.boilerplate_responses_initialised.invalid_token(
                title
            )
        self.disp.log_debug(f"Token = {token}", title)
        id_str = str(id)
        applet_id = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_ACTIONS,
            "id",
            f"id='{id_str}'"
        )
        if not applet_id or isinstance(applet_id, int):
            body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
                title=title,
                message="Applet not found.",
                resp="not found",
                token=token,
                error=True
            )
            return HCI.not_found(
                content=body,
                content_type=CONST.CONTENT_TYPE,
                headers=self.runtime_data_initialised.json_header
            )
        self.disp.log_debug(f"Applet id found: {applet_id}", title)
        user_id = self.runtime_data_initialised.boilerplate_non_http_initialised.get_user_id_from_token(
            title,
            token
        )
        if isinstance(user_id, Response):
            return user_id
        self.disp.log_debug(f"User id found: {user_id}", title)
        remove = self.runtime_data_initialised.database_link.remove_data_from_table(
            CONST.TAB_USER_SERVICES,
            f"user_id='{user_id}' AND area_id='{applet_id}'"
        )
        if remove == self.error:
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(
                title,
                token
            )
        self.disp.log_debug("Disconnected", title)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title=title,
            message="You are disconnected from the applet successfully.",
            resp="success",
            token=token
        )
        return HCI.success(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def get_triggers_by_service_name(self, request: Request, service_name: str) -> Response:
        """
        Get triggers by service name
        """
        title = "Get triggers by service name"
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="create_applet",
            message="Not implemented yet",
            resp="not implemented",
            token=None,
            error= True
        )
        return HCI.not_implemented(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

    def get_reactions_by_service_name(self, request: Request, service_name: str) -> Response:
        """
        Get reactions by service name
        """
        title = "Get reactions by service name"
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="create_applet",
            message="Not implemented yet",
            resp="not implemented",
            token=None,
            error= True
        )
        return HCI.not_implemented(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )
    
    def delete_applet_by_id(self, request: Request, id: str) -> Response:
        """
        Get reactions by service name
        """
        title = "Delete service by id"
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="create_applet",
            message="Not implemented yet",
            resp="not implemented",
            token=None,
            error= True
        )
        return HCI.not_implemented(
            content=body,
            content_type=CONST.CONTENT_TYPE,
            headers=self.runtime_data_initialised.json_header
        )

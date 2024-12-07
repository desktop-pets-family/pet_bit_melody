"""_summary_
    This is the the class in charge of containing the non-http boilerplates.
"""

import re
import uuid
import json
from random import randint
from datetime import datetime, timedelta
from typing import Union, List, Dict, Any

from fastapi import Response
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME

from ..components import RuntimeData, CONST
from ..sql.sql_manager import SQL


class BoilerplateNonHTTP:
    """_summary_
    """

    def __init__(self, runtime_data_initialised: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_
        """
        self.debug: bool = debug
        self.error: int = error
        self.success: int = success
        self.runtime_data_initialised: RuntimeData = runtime_data_initialised
        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def pause(self) -> str:
        """_summary_
            This is a pause function that works in the same wat as the batch pause command.
            It pauses the program execution until the user presses the enter key.

        Returns:
            str: _description_: The input from the user
        """
        return input("Press enter to continue...")

    def set_lifespan(self, seconds: int) -> datetime:
        """
                The function to set the lifespan of the user token
            Args:
                seconds (int): Seconds

            Returns:
                datetime: The datetime of the lifespan of the token
            """
        current_time = datetime.now()
        offset_time = current_time + timedelta(seconds=seconds)
        return offset_time

    def is_token_correct(self, token: str) -> bool:
        """_summary_
            Check if the token is correct.
        Args:
            token (str): _description_: The token to check

        Returns:
            bool: _description_: True if the token is correct, False otherwise
        """
        title = "is_token_correct"
        self.disp.log_debug("Checking if the token is correct.", title)
        if isinstance(token, str) is False:
            return False
        login_table = self.runtime_data_initialised.database_link.get_data_from_table(
            CONST.TAB_CONNECTIONS,
            "*",
            where=f"token={token}",
            beautify=False
        )
        if isinstance(login_table, int):
            return False
        if len(login_table) != 1:
            return False
        self.disp.log_debug(f"login_table = {login_table}", title)
        if datetime.now() > login_table[0][-1]:
            return False
        new_date = self.runtime_data_initialised.boilerplate_non_http_initialised.set_lifespan(
            CONST.UA_TOKEN_LIFESPAN
        )
        new_date_str = self.runtime_data_initialised.database_link.datetime_to_string(
            datetime_instance=new_date,
            date_only=False,
            sql_mode=True
        )
        self.disp.log_debug(f"string date: {new_date_str}", title)
        status = self.runtime_data_initialised.database_link.update_data_in_table(
            table=CONST.TAB_CONNECTIONS,
            data=new_date_str,
            column="expiration_date",
            where=f"token={token}"
        )
        if status != self.success:
            self.disp.log_warning(
                f"Failed to update expiration_date for {token}.",
                title
            )
        return True

    def generate_token(self) -> str:
        """_summary_
            This is a function that will generate a token for the user.
        Returns:
            str: _description_: The token generated
        """
        title = "generate_token"
        token = str(uuid.uuid4())
        user_token = self.runtime_data_initialised.database_link.get_data_from_table(
            table=CONST.TAB_CONNECTIONS,
            column="token",
            where=f"token='{token}'",
            beautify=False
        )
        self.disp.log_debug(f"user_token = {user_token}", title)
        while len(user_token) > 0:
            token = str(uuid.uuid4())
            user_token = self.runtime_data_initialised.database_link.get_data_from_table(
                table=CONST.TAB_CONNECTIONS,
                column="token",
                where=f"token='{token}'",
                beautify=False
            )
            self.disp.log_debug(f"user_token = {user_token}", title)
            if isinstance(user_token, int) is True and user_token == self.error:
                return token
            if len(user_token) == 0:
                return token
        return token

    def server_show_item_content(self, function_name: str = "show_item_content", item_name: str = "", item: object = None, show: bool = True) -> None:
        """_summary_
            This is a function that will display the content of an item.
            The purpose of this function is more for debugging purposes.
        Args:
            function_name (str, optional): _description_. Defaults to "show_item_content".
            item (object, optional): _description_. Defaults to None.
        """
        if show is False:
            return
        self.disp.log_debug(
            f"({function_name}) dir({item_name}) = {dir(item)}",
            "pet_server_show_item_content"
        )
        for i in dir(item):
            if i in ("auth", "session", "user"):
                self.disp.log_debug(
                    f"({function_name}) skipping {item_name}.{i}"
                )
                continue
            self.disp.log_debug(
                f"({function_name}) {item_name}.{i} = {getattr(item, i)}"
            )

    def check_date(self, date: str = "DD/MM/YYYY") -> bool:
        """_summary_
            This is a function that will check if the date is correct or not.
        Args:
            date (str, optional): _description_: The date to check. Defaults to "DD/MM/YYYY".

        Returns:
            bool: _description_: True if the date is correct, False otherwise
        """
        pattern = re.compile(
            r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        )
        match = pattern.match(date)
        return bool(match)

    def check_database_health(self) -> None:
        """_summary_
            This function will reconnect to the database in case it has been disconnected.
        """
        if self.runtime_data_initialised.database_link is None:
            try:
                self.disp.log_debug(
                    "database_link is none, initialising sql.",
                    "check_database_health"
                )
                self.runtime_data_initialised.database_link = SQL(
                    url=CONST.DB_HOST,
                    port=CONST.DB_PORT,
                    username=CONST.DB_USER,
                    password=CONST.DB_PASSWORD,
                    db_name=CONST.DB_DATABASE,
                    success=self.success,
                    error=self.error,
                    debug=self.debug
                )
            except RuntimeError as e:
                msg = "Could not connect to the database."
                raise RuntimeError(msg) from e

        if self.runtime_data_initialised.database_link.is_connected() is False:
            if self.runtime_data_initialised.database_link.connect_to_db() is False:
                try:
                    self.disp.log_debug(
                        "database_link is none, initialising sql.",
                        "check_database_health"
                    )
                    self.runtime_data_initialised.database_link = SQL(
                        url=CONST.DB_HOST,
                        port=CONST.DB_PORT,
                        username=CONST.DB_USER,
                        password=CONST.DB_PASSWORD,
                        db_name=CONST.DB_DATABASE,
                        success=self.success,
                        error=self.error,
                        debug=self.debug
                    )
                except RuntimeError as e:
                    msg = "(check_database_health) Could not connect to the database."
                    raise RuntimeError(msg) from e

    def is_token_admin(self, token: str) -> bool:
        """_summary_
            Check if the user's token has admin privileges.
        Args:
            token (str): _description_

        Returns:
            bool: _description_
        """
        title = "is_token_admin"
        user_id = self.runtime_data_initialised.database_link.get_data_from_table(
            table=CONST.TAB_CONNECTIONS,
            column="user_id",
            where=f"token='{token}'",
            beautify=False
        )
        if isinstance(user_id, int) is True and user_id == self.error or not user_id:
            self.disp.log_error(
                f"Failed to find token {token} in the database.", title
            )
            return False
        self.disp.log_debug(f"usr_id = {user_id}", title)
        user_info = self.runtime_data_initialised.database_link.get_data_from_table(
            table=CONST.TAB_ACCOUNTS,
            column="admin",
            where=f"id={user_id[0][0]}",
            beautify=False
        )
        if isinstance(user_info, int) is True and user_info == self.error:
            self.disp.log_error(
                f"Failed to find user {user_id[0][0]} in the database.", title
            )
            return False
        self.disp.log_debug(f"usr_info = {user_info}", title)
        return user_info[0][0] == 1

    def generate_check_token(self, token_size: int = 4) -> str:
        """_summary_
            Create a token that can be used for e-mail verification.

        Returns:
            str: _description_
        """
        if isinstance(token_size, (int, float)) is False:
            token_size = 4
        token_size = int(token_size)
        token_size = max(token_size, 0)
        code = f"{randint(CONST.RANDOM_MIN, CONST.RANDOM_MAX)}"
        for i in range(token_size):
            code += f"-{randint(CONST.RANDOM_MIN, CONST.RANDOM_MAX)}"
        return code

    def get_user_id_from_token(self, title: str, token: str) -> Union[str, Response]:
        """_summary_
            The function in charge of getting the user id based of the provided content.

        Args:
            title (str): _description_: The title of the endpoint calling it
            token (str): _description_: The token of the user account

        Returns:
            Union[str, Response]: _description_: Returns as string id if success, otherwise, a pre-made response for the endpoint.
        """
        function_title = "get_user_id_from_token"
        usr_id_node: str = "user_id"
        self.disp.log_debug(
            f"Getting user id based on {token}", function_title
        )
        current_user: List[Dict[str]] = self.runtime_data_initialised.database_link.get_data_from_table(
            table=CONST.TAB_CONNECTIONS,
            column="*",
            where=f"token='{token}'",
            beautify=True
        )
        self.disp.log_debug(f"current_user = {current_user}", function_title)
        if current_user == self.error:
            return self.runtime_data_initialised.boilerplate_responses_initialised.user_not_found(title, token)
        self.disp.log_debug(
            f"user_length = {len(current_user)}", function_title
        )
        if len(current_user) == 0 or len(current_user) > 1:
            return self.runtime_data_initialised.boilerplate_responses_initialised.user_not_found(title, token)
        self.disp.log_debug(
            f"current_user[0] = {current_user[0]}", function_title
        )
        if usr_id_node not in current_user[0]:
            return self.runtime_data_initialised.boilerplate_responses_initialised.user_not_found(title, token)
        msg = "str(current_user[0]["
        msg += f"{usr_id_node}]) = {str(current_user[0][usr_id_node])}"
        self.disp.log_debug(msg, function_title)
        return str(current_user[0][usr_id_node])

    def update_user_data(self, title: str, usr_id: str, line_content: List[str]) -> Union[int, Response]:
        """_summary_
            Update the account information based on the provided line.

        Args:
            title (str): _description_: This is the title of the endpoint
            usr_id (str): _description_: This is the id of the user that needs to be updated
            line_content (List[str]): _description_: The content of the line to be edited.

        Returns:
            Union[int, Response]: _description_
        """
        self.disp.log_debug(f"Compile line_content: {line_content}.", title)
        columns: List[str] = self.runtime_data_initialised.database_link.get_table_column_names(
            CONST.TAB_ACCOUNTS
        )
        self.disp.log_debug(f"Removing id from columns: {columns}.", title)
        columns.pop(0)
        status = self.runtime_data_initialised.database_link.update_data_in_table(
            table=CONST.TAB_ACCOUNTS,
            data=line_content,
            column=columns,
            where=f"id='{usr_id}'"
        )
        if status == self.error:
            return self.runtime_data_initialised.boilerplate_responses_initialised.internal_server_error(title, usr_id)
        return self.success

    def remove_user_from_tables(self, where: str, tables: List[str]) -> Union[int, Dict[str, int]]:
        """_summary_
            Remove the user from the provided tables.

        Args:
            where (str): _description_: The id of the user to remove
            tables (List[str]): _description_: The tables to remove the user from

        Returns:
            int: _description_: The status of the operation
        """
        title = "remove_user_from_tables"
        if isinstance(tables, (List, tuple, str)) is False:
            self.disp.log_error(
                f"Expected tables to be of type list but got {type(tables)}",
                title
            )
            return self.error
        if isinstance(tables, str) is True:
            self.disp.log_warning(
                "Tables is of type str, converting to list[str].", title
            )
            tables = [tables]
        deletion_status = {}
        for table in tables:
            status = self.runtime_data_initialised.database_link.remove_data_from_table(
                table=table,
                where=where
            )
            deletion_status[str(table)] = status
            if status == self.error:
                self.disp.log_warning(
                    f"Failed to remove data from table: {table}",
                    title
                )
        return deletion_status

    def update_single_data(self, table: str, column_finder: str, column_to_update: str, data_finder: str, request_body: dict) -> int:
        """
        The function in charge of updating the data in the database
        """
        if self.runtime_data_initialised.database_link.update_data_in_table(
            table,
            [request_body[column_to_update]],
            [column_to_update],
            f"{column_finder}='{data_finder}'"
        ) == self.error:
            return self.error
        return self.success

    def get_actions(self, service_id: str) -> List[Dict[str, Any]]:
        """_summary_
            Get the actions that are available for the service

        Args:
            service_id (str): _description_

        Returns:
            List[Dict[str, Any]]: _description_
        """
        title = "get_actions"
        result = []
        self.disp.log_debug("Gathering actions", title)
        actions = self.runtime_data_initialised.database_link.get_data_from_table(
            table=CONST.TAB_ACTION_TEMPLATE,
            column="*",
            where=f"action_id='{service_id}' AND type='trigger'",
            beautify=True
        )
        self.disp.log_debug(f"actions = {actions}", title)
        if actions == self.error:
            self.disp.log_error("Failed to get actions", title)
            return result
        for index, item in enumerate(actions):
            try:
                if "json" not in item:
                    self.disp.log_error(f"json not in item {index}", title)
                    self.disp.log_warning("Skipping action", title)
                    continue
                if item["type"].lower() != "trigger":
                    self.disp.log_debug(
                        f"item {index} is not a trigger", title
                    )
                    self.disp.log_debug("Skipping action", title)
                    continue
                self.disp.log_debug(f"item = {item}", title)
                self.disp.log_debug("Getting json node.", title)
                node_str = item["json"]
                node = json.loads(node_str)
                self.disp.log_debug("data has been converted to json", title)
                self.disp.log_debug(f"node = {node}", title)
                self.disp.log_debug(f"node keys = {list(node)}", title)
                self.disp.log_debug("Adding reaction to result", title)
                result.append(
                    {
                        "name": node["ignore:name"],
                        "description": node["ignore:description"],
                    }
                )
                self.disp.log_debug("Reaction gathered.", title)
            except Exception as e:
                self.disp.log_error(f"Failed to parse reaction {index}", title)
                self.disp.log_error(f"Error: {e}", title)
                self.disp.log_info("Skipping reaction", title)
        self.disp.log_debug(f"result = {result}", title)
        return result

    def get_reactions(self, service_id: str) -> List[Dict[str, Any]]:
        """_summary_
            Get the reactions that are available for the service

        Args:
            service_id (str): _description_

        Returns:
            List[Dict[str, Any]]: _description_
        """
        title = "get_reactions"
        self.disp.log_debug("Gathering reactions", title)
        result = []
        reactions = self.runtime_data_initialised.database_link.get_data_from_table(
            table=CONST.TAB_ACTION_TEMPLATE,
            column="*",
            where=f"action_id='{service_id}' AND type='action'",
            beautify=True
        )
        self.disp.log_debug(f"reactions = {reactions}", title)
        if reactions == self.error:
            self.disp.log_error("Failed to get reactions", title)
            return result
        for index, item in enumerate(reactions):
            try:
                if "json" not in item:
                    self.disp.log_error(f"json not in item {index}", title)
                    self.disp.log_warning("Skipping action", title)
                    continue
                if item["type"].lower() != "action":
                    self.disp.log_debug(
                        f"item {index} is not a action", title
                    )
                    self.disp.log_debug("Skipping trigger", title)
                    continue
                self.disp.log_debug(f"item = {item}", title)
                self.disp.log_debug("Getting json node.", title)
                node_str = item["json"]
                node = json.loads(node_str)
                self.disp.log_debug("data has been converted to json", title)
                self.disp.log_debug(f"node = {node}", title)
                self.disp.log_debug(f"node keys = {list(node)}", title)
                self.disp.log_debug("Adding reaction to result", title)
                result.append(
                    {
                        "name": node["ignore:name"],
                        "description": node["ignore:description"],
                    }
                )
                self.disp.log_debug("Reaction gathered.", title)
            except Exception as e:
                self.disp.log_error(f"Failed to parse reaction {index}", title)
                self.disp.log_error(f"Error: {e}", title)
                self.disp.log_info("Skipping reaction", title)
        self.disp.log_debug(f"result = {result}", title)
        return result

    def get_services(self) -> List[Dict[str, Any]]:
        """_summary_
            Get the services that are available.

        Returns:
            List[Dict[str, Any]]: _description_
        """
        title = "get_services"
        self.disp.log_debug("Gathering services", title)
        result = []
        services = self.runtime_data_initialised.database_link.get_data_from_table(
            table=CONST.TAB_SERVICES,
            column="*",
            where="",
            beautify=True
        )
        self.disp.log_debug(f"services = {services}", title)
        if services == self.error:
            self.disp.log_error("Failed to get services", title)
            return result
        for index, item in enumerate(services):
            result.append(
                {
                    "name": item["name"],
                    "actions": self.get_actions(services[index]["id"]),
                    "reactions": self.get_reactions(services[index]["id"])
                }
            )
        self.disp.log_debug(f"result = {result}", title)
        return result

    def hide_api_key(self, api_key: str) -> str:
        """_summary_
            Hide the api key from the user.

        Args:
            api_key (str): _description_: The api key to hide

        Returns:
            str: _description_: The hidden api key
        """
        title = "hide_api_key"
        self.disp.log_debug(f"api_key = {api_key}", title)
        if api_key is None:
            api_key = "No api key"
        else:
            api_key = "Some api key"
        self.disp.log_debug(f"api_key after: {api_key}", title)
        return api_key

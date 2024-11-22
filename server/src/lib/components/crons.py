"""_summary_
    File in charge of containing the functions that will be run in the background.
"""
from typing import Any, List, Dict
from datetime import datetime
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .runtime_data import RuntimeData
from . import constants as CONST


class Crons:
    """_summary_
    """

    def __init__(self, runtime_data: RuntimeData, error: int = 84, success: int = 0, debug: bool = False) -> None:

        # -------------------------- Inherited values --------------------------
        self.error: int = error
        self.success: int = success
        self.debug: bool = debug
        self.runtime_data: RuntimeData = runtime_data
        # ---------------------- The visual logger class  ----------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def __del__(self) -> None:
        """_summary_
            The destructor of the class
        """
        self.disp.log_info("Cron sub processes are shutting down.", "__del__")
        if self.runtime_data.background_tasks_initialised is not None:
            del self.runtime_data.background_tasks_initialised
            self.runtime_data.background_tasks_initialised = None

    def inject_crons(self) -> int:
        """_summary_
            Add the cron functions to the cron loop.

        Returns:
            int: _description_: The overall status of the injection.
        """
        self.runtime_data.background_tasks_initialised.safe_add_task(
            func=self.check_actions,
            args=None,
            trigger='interval',
            seconds=CONST.CHECK_ACTIONS_INTERVAL
        )
        if CONST.ENABLE_TEST_CRONS is True:
            self.runtime_data.background_tasks_initialised.safe_add_task(
                func=self._harass_database,
                args=None,
                trigger='interval',
                seconds=CONST.TEST_CRONS_INTERVAL
            )
            self.runtime_data.background_tasks_initialised.safe_add_task(
                func=self._test_current_date,
                args=datetime.now,
                trigger='interval',
                seconds=CONST.TEST_CRONS_INTERVAL
            )
            self.runtime_data.background_tasks_initialised.safe_add_task(
                func=self._test_hello_world,
                args=None,
                trigger='interval',
                seconds=CONST.TEST_CRONS_INTERVAL
            )
        if CONST.CLEAN_TOKENS is True:
            self.runtime_data.background_tasks_initialised.safe_add_task(
                func=self.clean_expired_tokens,
                args=None,
                trigger='interval',
                seconds=CONST.CLEAN_TOKENS_INTERVAL
            )
        if CONST.CLEAN_VERIFICATION is True:
            self.runtime_data.background_tasks_initialised.safe_add_task(
                func=self.clean_expired_verification_nodes,
                args=None,
                trigger='interval',
                seconds=CONST.CLEAN_VERIFICATION_INTERVAL
            )
        if CONST.RENEW_OATH_TOKENS is True:
            self.runtime_data.background_tasks_initialised.safe_add_task(
                func=self.renew_oaths,
                args=None,
                trigger='interval',
                seconds=CONST.RENEW_OATH_TOKENS_INTERVAL
            )

    def _test_hello_world(self) -> None:
        """_summary_
            This is a test function that will print "Hello World".
        """
        self.disp.log_info("Hello World", "_test_hello_world")

    def _test_current_date(self, *args: Any) -> None:
        """_summary_
            This is a test function that will print the current date.
        Args:
            date (datetime): _description_
        """
        if len(args) >= 1:
            date = args[0]
        else:
            date = datetime.now()
        if callable(date) is True:
            self.disp.log_info(
                f"(Called) Current date: {date()}",
                "_test_current_date"
            )
        else:
            self.disp.log_info(
                f"(Not called) Current date: {date}",
                "_test_current_date"
            )

    def _harass_database(self, *args: Any) -> None:
        """_summary_
            This is a test function that will print the current date.
        Args:
            date (datetime): _description_
        """
        title = "_harass_database"
        self.disp.log_info(f"In {title}", title)
        self.runtime_data.database_link.show_connection_info()
        connection = self.runtime_data.database_link.is_connected()
        self.disp.log_info(
            f"Connection status: {connection}",
            title
        )
        if connection is False:
            self.runtime_data.database_link.connect_to_db()
            connection = self.runtime_data.database_link.is_connected()
            self.disp.log_info(
                f"Connection status: {connection}",
                title
            )
            connection = self.runtime_data.database_link.is_connected()
            self.disp.log_info(
                f"Connection status: {connection}",
                title
            )
        if connection is True:
            data = self.runtime_data.database_link.get_table_names()
            self.disp.log_info(
                f"Data from {CONST.TAB_CONNECTIONS}: {data}",
                title
            )
            data = self.runtime_data.database_link.describe_table(
                CONST.TAB_CONNECTIONS
            )
            self.disp.log_info(
                f"Data from {CONST.TAB_CONNECTIONS}: {data}",
                title
            )
            data = self.runtime_data.database_link.get_data_from_table(
                CONST.TAB_CONNECTIONS, "*", "", True
            )
            self.disp.log_info(
                f"Data from {CONST.TAB_CONNECTIONS}: {data}",
                title
            )
            data = self.runtime_data.database_link.get_table_column_names(
                CONST.TAB_CONNECTIONS
            )
            self.disp.log_info(
                f"Data from {CONST.TAB_CONNECTIONS}: {data}",
                title
            )
            data = self.runtime_data.database_link.get_table_size(
                CONST.TAB_CONNECTIONS, "*", ""
            )
            self.disp.log_info(
                f"Data from {CONST.TAB_CONNECTIONS}: {data}",
                title
            )
        self.disp.log_info(f"Out of {title}.", title)

    def clean_expired_tokens(self) -> None:
        """_summary_
            Remove the tokens that have passed their lifespan.
        """
        title = "clean_expired_tokens"
        date_node = "expiration_date"
        current_time = datetime.now()
        self.disp.log_info("Cleaning expired tokens", title)
        current_tokens = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_CONNECTIONS,
            column="*",
            where="",
            beautify=True
        )
        if isinstance(current_tokens, int) is True:
            msg = "There is no data to be cleared in "
            msg += f"{CONST.TAB_CONNECTIONS} table."
            self.disp.log_warning(msg, title)
            return
        self.disp.log_debug(f"current tokens = {current_tokens}", title)
        for i in current_tokens:
            if i[date_node] is not None and i[date_node] != "" and isinstance(i[date_node], str) is True:
                datetime_node = self.runtime_data.database_link.string_to_datetime(
                    i[date_node]
                )
                msg = f"Converted {i[date_node]} to a datetime instance"
                msg += f" ({datetime_node})."
                self.disp.log_debug(msg, title)
            else:
                datetime_node = i[date_node]
                self.disp.log_debug(f"Did not convert {i[date_node]}.", title)
            if datetime_node < current_time:
                self.runtime_data.database_link.remove_data_from_table(
                    table=CONST.TAB_CONNECTIONS,
                    where=f"id='{i['id']}'"
                )
                self.disp.log_debug(f"Removed {i}.", title)
            else:
                self.disp.log_debug(
                    f"Did not remove {i} because it is not yet time.", title
                )
        self.disp.log_debug("Cleaned expired tokens", title)

    def clean_expired_verification_nodes(self) -> None:
        """_summary_
            Remove the nodes in the verification table that have passed their lifespan.
        """
        title = "clean_expired_verification_nodes"
        date_node = "expiration"
        current_time = datetime.now()
        self.disp.log_info(
            f"Cleaning expired lines in the {CONST.TAB_VERIFICATION} table.",
            title
        )
        current_lines = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_VERIFICATION,
            column="*",
            where="",
            beautify=True
        )
        if isinstance(current_lines, int) is True:
            msg = "There is no data to be cleared in "
            msg += f"{CONST.TAB_VERIFICATION} table."
            self.disp.log_warning(
                msg,
                title
            )
            return
        self.disp.log_debug(f"current lines = {current_lines}", title)
        for i in current_lines:
            if i[date_node] is not None and i[date_node] != "" and isinstance(i[date_node], str) is True:
                datetime_node = self.runtime_data.database_link.string_to_datetime(
                    i[date_node]
                )
                msg = f"Converted {i[date_node]} to a datetime instance"
                msg += f" ({datetime_node})."
                self.disp.log_debug(msg, title)
            else:
                datetime_node = i[date_node]
                self.disp.log_debug(f"Did not convert {i[date_node]}.", title)
            if datetime_node < current_time:
                self.runtime_data.database_link.remove_data_from_table(
                    table=CONST.TAB_VERIFICATION,
                    where=f"id='{i['id']}'"
                )
                self.disp.log_debug(f"Removed {i}.", title)
        self.disp.log_debug("Cleaned expired lines", title)

    def renew_oaths(self) -> None:
        """_summary_
            Function in charge of renewing the oath tokens that are about to expire.
        """
        title = "renew_oaths"
        self.disp.log_debug(
            "Checking for oaths that need to be renewed", title
        )
        oath_connections: List[Dict[str]] = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_ACTIVE_OAUTHS,
            column="*",
            where="",
            beautify=True
        )
        current_time: datetime = datetime.now()
        for oath in oath_connections:
            node_id: str = oath['id']
            token_expiration: datetime = oath["token_expiration"]
            if current_time > token_expiration:
                renew_link: str = oath["refresh_link"]
                lifespan: int = int(oath["token_lifespan"])
                provider_name: List[
                    Dict[str, Any]
                ] = self.runtime_data.database_link.get_data_from_table(
                    table=CONST.TAB_SERVICES,
                    column="name",
                    where=f"id='{oath['service_id']}'",
                    beautify=True
                )
                if isinstance(provider_name, int) is True:
                    self.disp.log_error(
                        f"Could not find provider name for {node_id}", title
                    )
                    continue
                new_token: str = self.runtime_data.oauth_authentication_initialised.refresh_token(
                    provider_name[0]['name'],
                    renew_link
                )
                token_expiration: str = self.runtime_data.database_link.datetime_to_string(
                    datetime=self.runtime_data.boilerplate_non_http_initialised.set_lifespan(
                        seconds=lifespan
                    ),
                    date_only=False,
                    sql_mode=True
                )
                self.disp.log_debug(
                    f"token expiration = {token_expiration}", title
                )
                if new_token != "":
                    self.runtime_data.database_link.update_data_in_table(
                        table=CONST.TAB_ACTIVE_OAUTHS,
                        data={
                            "token": new_token,
                            "token_expiration": token_expiration
                        },
                        where=f"id='{node_id}'"
                    )
                    self.disp.log_debug(
                        f"token {new_token} updated for {node_id}"
                    )
                else:
                    self.disp.log_error(f"Could not renew token for {node_id}")
            else:
                self.disp.log_debug(
                    f"Token for {node_id} does not need to be renewed.", title
                )
        self.disp.log_debug("Checked for oath that need to be renewed", title)

    def check_actions(self) -> None:
        """_summary_
            Function in charge of checking if any actions need to be run.
        """
        title = "check_actions"
        self.disp.log_debug("Checking for actions that need to be run.", title)
        self.runtime_data.actions_main_initialised.execute_actions()
        self.disp.log_debug("Checked for actions that needed to be run", title)

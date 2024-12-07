"""_summary_
    File in charge of logging events into the logging database
"""
from typing import List, Union, Dict, Any

from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME

from ..components.runtime_data import RuntimeData
from ..components import constants as CONST

from . import constants as ACONST


class ActionLogger:
    """_summary_
        Class in charge of logging events into the logging database
    """

    def __init__(self, runtime_data: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_
            Class in charge of logging events into the logging database

        Args:
            runtime_data (RuntimeData): _description_
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
            debug (bool, optional): _description_. Defaults to False.
        """
        # -------------------------- Inherited values --------------------------
        self.error = error
        self.debug = debug
        self.success = success
        self.runtime_data = runtime_data
        # ---------------------- The visual logger class  ----------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def log_event(self, log_type: str, action_id: int = 0, code: int = ACONST.CODE_ERROR, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            code (int, optional): _description_: The code of the event, defaults to ACONST.CODE_ERROR
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns 0 if it succeeds, 84 otherwise
        """
        title = "log_event"

        columns: List[str] = self.runtime_data.database_link.get_table_column_names(
            CONST.TAB_ACTION_LOGGING
        )
        if isinstance(columns, int) is True and columns != self.success:
            self.disp.log_error("Failed to get the table columns.", title)
            return self.error
        columns.pop(0)

        if log_type not in ACONST.LIST_TYPE:
            msg = f"Type: {type} is not in the list of types."
            msg += f" Setting type to {ACONST.TYPE_UNKNOWN}."
            self.disp.log_warning(msg, title)
            log_type = ACONST.TYPE_UNKNOWN

        if self._check_if_action_id_in_table(action_id) is False:
            msg = f"The action_id, {action_id},"
            msg += " is not in the Actions table."
            self.disp.log_error(msg, title)
            return self.error

        self.disp.log_debug(f"code = {code}", title)

        if code in ACONST.LOG_EQUIVALENCE:
            code_level = ACONST.LOG_EQUIVALENCE[code]
        else:
            code_level = ACONST.LOG_EQUIVALENCE[ACONST.CODE_UNKNOWN]

        self.disp.log_debug(f"code_level = {code_level}", title)

        if message is None:
            self.disp.log_warning(
                "The message is None, defaulting to the code message equivalence.", title
            )
            message = ACONST.LOG_MESSAGE_EQUIVALENCE[code_level]

        self.disp.log_debug(f"message = {message}", title)

        if isinstance(resolved, bool) is False:
            self.disp.log_warning(
                "The resolved status is not a boolean, defaulting to False.", title
            )
            resolved = False

        self.disp.log_debug(f"resolved = {resolved}", title)

        data = [
            "now",  # time
            f"{log_type}",  # type
            f"{action_id}",  # action_id
            f"{message}",  # message
            f"{code}",  # error_code
            f"{code_level}",  # error_level
            f"{int(resolved)}"  # resolved
        ]
        self.disp.log_debug(f"data = {data}", title)
        status = self.runtime_data.database_link.insert_data_into_table(
            table=CONST.TAB_ACTION_LOGGING,
            data=data,
            column=columns
        )
        self.disp.log_info(f"status = {status}", title)
        if status != self.success:
            self.disp.log_error("Failed to log the event.", title)
            return self.error
        return self.success

    def _check_if_action_id_in_table(self, action_id: int = 0) -> bool:
        """_summary_
            Check if the action_id is in the Actions table

        Args:
            action_id (int, optional): _description_. Defaults to 0.: The id of the concerned action.

        Returns:
            bool: _description_: Returns True if it is present, False otherwise.
        """
        title = "_check_if_action_id_in_table"
        self.disp.log_debug(f"action_id = {action_id}", title)
        data = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_ACTIONS,
            column="id",
            where=f"id='{action_id}'",
            beautify=False
        )
        self.disp.log_debug(f"data = {data}", title)
        if isinstance(data, int) is True and data != self.success:
            return False
        self.disp.log_debug(f"len(data) = {len(data)}", title)
        if len(data) == 1:
            return True
        return False

    def log_info(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an info event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_INFO,
            message=message,
            resolved=resolved
        )

    def log_success(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an success event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_SUCCESS,
            message=message,
            resolved=resolved
        )

    def log_debug(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an debug event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_DEBUG,
            message=message,
            resolved=resolved
        )

    def log_warning(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an warning event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_WARNING,
            message=message,
            resolved=resolved
        )

    def log_error(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an error event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_ERROR,
            message=message,
            resolved=resolved
        )

    def log_critical(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an critical event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_CRITICAL,
            message=message,
            resolved=resolved
        )

    def log_fatal(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an fatal event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_FATAL,
            message=message,
            resolved=resolved
        )

    def log_unknown(self, log_type: str, action_id: int = 0, message: Union[str, None] = None, resolved: bool = False) -> int:
        """_summary_
            Log an unknown event into the logging database

        Args:
            log_type (str): _description_: The type of the event
            action_id (int, optional): _description_: The id of the action that triggered the event, defaults to 0
            message (Union[str, None], optional): _description_: The message of the event, defaults to None
            resolved (bool, optional): _description_: The status of the event, defaults to False

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise
        """
        return self.log_event(
            log_type=log_type,
            action_id=action_id,
            code=ACONST.CODE_UNKNOWN,
            message=message,
            resolved=resolved
        )

    def get_logs(self, action_id: Union[int, None] = None, code: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            code (Union[int, None], optional): _description_: Specify a code to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        title = "get_logs"
        where = []
        if action_id is not None:
            where.append(f"action_id='{action_id}'")
        if code is not None:
            where.append(f"code='{code}'")
        if len(where) == 0:
            where = None
        self.disp.log_debug(f"where = {where}", title)
        data = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_ACTION_LOGGING,
            column="*",
            where=where,
            beautify=beautify
        )
        self.disp.log_debug(f"data = {data}", title)
        if isinstance(data, int) is True and data != self.success:
            self.disp.log_error("Failed to get the logs.", title)
            return self.error
        return data

    def get_logs_unknown(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the unknown logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_UNKNOWN,
            beautify=beautify
        )

    def get_logs_info(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the info logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_INFO,
            beautify=beautify
        )

    def get_logs_success(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the success logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_SUCCESS,
            beautify=beautify
        )

    def get_logs_debug(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the debug logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_DEBUG,
            beautify=beautify
        )

    def get_logs_warning(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the warning logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_WARNING,
            beautify=beautify
        )

    def get_logs_error(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the error logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_ERROR,
            beautify=beautify
        )

    def get_logs_critical(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the critical logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_CRITICAL,
            beautify=beautify
        )

    def get_logs_fatal(self, action_id: Union[int, None] = None, beautify: bool = True) -> Union[List[Union[Dict[str, Any], List[Any]]], int]:
        """_summary_
            Get the fatal logs from the database

        Args:
            action_id (Union[int, None], optional): _description_: Specify an action id to narrow down the results.
            beautify (bool, optional): _description_: Set to True if you wish to beautify the output

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: Returns the logs if it succeeds, self.error otherwise
        """
        return self.get_logs(
            action_id=action_id,
            code=ACONST.CODE_FATAL,
            beautify=beautify
        )

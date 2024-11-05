"""_summary_
    File in charge of testing the logger class for the actions
"""

import os
import sys
from typing import List, Dict, Any, Union

sys.path.append(os.path.join("..", os.getcwd()))
sys.path.append(os.getcwd())

try:
    import constants as TCONST
except ImportError as e:
    raise ImportError("Failed to import the unit test constants module") from e

try:
    from src.lib.actions import constants as ACONST
    from src.lib.actions.logger import ActionLogger
    from src.lib.sql.sql_manager import SQL
    from src.lib.components import constants as CONST
    from src.lib.components.runtime_data import RuntimeData
    from src.lib.boilerplates.non_web import BoilerplateNonHTTP
    from src.lib.boilerplates.responses import BoilerplateResponses
    from src.lib.components.password_handling import PasswordHandling
except ImportError as e:
    raise ImportError("Failed to import the src module") from e

ERROR = TCONST.ERROR
SUCCESS = TCONST.SUCCESS
DEBUG = TCONST.DEBUG


RDI = RuntimeData(TCONST.SERVER_HOST, TCONST.PORT, "Area", ERROR, SUCCESS)
BRI = BoilerplateResponses(
    runtime_data=RDI,
    debug=DEBUG
)
RDI.boilerplate_responses_initialised = BRI
RDI.boilerplate_non_http_initialised = BoilerplateNonHTTP(
    runtime_data_initialised=RDI,
    success=SUCCESS,
    error=ERROR,
    debug=DEBUG
)

SQLI = SQL(
    url=CONST.DB_HOST,
    port=CONST.DB_PORT,
    username=CONST.DB_USER,
    password=CONST.DB_PASSWORD,
    db_name=CONST.DB_DATABASE,
    debug=DEBUG
)
RDI.database_link = SQLI

RDI.boilerplate_responses_initialised = BRI

ACLI = ActionLogger(
    runtime_data=RDI,
    success=SUCCESS,
    error=ERROR,
    debug=DEBUG
)

PHI = PasswordHandling(
    error=ERROR,
    success=SUCCESS,
    debug=DEBUG
)

TEST_INFO = {
    "user_id": 0,
    "action_id": 0,
    "cache_busting": TCONST.CACHE_BUSTER_ADMIN
}


def _add_dummy_user() -> None:
    """_summary_
        Function in charge of adding a dummy user to the database.
    """
    columns: List[str] = SQLI.get_table_column_names(CONST.TAB_ACCOUNTS)
    if columns == ERROR:
        msg = f"Failed get data from table: {CONST.TAB_ACCOUNTS}"
        raise RuntimeError(msg)
    columns.pop(0)
    username = f"test_user_{TEST_INFO['cache_busting']}"
    email = f"test_email_{TEST_INFO['cache_busting']}@combobox.ttk"
    password = PHI.hash_password(f"test_password_{TEST_INFO['cache_busting']}")
    method = "local"
    favicon = "NULL"
    admin = "1"
    data = [
        username,
        email,
        password,
        method,
        favicon,
        admin
    ]
    status = SQLI.insert_data_into_table(
        table=CONST.TAB_ACCOUNTS,
        data=data,
        column=columns
    )
    if status == ERROR:
        msg = f"Failed to add user {username}"
        msg += f"to the database {CONST.TAB_ACCOUNTS}"
        raise RuntimeError(msg)
    usr_id = SQLI.get_data_from_table(
        table=CONST.TAB_ACCOUNTS,
        column="id",
        where=f"email='{email}'",
        beautify=False
    )
    if usr_id == ERROR:
        msg = f"Failed to get user id for {username}"
        raise RuntimeError(msg)
    TEST_INFO["user_id"] = usr_id[0][0]


def _add_dummy_action() -> None:
    """_summary_
        Function in charge of adding a dummy action to the database.
    """
    title = "_add_dummy_action"
    _add_dummy_user()
    columns: List[str] = SQLI.get_table_column_names(CONST.TAB_ACTIONS)
    if columns == ERROR:
        msg = f"Failed get data from table: {CONST.TAB_ACTIONS}"
        raise RuntimeError(msg)
    columns.pop(0)
    name = f"test_action_name_{TEST_INFO['cache_busting']}"
    trigger = f"test_trigger_{TEST_INFO['cache_busting']}"
    consequences = f"test_consequences_{TEST_INFO['cache_busting']}"
    user_id = str(TEST_INFO["user_id"])
    tags = "test_actions,will_not_run"
    running = f"{int(False)}"
    description = "This is an action that was generated during unit tests, it is thus not an action that can run."
    colour = "#00D9FFFF"
    favicon = "NULL"
    frequency = "0"
    data = [
        name,
        trigger,
        consequences,
        user_id,
        tags,
        running,
        description,
        colour,
        favicon,
        frequency
    ]
    status = SQLI.insert_data_into_table(
        table=CONST.TAB_ACTIONS,
        data=data,
        column=columns
    )
    if status != SUCCESS:
        msg = f"Failed to add action {name}"
        msg += f"to the database {CONST.TAB_ACTIONS}"
        raise RuntimeError(msg)
    action_id = SQLI.get_data_from_table(
        table=CONST.TAB_ACTIONS,
        column="id",
        where=f"name='{name}'",
        beautify=False
    )
    if action_id == ERROR:
        msg = f"Failed to get action id for {name}"
        raise RuntimeError(msg)
    TCONST.IDISP.log_debug(f"Gathered action: {action_id}", title)
    TEST_INFO["action_id"] = action_id[0][0]


def _remove_dummy_user() -> None:
    """_summary_
        Function in charge of removing the dummy user from the database.
    """
    _remove_dummy_action()
    SQLI.remove_data_from_table(
        CONST.TAB_ACCOUNTS,
        where=f"id={TEST_INFO['user_id']}"
    )


def _remove_dummy_action() -> None:
    """_summary_
        Function in charge of removing the dummy action from the database.
    """
    SQLI.remove_data_from_table(
        CONST.TAB_ACTIONS,
        where=f"id={TEST_INFO['action_id']}"
    )


def _remove_log_line(log_id: Union[int, Dict[str, int]]) -> None:
    """_summary_
        Function in charge of removing the log line from the database.

    Args:
        log_id (int): _description_
    """
    if isinstance(log_id, Dict):
        for i in log_id:
            SQLI.remove_data_from_table(
                CONST.TAB_ACTION_LOGGING,
                where=f"id={log_id[i]}"
            )
    else:
        SQLI.remove_data_from_table(
            CONST.TAB_ACTION_LOGGING,
            where=f"id={log_id}"
        )


def _get_log_lines(action_id: str = "") -> Dict[str, Any]:
    """_summary_
        Function in charge of getting the log line from the database.
    """
    node = action_id
    log_line = SQLI.get_data_from_table(
        table=CONST.TAB_ACTION_LOGGING,
        column="*",
        where=f"action_id='{node}'"
    )
    if log_line == ERROR:
        msg = f"Failed to get log line for {TEST_INFO['log_id']}"
        raise RuntimeError(msg)
    return log_line


def test_log_event_info() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_info"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_INFO
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_INFO
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_event_unknown() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_unknown"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_UNKNOWN
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_UNKNOWN
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_event_success() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_success"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_SUCCESS
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_SUCCESS
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_event_debug() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_debug"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_DEBUG
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_DEBUG
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_event_warning() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_warning"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_WARNING
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_WARNING
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_event_error() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_error"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_ERROR
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_ERROR
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_event_critical() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_critical"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_CRITICAL
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_CRITICAL
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_event_fatal() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_event_fatal"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_FATAL
    action_test_message = "This is a test message"
    action_resolved = False
    action_expected_level = ACONST.LEVEL_FATAL
    status = ACLI.log_event(
        log_type=action_type,
        action_id=action_id,
        code=action_code,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_success() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_success"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_SUCCESS
    action_test_message = "This is a test message"
    action_resolved = True
    action_expected_level = ACONST.LEVEL_SUCCESS
    status = ACLI.log_success(
        log_type=action_type,
        action_id=action_id,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_debug() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_debug"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_DEBUG
    action_test_message = "This is a test message"
    action_resolved = True
    action_expected_level = ACONST.LEVEL_DEBUG
    status = ACLI.log_debug(
        log_type=action_type,
        action_id=action_id,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_warning() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_warning"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_WARNING
    action_test_message = "This is a test message"
    action_resolved = True
    action_expected_level = ACONST.LEVEL_WARNING
    status = ACLI.log_warning(
        log_type=action_type,
        action_id=action_id,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_error() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_error"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_ERROR
    action_test_message = "This is a test message"
    action_resolved = True
    action_expected_level = ACONST.LEVEL_ERROR
    status = ACLI.log_error(
        log_type=action_type,
        action_id=action_id,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_critical() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_critical"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_CRITICAL
    action_test_message = "This is a test message"
    action_resolved = True
    action_expected_level = ACONST.LEVEL_CRITICAL
    status = ACLI.log_critical(
        log_type=action_type,
        action_id=action_id,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_fatal() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_fatal"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_FATAL
    action_test_message = "This is a test message"
    action_resolved = True
    action_expected_level = ACONST.LEVEL_FATAL
    status = ACLI.log_fatal(
        log_type=action_type,
        action_id=action_id,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_log_unknown() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_log_unknown"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_code = ACONST.CODE_UNKNOWN
    action_test_message = "This is a test message"
    action_resolved = True
    action_expected_level = ACONST.LEVEL_UNKNOWN
    status = ACLI.log_unknown(
        log_type=action_type,
        action_id=action_id,
        message=action_test_message,
        resolved=action_resolved,
    )
    TCONST.IDISP.log_debug(f"Log id = {status}", title)
    if status == ERROR:
        msg = "Failed to log the event."
        TCONST.IDISP.log_error(msg, title)
        _remove_dummy_user()
        assert status == SUCCESS
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    _remove_log_line(data[0]["id"])
    _remove_dummy_user()
    data = data[0]
    assert data["type"] == action_type
    assert str(data["action_id"]) == str(action_id)
    assert data["message"] == action_test_message
    assert str(data["code"]) == str(action_code)
    assert data["level"] == action_expected_level
    assert str(data["resolved"]) == str(int(action_resolved))


def test_get_logs() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    data = _get_log_lines(action_id)
    TCONST.IDISP.log_debug(f"Gathered data: {data}", title)
    user_logs = ACLI.get_logs(
        action_id=action_id, code=None, beautify=True
    )
    TCONST.IDISP.log_debug(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    index = 0
    for log in user_logs:
        action_code = ACONST.LIST_CODE[index]
        action_level = ACONST.LIST_LEVEL_INFO[index]
        index += 1
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_unknown() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_unknown"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_unknown(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_UNKNOWN
        action_level = ACONST.LEVEL_UNKNOWN
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_info() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_info"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_info(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_INFO
        action_level = ACONST.LEVEL_INFO
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_success() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_success"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_success(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_SUCCESS
        action_level = ACONST.LEVEL_SUCCESS
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_debug() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_debug"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_debug(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_DEBUG
        action_level = ACONST.LEVEL_DEBUG
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_warning() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_warning"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_warning(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_WARNING
        action_level = ACONST.LEVEL_WARNING
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_error() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_error"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_error(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_ERROR
        action_level = ACONST.LEVEL_ERROR
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_critical() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_critical"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_critical(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_CRITICAL
        action_level = ACONST.LEVEL_CRITICAL
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))


def test_get_logs_fatal() -> None:
    """_summary_
        Function in charge of testing the log_event function.
    """
    title = "test_get_logs_fatal"
    _add_dummy_action()
    action_id = TEST_INFO["action_id"]
    action_type = ACONST.TYPE_ACTION
    action_test_message = "This is a test message"
    action_resolved = True
    log_ids = {}
    for code in ACONST.LIST_CODE:
        status = ACLI.log_event(
            log_type=action_type,
            action_id=action_id,
            code=code,
            message=action_test_message,
            resolved=action_resolved,
        )
        if status != ERROR:
            node = _get_log_lines(action_id)
            if len(node) > 0:
                node = node[-1]
                log_ids[code] = node['id']
        if status == ERROR:
            msg = "Failed to log the event."
            TCONST.IDISP.log_error(msg, title)
            _remove_log_line(log_ids)
            _remove_dummy_user()
            assert status != ERROR
    TCONST.IDISP.log_debug(f"Log ids = {log_ids}", title)
    user_logs = ACLI.get_logs_fatal(
        action_id=action_id, beautify=True
    )
    print(f"Gathered user logs = {user_logs}", title)
    _remove_log_line(log_ids)
    _remove_dummy_user()
    TCONST.IDISP.log_debug(f"logs = {user_logs}", title)
    for log in user_logs:
        action_code = ACONST.CODE_FATAL
        action_level = ACONST.LEVEL_FATAL
        assert log["type"] == action_type
        assert str(log["action_id"]) == str(action_id)
        assert log["message"] == action_test_message
        assert str(log["code"]) == str(action_code)
        assert log["level"] == action_level
        assert str(log["resolved"]) == str(int(action_resolved))

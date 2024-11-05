"""_summary_
    File in charge of testing the variables class
"""
import os
import sys

sys.path.append(os.path.join("..", os.getcwd()))
sys.path.append(os.getcwd())

try:
    import constants as TCONST
except ImportError as e:
    raise ImportError("Failed to import the unit test constants module") from e

try:
    from src.lib.actions import constants as ACONST
except ImportError as e:
    raise ImportError("Failed to import the src module") from e


ERROR = TCONST.ERROR
SUCCESS = TCONST.SUCCESS
DEBUG = TCONST.DEBUG

spaceship = ACONST._spaceship


def test_log_types() -> None:
    """_summary_
        Function in charge of testing the log types.
    """
    assert ACONST.TYPE_UNKNOWN == "UNKNOWN LOGGING TYPE"
    assert ACONST.TYPE_API == "API"
    assert ACONST.TYPE_SERVICE == "SERVICE"
    assert ACONST.TYPE_SERVICE_TRIGGER == "SERVICE TRIGGER"
    assert ACONST.TYPE_SERVICE_ACTION == "SERVICE ACTION"
    assert ACONST.TYPE_ACTION == "ACTION"
    assert ACONST.TYPE_UNDEFINED == "UNDEFINED"
    assert ACONST.TYPE_MISMATCH == "MISMATCH"
    assert ACONST.TYPE_BEFORE_ASSIGNEMENT == "REFERENCED BEFORE ASSIGNEMENT"
    assert ACONST.TYPE_DIV_ZERO == "DIVISION BY ZERO"
    assert ACONST.TYPE_SYNTAX_ERROR == "SYNTAX ERROR"
    assert ACONST.TYPE_RUNTIME_ERROR == "RUNTIME ERROR"
    assert ACONST.TYPE_INCOMPARABLE == "INCOMPARABLE TYPES"
    assert ACONST.TYPE_OVERFLOW == "VALUE OVERFLOW"
    assert ACONST.TYPE_UNDERFLOW == "VALUE UNDERFLOW"


def test_error_codes() -> None:
    """_summary_
        Function in charge of testing the error codes.
    """
    assert ACONST.CODE_UNKNOWN == -1
    assert ACONST.CODE_INFO == 0
    assert ACONST.CODE_SUCCESS == 1
    assert ACONST.CODE_DEBUG == 2
    assert ACONST.CODE_WARNING == 3
    assert ACONST.CODE_ERROR == 4
    assert ACONST.CODE_CRITICAL == 5
    assert ACONST.CODE_FATAL == 6


def test_error_level() -> None:
    """_summary_
        Function in charge of testing the error levels.
    """
    assert ACONST.LEVEL_UNKNOWN == "UNKNOWN"
    assert ACONST.LEVEL_INFO == "INFO"
    assert ACONST.LEVEL_SUCCESS == "SUCCESS"
    assert ACONST.LEVEL_DEBUG == "DEBUG"
    assert ACONST.LEVEL_WARNING == "WARNING"
    assert ACONST.LEVEL_ERROR == "ERROR"
    assert ACONST.LEVEL_CRITICAL == "CRITICAL"
    assert ACONST.LEVEL_FATAL == "FATAL"


def test_error_messages() -> None:
    """_summary_
        Function in charge of testing the error messages.
    """
    assert ACONST.MSG_UNKNOWN == "Unknown: Operation executed with unknown status."
    assert ACONST.MSG_INFO == "Information: Operation executed without any issues."
    assert ACONST.MSG_SUCCESS == "Success: Operation completed successfully."
    assert ACONST.MSG_DEBUG == "Debug: Tracking detailed operational data for diagnostics."
    assert ACONST.MSG_WARNING == "Warning: Potential issue detected. Review is recommended."
    assert ACONST.MSG_ERROR == "Error: Operation could not be completed successfully."
    assert ACONST.MSG_CRITICAL == "Critical: Immediate attention required to prevent severe impact."
    assert ACONST.MSG_FATAL == "Fatal: System failure imminent. Immediate intervention necessary."


def test_log_equivalence() -> None:
    """_summary_
        Function in charge of testing the error equivalence.
    """
    assert ACONST.LOG_EQUIVALENCE == {
        ACONST.CODE_UNKNOWN: ACONST.LEVEL_UNKNOWN,
        ACONST.CODE_INFO: ACONST.LEVEL_INFO,
        ACONST.CODE_SUCCESS: ACONST.LEVEL_SUCCESS,
        ACONST.CODE_DEBUG: ACONST.LEVEL_DEBUG,
        ACONST.CODE_WARNING: ACONST.LEVEL_WARNING,
        ACONST.CODE_ERROR: ACONST.LEVEL_ERROR,
        ACONST.CODE_CRITICAL: ACONST.LEVEL_CRITICAL,
        ACONST.CODE_FATAL: ACONST.LEVEL_FATAL,
    }


def test_log_message_equivalence() -> None:
    """_summary_
        Function in charge of testing the error message equivalence.
    """
    assert ACONST.LOG_MESSAGE_EQUIVALENCE == {
        ACONST.CODE_UNKNOWN: ACONST.MSG_UNKNOWN,
        ACONST.CODE_INFO: ACONST.MSG_INFO,
        ACONST.CODE_SUCCESS: ACONST.MSG_SUCCESS,
        ACONST.CODE_DEBUG: ACONST.MSG_DEBUG,
        ACONST.CODE_WARNING: ACONST.MSG_WARNING,
        ACONST.CODE_ERROR: ACONST.MSG_ERROR,
        ACONST.CODE_CRITICAL: ACONST.MSG_CRITICAL,
        ACONST.CODE_FATAL: ACONST.MSG_FATAL,
    }


def test_list_type_equivalence() -> None:
    """_summary_
        Function in charge of testing the list type equivalence.
    """
    assert ACONST.LIST_TYPE == [
        ACONST.TYPE_UNKNOWN,
        ACONST.TYPE_API,
        ACONST.TYPE_SERVICE,
        ACONST.TYPE_SERVICE_TRIGGER,
        ACONST.TYPE_SERVICE_ACTION,
        ACONST.TYPE_ACTION,
        ACONST.TYPE_UNDEFINED,
        ACONST.TYPE_MISMATCH,
        ACONST.TYPE_BEFORE_ASSIGNEMENT,
        ACONST.TYPE_DIV_ZERO,
        ACONST.TYPE_SYNTAX_ERROR,
        ACONST.TYPE_RUNTIME_ERROR,
        ACONST.TYPE_INCOMPARABLE,
        ACONST.TYPE_OVERFLOW,
        ACONST.TYPE_UNDERFLOW,
    ]


def test_list_code_equivalence() -> None:
    """_summary_
        Function in charge of testing the list code equivalence.
    """
    assert ACONST.LIST_CODE == [
        ACONST.CODE_UNKNOWN,
        ACONST.CODE_INFO,
        ACONST.CODE_SUCCESS,
        ACONST.CODE_DEBUG,
        ACONST.CODE_WARNING,
        ACONST.CODE_ERROR,
        ACONST.CODE_CRITICAL,
        ACONST.CODE_FATAL,
    ]


def test_list_info_equivalence() -> None:
    """_summary_
        Function in charge of testing the list info equivalence.
    """
    assert ACONST.LIST_LEVEL_INFO == [
        ACONST.LEVEL_UNKNOWN,
        ACONST.LEVEL_INFO,
        ACONST.LEVEL_SUCCESS,
        ACONST.LEVEL_DEBUG,
        ACONST.LEVEL_WARNING,
        ACONST.LEVEL_ERROR,
        ACONST.LEVEL_CRITICAL,
        ACONST.LEVEL_FATAL,
    ]


def test_list_msg_equivalence() -> None:
    """_summary_
        Function in charge of testing the list message equivalence.
    """
    assert ACONST.LIST_MSG == [
        ACONST.MSG_UNKNOWN,
        ACONST.MSG_INFO,
        ACONST.MSG_SUCCESS,
        ACONST.MSG_DEBUG,
        ACONST.MSG_WARNING,
        ACONST.MSG_ERROR,
        ACONST.MSG_CRITICAL,
        ACONST.MSG_FATAL,
    ]


def test_spaceship_less_than() -> None:
    """_summary_
        Function in charge of testing the spaceship less than operator.
    """
    assert spaceship(2, 3) == -1  # 2 < 3


def test_spaceship_equal() -> None:
    """_summary_
        Function in charge of testing the spaceship equal operator.
    """
    assert spaceship(5, 5) == 0   # 5 == 5


def test_spaceship_greater_than() -> None:
    """_summary_
        Function in charge of testing the spaceship greater than operator.
    """
    assert spaceship(7, 4) == 1   # 7 > 4


def test_spaceship_negative_comparison() -> None:
    """_summary_
        Function in charge of testing the spaceship negative comparison.
    """
    assert spaceship(-1, -2) == 1  # -1 > -2


def test_spaceship_zero_comparison() -> None:
    """_summary_
        Function in charge of testing the spaceship zero comparison.
    """
    assert spaceship(0, 0) == 0    # 0 == 0


def test_spaceship_float_comparison() -> None:
    """_summary_
        Function in charge of testing the spaceship float comparison.
    """
    assert spaceship(2.5, 2.5) == 0  # 2.5 == 2.5
    assert spaceship(2.5, 3.0) == -1  # 2.5 < 3.0
    assert spaceship(3.0, 2.5) == 1   # 3.0 > 2.5


def test_spaceship_string_comparison() -> None:
    """_summary_
        Function in charge of testing the spaceship string
    """
    assert spaceship("apple", "banana") == -1  # "apple" < "banana"
    assert spaceship("cherry", "apple") == 1   # "cherry" > "apple"
    assert spaceship("date", "date") == 0      # "date" == "date"

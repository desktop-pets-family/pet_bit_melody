"""_summary_
    File in charge of testing the boilerplate Boilerplate non http class.
"""
import os
import sys
from datetime import datetime
import constants as TCONST


import pytest

sys.path.append(os.getcwd())

try:
    from src.lib.sql.sql_manager import SQL
    from src.lib.components import constants as CONST
except ImportError as e:
    raise ImportError("Failed to import the src module") from e

ERROR = TCONST.ERROR
SUCCESS = TCONST.SUCCESS
DEBUG = TCONST.DEBUG

SI = SQL(
    url=CONST.DB_HOST,
    port=CONST.DB_PORT,
    username=CONST.DB_USER,
    password=CONST.DB_PASSWORD,
    db_name=CONST.DB_DATABASE,
    debug=DEBUG
)


def _datetime_to_date_str(date: datetime) -> str:
    """_summary_
        Function in charge of converting a datetime object to a string.
    """
    return date.strftime("%Y-%m-%d")


def _datetime_to_datetime_str(date: datetime) -> str:
    """_summary_
        Function in charge of converting a datetime object to a string.
    """
    return date.strftime("%Y-%m-%d %H:%M:%S")


def _datetime_to_sql_time_str(date: datetime) -> str:
    """_summary_
        Function in charge of converting a datetime object to a string.
    """
    microsecond = date.strftime("%f")[:3]
    converted_time = date.strftime("%Y-%m-%d %H:%M:%S")
    return f"{converted_time}.{microsecond}"


def _str_to_datetime(string: str) -> datetime:
    """_summary_
        Function in charge of converting a string to a datetime object.
    """
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


def _str_to_date(string: str) -> datetime:
    """_summary_
        Function in charge of converting a string to a datetime object.
    """
    return datetime.strptime(string, "%Y-%m-%d")


def test_datetime_to_datetime_string_no_error() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """
    test = datetime.now()
    test_data = SI.datetime_to_string(test, date_only=False, sql_mode=False)
    correct_data = _datetime_to_datetime_str(test)
    assert test_data is not None
    assert test_data == correct_data


def test_datetime_to_sql_string_no_error() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """
    test = datetime.now()
    test_data = SI.datetime_to_string(test, date_only=False, sql_mode=True)
    correct_data = _datetime_to_sql_time_str(test)
    assert test_data is not None
    assert test_data == correct_data


def test_datetime_to_date_string_no_error() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """
    test = datetime.now()
    test_data = SI.datetime_to_string(test, date_only=True, sql_mode=False)
    correct_data = _datetime_to_date_str(test)
    assert test_data is not None
    assert test_data == correct_data


def test_datetime_to_date_sql_string_no_error() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """
    test = datetime.now()
    test_data = SI.datetime_to_string(test, date_only=True, sql_mode=True)
    correct_data = _datetime_to_date_str(test)
    assert test_data is not None
    assert test_data == correct_data


def test_datetime_to_datetime_string_not_a_datetime_instance() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """
    test = "test"
    with pytest.raises(ValueError):
        SI.datetime_to_string(test, date_only=False, sql_mode=False)


def test_datetime_to_sql_string_not_a_datetime_instance() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """
    test = "test"
    with pytest.raises(ValueError):
        SI.datetime_to_string(test, date_only=False, sql_mode=True)


def test_datetime_to_date_string_not_a_datetime_instance() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """

    test = "test"
    with pytest.raises(ValueError):
        SI.datetime_to_string(test, date_only=True, sql_mode=False)


def test_datetime_to_date_sql_string_not_a_datetime_instance() -> None:
    """_summary_
        Function in charge of testing the datetime_to_string function.
    """

    test = "test"
    with pytest.raises(ValueError):
        SI.datetime_to_string(test, date_only=True, sql_mode=True)


def test_string_to_datetime_no_error() -> None:
    """_summary_
        Function in charge of testing the string_to_datetime function.
    """
    node = datetime.now()
    test = _str_to_datetime(node)
    test_data = SI.string_to_datetime(test, date_only=False)
    assert test_data is not None
    assert test_data == node


def test_string_to_date_datetime_no_error() -> None:
    """_summary_
        Function in charge of testing the string_to_datetime function.
    """
    node = datetime.now()
    test = _str_to_date(node)
    test_data = SI.string_to_datetime(test, date_only=True)
    assert test_data is not None
    assert test_data == node


def test_string_to_datetime_datetime_not_a_string_instance() -> None:
    """_summary_
        Function in charge of testing the string_to_datetime function.
    """
    test = datetime.now()
    with pytest.raises(ValueError):
        SI.string_to_datetime(test, date_only=False)


def test_string_to_date_datetime_not_a_string_instance() -> None:
    """_summary_
        Function in charge of testing the string_to_datetime function.
    """

    test = datetime.now()
    with pytest.raises(ValueError):
        SI.string_to_datetime(test, date_only=True)


def test_string_to_datetime_datetime_not_a_datetime_string_instance() -> None:
    """_summary_
        Function in charge of testing the string_to_datetime function.
    """
    test = "test"
    with pytest.raises(ValueError):
        SI.string_to_datetime(test, date_only=False)


def test_string_to_date_datetime_not_a_datetime_string_instance() -> None:
    """_summary_
        Function in charge of testing the string_to_datetime function.
    """

    test = "test"
    with pytest.raises(ValueError):
        SI.string_to_datetime(test, date_only=True)

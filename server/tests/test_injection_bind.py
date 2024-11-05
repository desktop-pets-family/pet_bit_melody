"""_summary_
    File in charge of testing the boilerplate Boilerplate non http class.
"""
import os
import sys
from typing import List
import constants as TCONST


sys.path.append(os.getcwd())

try:
    from src.lib.sql.sql_injection import SQLInjection
except ImportError as e:
    raise ImportError("Failed to import the src module") from e

DEBUG = TCONST.DEBUG
ERROR = TCONST.ERROR
SUCCESS = TCONST.SUCCESS

SENTENCES = [
    "SHOW TABLES;",
    "SHOW Databases;",
    "DROP TABLES;",
    "SHOW DATABASE;",
    "SELECT * FROM table;",
]

SQLII = SQLInjection(
    error=ERROR,
    success=SUCCESS,
    debug=DEBUG
)


def _run_test(array: List[str], function: object, expected_response: bool = False) -> None:
    """ Run a test and return it's status"""
    for i in array:
        response = function(i)
        assert response == expected_response


def test_if_logic_gate_sql_injection_list_logic_gates() -> None:
    """_summary_
        Function in charge of testing the logic gate for sql injection.
    """
    _run_test(
        array=SQLII.logic_gates,
        function=SQLII.check_if_logic_gate_sql_injection,
        expected_response=True
    )


def test_if_command_sql_injection_list_keywords() -> None:
    """_summary_
        Function in charge of testing the command for sql injection.
    """
    _run_test(
        array=SQLII.keywords,
        function=SQLII.check_if_command_sql_injection,
        expected_response=True
    )


def test_if_symbol_sql_injection_list_symbols() -> None:
    """_summary_
        Function in charge of testing the symbol for sql injection.
    """
    _run_test(
        array=SQLII.symbols,
        function=SQLII.check_if_symbol_sql_injection,
        expected_response=True
    )


def test_if_sql_injection_list_all() -> None:
    """_summary_
        Function in charge of testing the list of all sql injections.
    """
    _run_test(
        array=SQLII.all,
        function=SQLII.check_if_sql_injection,
        expected_response=True
    )


def test_if_injections_in_strings_list_list_all() -> None:
    """_summary_
        Function in charge of testing the list of all sql injections in strings.
    """
    _run_test(
        array=[SQLII.all],
        function=SQLII.check_if_injections_in_strings,
        expected_response=True
    )


def test_if_injections_in_strings_list_list_all_list_all() -> None:
    """_summary_
        Function in charge of testing the list of all sql injections in strings.
    """
    _run_test(
        array=[SQLII.all, SQLII.all],
        function=SQLII.check_if_injections_in_strings,
        expected_response=True
    )


def test_if_sql_injection_list_sentence() -> None:
    """_summary_
        Function in charge of testing the list of a series of sentences
    """
    _run_test(
        array=SENTENCES,
        function=SQLII.check_if_sql_injection,
        expected_response=True,
    )

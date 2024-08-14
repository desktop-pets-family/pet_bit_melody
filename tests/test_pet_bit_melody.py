# tests/test_tty_ov.py

import pytest
import unittest
import unittest.mock
from sys import stderr
from pet_bit_melody import PetBitMelody


ERR = 84
ERROR = ERR
SUCCESS = 0


def print_debug(string: str = "") -> None:
    """ Print debug messages """
    debug = False
    if debug is True:
        print(f"DEBUG: {string}", file=stderr)


def test_sample_status() -> None:
    """ Test if a return status corresponds to the expected one """
    response = SUCCESS
    assert response is SUCCESS


@unittest.mock.patch('builtins.input', side_effect=["an_answer"])
def test_sample_input(mock_input) -> None:
    """ Test if the input provided by the sample test provides the exptected response """
    response = input("a_question")
    assert response == "an_answer"


def test_sample_output(capsys) -> None:
    """ Test if the displayed output corresponds to the expected one """
    string_input = "Hello world !"
    print(string_input)
    captured = capsys.readouterr()

    assert captured.out == f"{string_input}\n"

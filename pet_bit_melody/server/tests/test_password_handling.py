"""_summary_
    File in charge of testing the http response codes.
"""
import os
import sys

sys.path.append(os.getcwd())
try:
    from src.lib.components.password_handling import PasswordHandling
except ImportError as e:
    raise ImportError("Failed to import the src module") from e

DUMMY_PASSWORD = "some_password"
WRONG_PASSWORD = "some_other_password"
PHI = PasswordHandling()
HASHED_PASSWORD = PHI.hash_password(DUMMY_PASSWORD)


def test_correct_password() -> None:
    """_summary_
        Function in charge of testing if the current password is the same as the hashed version.
    """
    assert PHI.check_password(DUMMY_PASSWORD, HASHED_PASSWORD) is True


def test_wrong_password() -> None:
    """_summary_
        Function in charge of testing if the current password is not the same as the hashed version.
    """
    assert PHI.check_password(WRONG_PASSWORD, HASHED_PASSWORD) is False

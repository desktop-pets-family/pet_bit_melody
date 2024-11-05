"""_summary_
    File in charge of testing the background task scheduler function.
"""

import os
import sys
from typing import Any
from time import sleep
from datetime import datetime

import pytest
from apscheduler.job import Job
import constants as TCONST

sys.path.append(os.getcwd())
try:
    from src.lib.components.background_tasks import BackgroundTasks
except ImportError as e:
    raise ImportError("Failed to import the src module") from e


# Constants
SUCCESS = TCONST.SUCCESS
ERROR = TCONST.ERROR
DEBUG = TCONST.DEBUG

# Create a test function for each test scenario


def test_current_date(*args: Any) -> None:
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
        print(f"(test_current_date) (Called) Current date: {date()}")
    else:
        print(f"(test_current_date) (Not called) Current date: {date}",)


def hello_world() -> None:
    """_summary_
        This is a test function that will print "Hello, World!"
    """
    print("Hello, World!")


def pending_world() -> None:
    """_summary_
        This is a test function that will print "Pending, World!"
    """
    print("Pending, World!")


def goodbye_world() -> None:
    """_summary_
        This is a test function that will print "Goodbye, World!"
    """
    print("Goodbye, World!")


def test_initialization():
    """
    Test that BackgroundTasks initializes with correct parameters.
    """
    bgt = BackgroundTasks(success=SUCCESS, error=ERROR, debug=DEBUG)
    status_success = bgt.success
    status_error = bgt.error
    status_debug = bgt.debug
    del bgt
    assert status_success == SUCCESS
    assert status_error == ERROR
    assert status_debug is DEBUG


def test_add_task():
    """
    Test safe_add_task adds a task successfully.
    """

    def mock_func():
        return "mocked function"

    bgt = BackgroundTasks(success=SUCCESS, error=ERROR, debug=DEBUG)

    status = bgt.safe_add_task(
        func=mock_func,
        args=None,
        kwargs=None,
        trigger="interval",
        seconds=2
    )
    status = isinstance(status, Job)
    del bgt
    assert status is True, "Task failed to be added"


def test_scheduler_start_stop():
    """
    Test that the scheduler starts and stops correctly.
    """
    bgt = BackgroundTasks(success=SUCCESS, error=ERROR, debug=DEBUG)
    status_start = bgt.safe_start()
    status_stop = bgt.safe_stop(wait=True)
    del bgt

    assert status_start == SUCCESS
    assert status_stop == SUCCESS


def test_multiple_tasks():
    """
    Test adding multiple tasks to the scheduler.
    """

    bgt = BackgroundTasks(success=SUCCESS, error=ERROR, debug=DEBUG)

    status_task1 = bgt.safe_add_task(
        func=test_current_date,
        args=(datetime.now,),
        kwargs=None,
        trigger="interval",
        seconds=2
    )
    status_task2 = bgt.add_task(
        hello_world,
        args=None,
        kwargs=None,
        trigger="interval",
        seconds=2
    )
    status_task3 = bgt.safe_add_task(
        pending_world,
        args=None,
        kwargs=None,
        trigger="interval",
        seconds=2
    )
    status_task4 = bgt.add_task(
        goodbye_world,
        args=None,
        kwargs=None,
        trigger="interval",
        seconds=2
    )
    status_start = bgt.safe_start()
    sleep(10)
    status_stop = bgt.safe_stop(wait=True)
    status_task1 = isinstance(status_task1, Job)
    status_task2 = isinstance(status_task2, Job)
    status_task3 = isinstance(status_task3, Job)
    status_task4 = isinstance(status_task4, Job)
    del bgt

    assert status_task1 is True
    assert status_task2 is True
    assert status_task3 is True
    assert status_task4 is True
    assert status_start == SUCCESS
    assert status_stop == SUCCESS


def test_invalid_task():
    """
    Test that adding an invalid task (non-callable) raises an error.
    """
    bgt = BackgroundTasks(success=SUCCESS, error=ERROR, debug=DEBUG)

    with pytest.raises(ValueError):
        bgt.add_task(
            func="not_callable",  # this is invalid
            args=None,
            kwargs=None,
            trigger="interval",
            seconds=2
        )


def test_safe_methods():
    """
    Test safe methods like safe_pause, safe_resume.
    """
    bgt = BackgroundTasks(success=SUCCESS, error=ERROR, debug=DEBUG)
    status_start = bgt.safe_start()
    status_pause = bgt.safe_pause(pause=True)
    status_resume = bgt.safe_resume()
    status_stop = bgt.safe_stop(wait=True)
    del bgt

    assert status_start == SUCCESS
    assert status_pause == SUCCESS
    assert status_resume == SUCCESS
    assert status_stop == SUCCESS

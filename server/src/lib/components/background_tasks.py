##
# EPITECH PROJECT, 2024
# Terarea
# File description:
# crons.py
##

"""
    File in charge of setting up the cron jobs for the server.
"""

from typing import Union, Any, Dict, Tuple
from apscheduler.job import Job
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerAlreadyRunningError, SchedulerNotRunningError
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME


class BackgroundTasks:
    """_summary_
        This is the class that is in charge of scheduling background tasks that need to run on intervals
    """

    def __init__(self, success: int = 0, error: int = 84, debug: bool = False) -> None:
        # -------------------------- Inherited values --------------------------
        self.success: int = success
        self.error: int = error
        self.debug: bool = debug
        # ------------------------ The scheduler class  ------------------------
        self.scheduler = BackgroundScheduler()
        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def __del__(self) -> None:
        """_summary_
            The destructor of the class
        """
        self.disp.log_info("Stopping background tasks.", "__del__")
        exit_code = self.safe_stop()
        msg = f"The cron exited with status {exit_code}."
        if exit_code != self.success:
            self.disp.log_error(msg, "__del__")
        else:
            self.disp.log_debug(msg, "__del__")

    def safe_add_task(self, func: callable, args: Union[Tuple, None] = None, kwargs: Union[Dict, None] = None, trigger: Union[str, Any] = "interval", seconds: int = 5) -> Union[int, Job]:
        """_summary_
            A non-crashing implementation of the add_task function.

        Args:
            func (callable): _description_: The function to be called when it is time to run the job
            args (Union[Tuple, None], optional): _description_. Defaults to None.: Arguments you wish to pass to the function when executed.
            kwargs (Union[Dict, None], optional): _description_. Defaults to None.: Arguments you wish to pass to the function when executed.
            trigger (Union[str, Any], optional): _description_. Defaults to "interval".
            seconds (int, optional): _description_. Defaults to 5. The amount of seconds to wait before executing the task again (I don't think it is effective for the cron option)

        Returns:
            Union[int, Job]: _description_: returns self.error if there was an error, otherwise, returns a Job instance.
        """
        try:
            return self.add_task(
                func=func,
                args=args,
                kwargs=kwargs,
                trigger=trigger,
                seconds=seconds
            )
        except ValueError as e:
            self.disp.log_error(
                f"Runtime Error for add_task. {e}",
                "safe_add_task"
            )
            return self.error

    def safe_start(self) -> int:
        """_summary_
            This function is in charge of starting the scheduler. In a non-breaking way.

        Returns:
            int: _description_: Will return self.success if it worked, otherwise self.error.
        """
        try:
            return self.start()
        except RuntimeError as e:
            self.disp.log_error(
                f"Runtime Error for start. {e}",
                "safe_start"
            )
            return self.error

    def safe_pause(self, pause: bool = True) -> int:
        """_summary_
            This function is in charge of pausing the scheduler. In a non-breaking way.

        Args:
            pause (bool, optional): _description_: This is the boolean that will determine if the scheduler should be paused or not. Defaults to True.

        Returns:
            int: _description_: Will return self.success if it worked, otherwise self.error
        """
        try:
            return self.pause(pause=pause)
        except RuntimeError as e:
            self.disp.log_error(
                f"Runtime Error for start. {e}",
                "safe_pause"
            )
            return self.error

    def safe_resume(self) -> int:
        """_summary_
            This function is in charge of resuming the scheduler. In a non-breaking way.

        Returns:
            int: _description_: Will return self.success if it worked, otherwise self.error.
        """
        try:
            return self.resume()
        except RuntimeError as e:
            self.disp.log_error(
                f"Runtime Error for start. {e}",
                "safe_resume"
            )
            return self.error

    def safe_stop(self, wait: bool = True) -> int:
        """_summary_
            This function is in charge of stopping the scheduler. In a non-breaking way.

        Args:
            wait (bool, optional): _description_: Wait for the running tasks to finish. Defaults to True.

        Returns:
            int: _description_: will return self.success if it succeeds, otherwise self.error
        """
        try:
            return self.stop(wait=wait)
        except RuntimeError as e:
            self.disp.log_error(
                f"Runtime Error for start. {e}",
                "safe_stop"
            )
            return self.error

    def _to_dict(self, data: Union[Any, None] = None) -> dict:
        """_summary_
            Convert any data input into a dictionnary.
        Args:
            data (Union[Any, None], optional): _description_. Defaults to None. This is the data you are providing.

        Returns:
            dict: _description_: A dictionnary crea ted with what could be extracted from the data.
        """
        if data is None:
            return {"none": None}
        if isinstance(data, dict) is True:
            return data
        if isinstance(data, (list, tuple)) is True:
            res = {}
            for i in list(data):
                res[i] = None
            return res
        return {"data": data}

    def add_task(self, func: callable, args: Union[Tuple, None] = None, kwargs: Union[Dict, None] = None, trigger: Union[str, Any] = "interval",  seconds: int = 5) -> Union[Job, None]:
        """_summary_
            Function in charge of adding an automated call to functions that are meant to run in the background.
            They are meant to run on interval.

        Args:
            func (callable): _description_: The function to be called when it is time to run the job
            args (Union[Tuple, None], optional): _description_. Defaults to None.: Arguments you wish to pass to the function when executed.
            kwargs (Union[Dict, None], optional): _description_. Defaults to None.: Arguments you wish to pass to the function when executed.
            trigger (Union[str, Any], optional): _description_. Defaults to "interval".
            seconds (int, optional): _description_. Defaults to 5. The amount of seconds to wait before executing the task again (I don't think it is effective for the cron option)

        Returns:
            Union[int,Job]: _description_: will raise a ValueError when an error occurs, otherwise, returns an instance of Job. 
        """
        if callable(func) is False:
            self.disp.log_error(
                f"The provided function is not callable: {func}.",
                "add_task"
            )
            raise ValueError("The function must be callable.")
        if args is not None and isinstance(args, tuple) is False:
            msg = f"The provided args for {func.__name__} are not tuples.\n"
            msg += f"Converting args: '{args}'  to tuples."
            self.disp.log_warning(msg, "add_task")
            args = tuple((args,))
        if kwargs is not None and isinstance(kwargs, dict) is False:
            msg = f"The provided kwargs for {func.__name__}"
            msg += "are not dictionaries.\n"
            msg += f"Converting kwargs: '{kwargs}' to dictionaries."
            self.disp.log_warning(msg, "add_task")
            kwargs = self._to_dict(kwargs)
            self.disp.log_warning(f"Converted data = {kwargs}.", "add_task")
        if trigger is not None and isinstance(trigger, str) is False:
            self.disp.log_error(
                f"The provided trigger is not a string: {trigger}.",
                "add_task"
            )
            raise ValueError("The trigger must be a string.")
        if isinstance(seconds, int) is False:
            self.disp.log_error(
                f"The provided seconds is not an integer: {seconds}.",
                "add_task"
            )
            raise ValueError("The seconds must be an integer.")
        msg = f"Adding job: {func.__name__} "
        msg += f"with trigger: {trigger}, "
        msg += f"seconds = {seconds}, "
        msg += f"args = {args}, "
        msg += f"kwargs = {kwargs}."
        self.disp.log_debug(msg, "add_task")
        return self.scheduler.add_job(
            func=func,
            trigger=trigger,
            seconds=seconds,
            args=args,
            kwargs=kwargs
        )

    def start(self) -> Union[int, None]:
        """_summary_
            The function in charge of starting the scheduler loop.

        Raises:
            RuntimeError: _description_: Will raise a runtile error if the underlying functions failled.

        Returns:
            Union[int, None]: _description_: Will return self.success if it worked, otherwise None because it will have raised an error.
        """
        try:
            self.scheduler.start()
            self.disp.log_info("Scheduler started...", "start")
            return self.success
        except SchedulerAlreadyRunningError:
            self.disp.log_info("Scheduler is already running...", "start")
            return self.success
        except RuntimeError as e:
            self.disp.log_error(
                f"An error occurred while starting the scheduler: {e}",
                "start"
            )
            msg = f"Error({self.__class__.__name__}): "
            msg += "Failed to call the scheduler's start wrapper function."
            raise RuntimeError(msg) from e
        except Exception as e:
            self.disp.log_error(
                f"An error occurred while starting the scheduler: {e}", "start"
            )
            msg = f"Error({self.__class__.__name__}): "
            msg += "Failed to call the scheduler's start wrapper function."
            raise RuntimeError(msg) from e

    def pause(self, pause: bool = True) -> Union[int, None]:
        """_summary_
            This function is in charge of pausing the scheduler if it was running.

        Args:
            pause (bool, optional): _description_: This is the boolean that will determine if the scheduler should be paused or not. Defaults to True.

        Returns:
            Union[int, None]: _description_: Will return self.success if it worked, otherwise None because it will have raised an error.
        """
        try:
            if pause is True:
                self.scheduler.pause()
                self.disp.log_info("Scheduler paused.", "pause")
            else:
                self.scheduler.resume()
                self.disp.log_info("Scheduler resumed.", "pause")
            return self.success
        except Exception as e:
            self.disp.log_error(
                f"An error occurred while pausing the scheduler: {e}",
                "pause"
            )
            msg = f"Error({self.__class__.__name__}): "
            msg += "Failed to call the chron pause wrapper function."
            raise RuntimeError(msg) from e

    def resume(self) -> Union[int]:
        """_summary_
            This function is in charge of resuming the scheduler loop if it was paused.

        Returns:
            Union[int]: _description_: Will return self.success if it worked, otherwise None because it will have raised an error.
        """
        return self.pause(pause=False)

    def stop(self, wait: bool = True) -> Union[int, None]:
        """_summary_
            This function is responsible for shutting down the scheduler, terminating any running jobs, and optionally waiting for those jobs to complete before exiting.

        Args:
            wait (bool, optional): _description_. Defaults to True. Wait for the running tasks to finish.

        Raises:
            RuntimeError: _description_: The function failed to call the underlying processes that were required for it to run.

        Returns:
            Union[int, None]: _description_: will return self.success if it succeeds, or none if it raised an error.
        """
        try:
            self.scheduler.shutdown(wait=wait)
            self.disp.log_info("Scheduler stopped.", "stop")
            return self.success
        except SchedulerNotRunningError:
            self.disp.log_info("Scheduler is already stopped.", "stop")
            return self.success
        except Exception as e:
            self.disp.log_error(
                f"An error occurred while stopping the scheduler: {e}", "stop"
            )
            msg = f"Error({self.__class__.__name__}): "
            msg += "Failed to call the chron stop wrapper function."
            raise RuntimeError(msg) from e


if __name__ == "__main__":
    import sys
    from time import sleep
    from datetime import datetime

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

    print("Testing declared functions.")
    test_current_date()
    hello_world()
    pending_world()
    goodbye_world()
    print("Declared functions tested.")

    SUCCES = 0
    ERROR = 84
    DEBUG = True
    KIND_KILL = True
    NB_REPEATS = 2
    TRIGGER = "interval"
    SECONDS = 2
    NB_FUNCTIONS = 5
    MAIN_THREAD_DELAY = int((SECONDS*NB_FUNCTIONS)*NB_REPEATS)

    print(
        f"Statuses:\nSUCCESS = {SUCCES}, ERROR = {ERROR}\n"
        f"DEBUG = {DEBUG}, KIND_KILL = {KIND_KILL}, "
        f"NB_REPEATS = {NB_REPEATS}, "
        f"TRIGGER = {TRIGGER}, SECONDS = {SECONDS}, "
        f"NB_FUNCTIONS = {NB_FUNCTIONS}, "
        f"MAIN_THREAD_DELAY = {MAIN_THREAD_DELAY}"
    )

    print("Initialising class BackgroundTasks.")
    BTI = BackgroundTasks(
        success=SUCCES,
        error=ERROR,
        debug=DEBUG
    )
    print("Class BackgroundTasks initialised.")

    print("Adding tasks to the scheduler.")
    status = BTI.safe_add_task(
        func=test_current_date,
        args=(datetime.now,),
        kwargs=None,
        trigger=TRIGGER,
        seconds=SECONDS
    )
    print(f"status {status}")
    status = BTI.add_task(
        hello_world,
        args=None,
        kwargs=None,
        trigger=TRIGGER,
        seconds=SECONDS
    )
    print(f"status {status}")
    status = BTI.safe_add_task(
        pending_world,
        args=None,
        kwargs=None,
        trigger=TRIGGER,
        seconds=SECONDS
    )
    print(f"status {status}")
    status = BTI.add_task(
        goodbye_world,
        args=None,
        kwargs=None,
        trigger=TRIGGER,
        seconds=SECONDS
    )
    print(f"status {status}")
    status = BTI.add_task(
        func=test_current_date,
        args=datetime.now,
        kwargs=None,
        trigger=TRIGGER,
        seconds=SECONDS
    )
    print(f"status {status}")
    print("Added tasks to the scheduler.")

    print("Startins scheduler.")
    print(f"Status: {BTI.safe_start()}")
    print("Scheduler started.")
    print(f"Waiting {MAIN_THREAD_DELAY} on the main thread.")
    sleep(MAIN_THREAD_DELAY)
    print(f"Waited {MAIN_THREAD_DELAY} on the main thread.")
    print("Stopping scheduler.")
    status = BTI.safe_stop(KIND_KILL)
    print(f"Status: {status}")
    sys.exit(status)

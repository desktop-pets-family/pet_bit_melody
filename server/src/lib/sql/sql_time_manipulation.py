"""
    File in charge of containing the functions that allow for time conversion between datetime and strings.
"""

from datetime import datetime

from display_tty import Disp, TOML_CONF, SAVE_TO_FILE, FILE_NAME

from . import sql_constants as SCONST


class SQLTimeManipulation:
    """_summary_
    """

    def __init__(self, debug: bool = False) -> None:
        """_summary_
            This is the class that contains functions in charge of manipulating time.
            It can convert time from as string to a datetime and vice-versa

        Args:
            debug (bool, optional): _description_. Defaults to False.
        """
        self.debug: bool = debug
        # ----------------------- Inherited from SCONST  -----------------------
        self.date_only: str = SCONST.DATE_ONLY
        self.date_and_time: str = SCONST.DATE_AND_TIME
        # --------------------------- logger section ---------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def datetime_to_string(self, datetime_instance: datetime, date_only: bool = False, sql_mode: bool = False) -> str:
        """_summary_
            Convert a datetime instance to a string.

        Args:
            datetime_instance (datetime): _description_: The datetime item
            date_only (bool, optional): _description_. Defaults to False.: if True will only return the date section, otherwise will return the date and time section.
            sql_mode (bool, optional): _description_. Defaults to False.: if True, will add the microseconds to the response so that it can be directly inserted into an sql command.

        Raises:
            ValueError: _description_: If the datetime instance is not a datetime, a valueerror is raised.

        Returns:
            str: _description_: A string instance of the datetime.
        """

        if isinstance(datetime_instance, datetime) is False:
            self.disp.log_error(
                "The input is not a datetime instance.",
                "datetime_to_string"
            )
            raise ValueError("Error: Expected a datetime instance.")
        if date_only is True:
            return datetime_instance.strftime(self.date_only)
        converted_time = datetime_instance.strftime(self.date_and_time)
        if sql_mode is True:
            microsecond = datetime_instance.strftime("%f")[:3]
            res = f"{converted_time}.{microsecond}"
        else:
            res = f"{converted_time}"
        return res

    def string_to_datetime(self, datetime_string_instance: str, date_only: bool = False) -> str:
        """_summary_
            Convert a datetime instance to a string.

        Args:
            datetime_string_instance (str): _description_: The string datetime item
            date_only (bool, optional): _description_. Defaults to False.: if True will only return the date section, otherwise will return the date and time section.

        Raises:
            ValueError: _description_: If the datetime instance is not a datetime, a valueerror is raised.

        Returns:
            str: _description_: A string instance of the datetime.
        """

        if isinstance(datetime_string_instance, str) is False:
            self.disp.log_error(
                "The input is not a string instance.",
                "string_to_datetime"
            )
            raise ValueError("Error: Expected a string instance.")
        if date_only is True:
            return datetime.strptime(datetime_string_instance, self.date_only)
        return datetime.strptime(datetime_string_instance, self.date_and_time)

    def get_correct_now_value(self) -> str:
        """_summary_
            Get the current date and time in the correct format for the database.

        Returns:
            str: _description_
        """
        current_time = datetime.now()
        return current_time.strftime(self.date_and_time)

    def get_correct_current_date_value(self) -> str:
        """_summary_
            Get the current date and time in the correct format for the database.

        Returns:
            str: _description_
        """
        current_time = datetime.now()
        return current_time.strftime(self.date_only)

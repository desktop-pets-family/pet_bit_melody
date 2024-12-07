"""
    File in charge of containing the interfacing between an sql library and the program.
    This contains functions that simplify the process of interracting with databases as well as check for injection attempts.
"""

from display_tty import Disp, TOML_CONF, SAVE_TO_FILE, FILE_NAME

from .sql_time_manipulation import SQLTimeManipulation
from .sql_connections import SQLManageConnections
from .sql_query_boilerplates import SQLQueryBoilerplates


class SQL:
    """
    The class in charge of managing a SQL database
    """

    def __init__(self, url: str, port: int, username: str, password: str, db_name: str, success: int = 0, error: int = 84, debug: bool = False):
        """
        The constructor of the SQL class
        Args:
            url (str): _description_
            port (int): _description_
            username (str): _description_
            password (str): _description_
            db_name (str): _description_
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
            debug (bool, optional): _description_. Defaults to False.
        """
        self.debug: bool = debug
        self.success: int = success
        self.error: int = error
        self.url: str = url
        self.port: int = port
        self.username: str = username
        self.password: str = password
        self.db_name: str = db_name
        # ----------------- Pre class variable initialisation  -----------------
        self.disp: Disp = None
        self.sql_manage_connections: SQLManageConnections = None
        self.sql_time_manipulation: SQLTimeManipulation = None
        self.sql_query_boilerplates: SQLQueryBoilerplates = None
        # --------------------------- logger section ---------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )
        # ------------- The class in charge of the sql connection  -------------
        self.sql_manage_connections: SQLManageConnections = SQLManageConnections(
            url=self.url,
            port=self.port,
            username=self.username,
            password=self.password,
            db_name=self.db_name,
            success=self.success,
            error=self.error,
            debug=self.debug
        )

        # ---------------------------- Time logger  ----------------------------
        self.sql_time_manipulation: SQLTimeManipulation = SQLTimeManipulation(
            self.debug
        )
        self.datetime_to_string: SQLTimeManipulation.datetime_to_string = self.sql_time_manipulation.datetime_to_string
        self.string_to_datetime: SQLTimeManipulation.string_to_datetime = self.sql_time_manipulation.string_to_datetime
        self._get_correct_now_value: SQLTimeManipulation.get_correct_now_value = self.sql_time_manipulation.get_correct_now_value
        self._get_correct_current_date_value: SQLTimeManipulation.get_correct_current_date_value = self.sql_time_manipulation.get_correct_current_date_value
        # --------------------------- debug section  ---------------------------
        self.sql_manage_connections.show_connection_info("__init__")
        # --------------------------- initialise pool --------------------------
        if self.sql_manage_connections.initialise_pool() != self.success:
            msg = "Failed to initialise the connection pool."
            self.disp.log_critical(msg, "__init__")
            raise RuntimeError(f"Error: {msg}")
        # ----------------------- sql query boilerplates -----------------------
        self.sql_query_boilerplates: SQLQueryBoilerplates = SQLQueryBoilerplates(
            sql_pool=self.sql_manage_connections, success=self.success,
            error=self.error, debug=self.debug
        )
        self.get_table_column_names: SQLQueryBoilerplates.get_table_column_names = self.sql_query_boilerplates.get_table_column_names
        self.get_table_names: SQLQueryBoilerplates.get_table_names = self.sql_query_boilerplates.get_table_names
        self.describe_table: SQLQueryBoilerplates.describe_table = self.sql_query_boilerplates.describe_table
        self.insert_data_into_table: SQLQueryBoilerplates.insert_data_into_table = self.sql_query_boilerplates.insert_data_into_table
        self.get_data_from_table: SQLQueryBoilerplates.get_data_from_table = self.sql_query_boilerplates.get_data_from_table
        self.get_table_size: SQLQueryBoilerplates.get_table_size = self.sql_query_boilerplates.get_table_size
        self.update_data_in_table: SQLQueryBoilerplates.update_data_in_table = self.sql_query_boilerplates.update_data_in_table
        self.insert_or_update_data_into_table: SQLQueryBoilerplates.insert_or_update_data_into_table = self.sql_query_boilerplates.insert_or_update_data_into_table
        self.remove_data_from_table: SQLQueryBoilerplates.remove_data_from_table = self.sql_query_boilerplates.remove_data_from_table
        self.drop_data_from_table: SQLQueryBoilerplates.remove_data_from_table = self.sql_query_boilerplates.remove_data_from_table

    def __del__(self) -> None:
        """
            Disconnect the database when the class is destroyed
        """
        if self.sql_manage_connections is not None:
            del self.sql_manage_connections
            self.sql_manage_connections = None
        if self.sql_time_manipulation is not None:
            del self.sql_time_manipulation
            self.sql_time_manipulation = None
        if self.sql_query_boilerplates is not None:
            del self.sql_query_boilerplates
            self.sql_query_boilerplates = None

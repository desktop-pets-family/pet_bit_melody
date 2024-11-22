##
# EPITECH PROJECT, 2023
# Desktop_pet
# File description:
# pet_server.py
##

import os
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .sql import SQL
from .bucket import Bucket
from .components import Endpoints, ServerPaths, RuntimeData, ServerManagement, CONST, BackgroundTasks, Crons, OAuthAuthentication, MailManagement, FFFamily
from .boilerplates import BoilerplateIncoming, BoilerplateNonHTTP, BoilerplateResponses


class Server:
    """_summary_
    """

    def __init__(self, host: str = "0.0.0.0", port: int = 5000, success: int = 0, error: int = 84, app_name: str = "Area", debug: bool = False) -> None:
        """_summary_
            This is the class Server, a class that contains the structures used to allow the uvicorn and fastapi combo to run successfully.
        Args:
            host (str, optional): _description_. Defaults to "0.0.0.0".
            port (int, optional): _description_. Defaults to 5000.
            character_folder (str, optional): _description_. Defaults to "".
            usr_db_path (str, optional): _description_. Defaults to "".
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
            app_name (str, optional): _description_. Defaults to "Desktop Pets".
            debug (bool, optional): _description_. Defaults to False.
        """
        # ---------------------   The inherited arguments  ---------------------
        self.host: str = host
        self.port: int = port
        self.success: int = success
        self.error: int = error
        self.debug: bool = debug
        # ------------------------ The logging function ------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            FILE_DESCRIPTOR,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )
        # ------------------------ Shared Runtime data  ------------------------
        self.runtime_data_initialised: RuntimeData = RuntimeData(
            host=self.host,
            port=self.port,
            app_name=app_name,
            error=self.error,
            success=self.success
        )
        # ----- The classes that need to be tracked for the server to run  -----
        self.runtime_data_initialised.ff_family_initialised = FFFamily(
            cwd=CONST.FF_FAMILY_CWD,
            query_timeout=CONST.FF_FAMILY_QUERY_TIMEOUT,
            success=self.success,
            error=self.error,
            debug=self.debug,
            bundle_download=CONST.FF_FAMILY_BUNDLE_DOWNLOAD
        )
        self.runtime_data_initialised.background_tasks_initialised = BackgroundTasks(
            success=self.success,
            error=self.error,
            debug=self.debug
        )
        self.runtime_data_initialised.crons_initialised = Crons(
            self.runtime_data_initialised,
            success=self.success,
            error=self.error,
            debug=self.debug
        )
        self.disp.log_debug("Initialising database link.", "__init__")
        self.runtime_data_initialised.database_link = SQL(
            url=CONST.DB_HOST,
            port=CONST.DB_PORT,
            username=CONST.DB_USER,
            password=CONST.DB_PASSWORD,
            db_name=CONST.DB_DATABASE,
            success=self.success,
            error=self.error,
            debug=self.debug
        )
        self.runtime_data_initialised.server_management_initialised = ServerManagement(
            self.runtime_data_initialised,
            error=self.error,
            success=self.success,
            debug=self.debug
        )
        self.runtime_data_initialised.boilerplate_responses_initialised = BoilerplateResponses(
            self.runtime_data_initialised,
            debug=self.debug
        )
        self.runtime_data_initialised.boilerplate_incoming_initialised = BoilerplateIncoming(
            self.runtime_data_initialised,
            error=self.error,
            success=self.success,
            debug=self.debug
        )
        self.runtime_data_initialised.boilerplate_non_http_initialised = BoilerplateNonHTTP(
            self.runtime_data_initialised,
            error=self.error,
            success=self.success,
            debug=self.debug
        )
        self.runtime_data_initialised.paths_initialised = ServerPaths(
            self.runtime_data_initialised,
            error=self.error,
            success=self.success,
            debug=self.debug
        )
        self.runtime_data_initialised.bucket_link = Bucket(
            error=self.error,
            success=self.success,
            debug=self.debug
        )
        self.runtime_data_initialised.endpoints_initialised = Endpoints(
            self.runtime_data_initialised,
            error=self.error,
            success=self.success,
            debug=self.debug
        )
        self.runtime_data_initialised.oauth_authentication_initialised = OAuthAuthentication(
            self.runtime_data_initialised,
            success=success,
            error=error,
            debug=debug
        )
        self.runtime_data_initialised.mail_management_initialised = MailManagement(
            error=self.error,
            success=self.success,
            debug=self.debug
        )

    def __del__(self) -> None:
        """_summary_
            The destructor of the class.
        """
        self.disp.log_info("The server is shutting down.", "__del__")
        self.stop_server()

    def get_ff_family(self) -> int:
        """_summary_
            The function in charge of downloading the ffmpeg library.

        Returns:
            int: _description_: Returns 0 if the download was successful.
        """
        title = "get_ffmpeg"
        self.disp.log_info("Downloading ffmpeg", title)
        try:
            self.runtime_data_initialised.ff_family_initialised.ff_family_downloader_initialised()
        except (
            self.runtime_data_initialised.ff_family_initialised.package_not_installed,
            self.runtime_data_initialised.ff_family_initialised.package_not_supported,
            self.runtime_data_initialised.ff_family_initialised.architecture_not_supported,
            NotImplementedError,
            RuntimeError,
            ValueError
        ) as e:
            self.disp.log_critical(f"Error: {e}", title)
            return self.error
        self.disp.log_info("Downloaded ffmpeg", title)
        return self.success

    def main(self) -> int:
        """_summary_
            The main function of the server.
            This is the one in charge of starting the server.

        Returns:
            int: _description_
        """
        title = "main"
        status = self.get_ff_family()
        if status != self.success:
            self.disp.log_critical(
                "Error: failed to download ff binaries, Aborting server startup.",
                title
            )
            return status
        self.runtime_data_initialised.server_management_initialised.initialise_classes()
        self.runtime_data_initialised.paths_initialised.load_default_paths_initialised()
        self.runtime_data_initialised.paths_initialised.inject_routes()
        self.runtime_data_initialised.crons_initialised.inject_crons()
        status = self.runtime_data_initialised.background_tasks_initialised.safe_start()
        if status != self.success:
            self.disp.log_error(
                "Error: background tasks failed to start.",
                title
            )
            return status
        try:
            self.runtime_data_initialised.server.run()
        except Exception as e:
            self.disp.log_error(f"Error: {e}", title)
            return self.error
        return self.success

    def is_running(self) -> bool:
        """_summary_
            The function in charge of checking if the server is running.

        Returns:
            bool: _description_: Returns True if the server is running.
        """
        return self.runtime_data_initialised.server_management_initialised.is_server_running()

    def stop_server(self) -> None:
        """_summary_
            The function in charge of stopping the server.
        """
        title = "stop_server"
        self.disp.log_info("Stopping server", title)
        if self.runtime_data_initialised.server_management_initialised is not None:
            del self.runtime_data_initialised.server_management_initialised
            self.runtime_data_initialised.server_management_initialised = None
        if self.runtime_data_initialised.crons_initialised is not None:
            del self.runtime_data_initialised.crons_initialised
            self.runtime_data_initialised.crons_initialised = None
        self.disp.log_info("Server stopped", title)

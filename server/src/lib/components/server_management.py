"""_summary_
    This is the file in charge of containing the functions that will manage the server run status.
"""

import signal
import uvicorn
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from . import CONST
from .http_codes import HCI
from .runtime_data import RuntimeData


class ServerManagement:
    """_summary_
    """

    def __init__(self, runtime_data: RuntimeData, error: int = 84, success: int = 0, debug: bool = False) -> None:
        """_summary_
        """
        # -------------------------- Inherited values --------------------------
        self.runtime_data_initialised: RuntimeData = runtime_data
        self.error: int = error
        self.success: int = success
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

    def __del__(self) -> None:
        """_summary_
            The destructor of the class
        """
        self.disp.log_info(
            "Server sub processes are shutting down.",
            "__del__"
        )
        if self.is_server_alive() is True:
            del self.runtime_data_initialised.database_link
            self.runtime_data_initialised.database_link = None
            del self.runtime_data_initialised.bucket_link
            self.runtime_data_initialised.continue_running = False
            if self.runtime_data_initialised.server is not None:
                self.runtime_data_initialised.server.handle_exit(
                    signal.SIGTERM, None
                )
                self.runtime_data_initialised.server = None
        if self.runtime_data_initialised.background_tasks_initialised is not None:
            del self.runtime_data_initialised.background_tasks_initialised
            self.runtime_data_initialised.background_tasks_initialised = None

    def is_server_alive(self) -> bool:
        """
            Check if the server is still running.
        Returns:
            bool: Returns True if it is running.
        """
        return self.runtime_data_initialised.continue_running

    def is_server_running(self) -> bool:
        """
            Check if the server is still running.
        Returns:
            bool: Returns True if it is running.
        """
        return self.is_server_alive()

    async def shutdown(self) -> Response:
        """
            The function to shutdown the server
        Returns:
            Response: Return the shutdown server message
        """
        if self.runtime_data_initialised.database_link.is_connected() is True:
            self.runtime_data_initialised.database_link.disconnect_db()
        if self.runtime_data_initialised.bucket_link.is_connected() is True:
            self.runtime_data_initialised.bucket_link.disconnect()
        self.runtime_data_initialised.continue_running = False
        self.runtime_data_initialised.server.handle_exit(signal.SIGTERM, None)
        body = self.runtime_data_initialised.boilerplate_responses_initialised.build_response_body(
            title="Shutdown",
            message="The server is shutting down.",
            resp="Shutdown",
            token="",
            error=False
        )
        return HCI.success(body, content_type=CONST.CONTENT_TYPE, headers=self.runtime_data_initialised.json_header)

    # -------------------Initialisation-----------------------

    def initialise_classes(self) -> None:
        """
            The function to initialise the server classes
        """

        self.runtime_data_initialised.app = FastAPI()
        self.runtime_data_initialised.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        msg = "uvicorn.Config(\n"
        msg += f"app='{self.runtime_data_initialised.app}',\n"
        msg += f"host='{self.runtime_data_initialised.host}',\n"
        msg += f"port='{self.runtime_data_initialised.port}',\n"
        msg += f"lifespan='{CONST.SERVER_LIFESPAN}',\n"
        msg += f"timeout_keep_alive='{CONST.SERVER_TIMEOUT_KEEP_ALIVE}',\n"
        msg += f"workers='{CONST.SERVER_WORKERS}',\n"
        msg += f"reload='{CONST.SERVER_DEV_RELOAD}',\n"
        msg += f"reload_dirs='{CONST.SERVER_DEV_RELOAD_DIRS}',\n"
        msg += f"log_level='{CONST.SERVER_DEV_LOG_LEVEL}',\n"
        msg += f"use_colors='{CONST.SERVER_DEV_USE_COLOURS}',\n"
        msg += f"proxy_headers='{CONST.SERVER_PROD_PROXY_HEADERS}',\n"
        msg += f"forwarded_allow_ips='{CONST.SERVER_PROD_FORWARDED_ALLOW_IPS}'"
        msg += "\n\n)"
        self.disp.log_debug(msg, "initialise_classes")
        self.runtime_data_initialised.config = uvicorn.Config(
            app=self.runtime_data_initialised.app,
            host=self.runtime_data_initialised.host,
            port=self.runtime_data_initialised.port,
            lifespan=CONST.SERVER_LIFESPAN,
            timeout_keep_alive=CONST.SERVER_TIMEOUT_KEEP_ALIVE,
            workers=CONST.SERVER_WORKERS,
            reload=CONST.SERVER_DEV_RELOAD,
            reload_dirs=CONST.SERVER_DEV_RELOAD_DIRS,
            log_level=CONST.SERVER_DEV_LOG_LEVEL,
            use_colors=CONST.SERVER_DEV_USE_COLOURS,
            proxy_headers=CONST.SERVER_PROD_PROXY_HEADERS,
            forwarded_allow_ips=CONST.SERVER_PROD_FORWARDED_ALLOW_IPS
        )
        self.runtime_data_initialised.server = uvicorn.Server(
            self.runtime_data_initialised.config)
        self.runtime_data_initialised.continue_running = True

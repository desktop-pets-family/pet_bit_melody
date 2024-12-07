"""_summary_
    File in charge of referencing all the paths_initialised supported by the server.
"""
from typing import Union, List, Dict, Any
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME
from .runtime_data import RuntimeData
from .constants import PATH_KEY, ENDPOINT_KEY,  METHOD_KEY, ALLOWED_METHODS


class ServerPaths:
    """_summary_
    """

    def __init__(self, runtime_data: RuntimeData, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_

        Args:
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
        """
        self.runtime_data_initialised: RuntimeData = runtime_data
        self.success = success
        self.error = error
        self.routes: List[Dict[str, Any]] = []
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

    def add_path(self, path: str, endpoint: object, method: Union[str, List[str]]) -> int:
        """_summary_
            This function is in charge of adding a path to the list of paths_initialised.

        Args:
            path (str): _description_: The path to call for the endpoint to be triggered
            endpoint (str): _description_: The function that represents the endpoint
            method (str, list): _description_: The method used for the provided path (GET, PUT, POST, etc)

        Returns:
            int: _description_: success if it succeeded, error if there was an error in the data.
        """
        self.disp.log_debug(f"Adding path <{path}>", "add_path")

        if isinstance(path, (str)) is False or isinstance(method, (str, list)) is False or callable(endpoint) is False:
            self.disp.log_error(
                f"Failed to insert {path} with method {method}", "add_path"
            )
            return self.error
        if isinstance(method, str) is True and method.upper() not in ALLOWED_METHODS:
            msg = f"Failed to insert {path}, method {method} not allowed"
            self.disp.log_error(msg, "add_path")
            return self.error
        if isinstance(method, list) is True:
            for i in method:
                if isinstance(i, str) is False or i.upper() not in ALLOWED_METHODS:
                    msg = f"Failed to insert {path}, method {i} not allowed"
                    self.disp.log_error(msg, "add_path")
                    return self.error
        if isinstance(method, str) is True:
            method = [method]
        self.routes.append(
            {PATH_KEY: path, ENDPOINT_KEY: endpoint, METHOD_KEY: method}
        )
        return self.success

    def load_default_paths_initialised(self) -> None:
        """_summary_
            This function is in charge of adding the default paths_initialised to the list of paths_initialised.
        """
        self.disp.log_debug(
            "Loading default paths_initialised",
            "load_default_paths_initialised"
        )
        self.runtime_data_initialised.endpoints_initialised.inject_routes()

    def inject_routes(self) -> None:
        """_summary_
            Function in charge of loading the routes into the api.
        Args:
            app (FastAPI): _description_
        """
        self.disp.log_info("injecting routes", "inject_routes")
        for route in self.routes:
            self.disp.log_debug(f"route = {route}", "inject_routes")
            self.runtime_data_initialised.app.add_api_route(
                route[PATH_KEY],
                route[ENDPOINT_KEY],
                methods=route[METHOD_KEY]
            )

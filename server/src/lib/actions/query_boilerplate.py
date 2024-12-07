"""_summary_
    File in charge of containing the boilerplate endpoint functions to make queries to the web.
"""

from typing import Union, Mapping, Dict, Any

import requests

from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME

from . import constants as ACONST


class UnknownContentTypeError(Exception):
    """Exception raised when the content type of the response is unknown."""

    def __init__(self, message: str = "No Content-Type found in the header") -> None:
        self.message = message
        super().__init__(self.message)


class QueryEndpoint:
    """_summary_
        This is the class in charge of containing the boilerplate endpoint functions.
    """

    def __init__(self, host: str = "http://127.0.0.1", port: Union[int, None] = 6000, delay: int = 2, debug: bool = False) -> None:
        """_summary_
            Class in charge of containing the boilerplate endpoint functions to make queries to the web.

        Args:
            host (_type_, optional): _description_. Defaults to "http://127.0.0.1".
            port (Union[int, None], optional): _description_. Defaults to 6000.
            delay (int, optional): _description_. Defaults to 2.
            debug (bool, optional): _description_. Defaults to False.
        """
        self.debug: bool = debug
        if host.startswith("http") is False:
            self._host = f"http://{host}"
        else:
            self._host = host
        if self._host.endswith("/") is True:
            self._host = self._host[:-1]
        if port is not None:
            self._host += f":{port}"
        self._delay = delay
        # ---------------------- The visual logger class  ----------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def get_endpoint(self, path: str, content: Union[Dict[str, Any], None] = None, header: Union[Mapping[str, str], None] = None) -> requests.Response:
        """_summary_
            This function is in charge of sending a GET request to the server.
        Args:
            path (str): _description_: The path of the endpoint.
            content (Union[Dict[str, Any], None], optional): _description_: The content to be sent to the server.
            header (Union[Mapping[str, str], None], optional): _description_: The header to be sent to the server. Defaults to None.
        Returns:
            requests.Response: _description_: The response from the server.
        """
        title = "get_endpoint"
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        final_path = f"{self._host}/{path}"
        self.disp.log_debug(f"final_path = {final_path}", title)
        self.disp.log_debug(f"content = {content}", title)
        self.disp.log_debug(f"header = {header}", title)
        if content is not None and header is None:
            return requests.get(final_path, json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.get(final_path, headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.get(final_path, json=content, headers=header, timeout=self._delay)
        return requests.get(final_path, timeout=self._delay)

    def post_endpoint(self, path: str, content: Union[Dict[str, Any], None] = None, header: Union[Mapping[str, str], None] = None) -> requests.Response:
        """_summary_
            This function is in charge of sending a POST request to the server.
        Args:
            path (str): _description_: The path of the endpoint.
            content (Union[Dict[str, Any], None], optional): _description_: The content to be sent to the server.
            header (Union[Mapping[str, str], None], optional): _description_: The header to be sent to the server. Defaults to None.
        Returns:
            requests.Response: _description_: The response from the server.
        """
        title = "post_endpoint"
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        final_path = f"{self._host}/{path}"
        self.disp.log_debug(f"final_path = {final_path}", title)
        self.disp.log_debug(f"content = {content}", title)
        self.disp.log_debug(f"header = {header}", title)
        if content is not None and header is None:
            return requests.post(final_path, json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.post(final_path, headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.post(final_path, json=content, headers=header, timeout=self._delay)
        return requests.post(final_path, timeout=self._delay)

    def put_endpoint(self, path: str, content: Union[Dict[str, Any], None] = None, header: Union[Mapping[str, str], None] = None) -> requests.Response:
        """_summary_
            This function is in charge of sending a PUT request to the server.
        Args:
            path (str): _description_: The path of the endpoint.
            content (Union[Dict[str, Any], None], optional): _description_: The content to be sent to the server.
            header (Union[Mapping[str, str], None], optional): _description_: The header to be sent to the server. Defaults to None.
        Returns:
            requests.Response: _description_: The response from the server.
        """
        title = "put_endpoint"
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        final_path = f"{self._host}/{path}"
        self.disp.log_debug(f"final_path = {final_path}", title)
        self.disp.log_debug(f"content = {content}", title)
        self.disp.log_debug(f"header = {header}", title)
        if content is not None and header is None:
            return requests.put(final_path, json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.put(final_path, headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.put(final_path, json=content, headers=header, timeout=self._delay)
        return requests.put(final_path, timeout=self._delay)

    def patch_endpoint(self, path: str, content: Union[Dict[str, Any], None] = None, header: Union[Mapping[str, str], None] = None) -> requests.Response:
        """_summary_
            This function is in charge of sending a PATCH request to the server.
        Args:
            path (str): _description_: The path of the endpoint.
            content (Union[Dict[str, Any], None], optional): _description_: The content to be sent to the server.
            header (Union[Mapping[str, str], None], optional): _description_: The header to be sent to the server. Defaults to None.
        Returns:
            requests.Response: _description_: The response from the server.
        """
        title = "patch_endpoint"
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        final_path = f"{self._host}/{path}"
        self.disp.log_debug(f"final_path = {final_path}", title)
        self.disp.log_debug(f"content = {content}", title)
        self.disp.log_debug(f"header = {header}", title)
        if content is not None and header is None:
            return requests.patch(final_path, json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.patch(final_path, headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.patch(final_path, json=content, headers=header, timeout=self._delay)
        return requests.patch(final_path, timeout=self._delay)

    def delete_endpoint(self, path: str, content: Union[Dict[str, Any], None] = None, header: Union[Mapping[str, str], None] = None) -> requests.Response:
        """_summary_
            This function is in charge of sending a DELETE request to the server.
        Args:
            path (str): _description_: The path of the endpoint.
            content (Union[Dict[str, Any], None], optional): _description_: The content to be sent to the server.
            header (Union[Mapping[str, str], None], optional): _description_: The header to be sent to the server. Defaults to None.
        Returns:
            requests.Response: _description_: The response from the server.
        """
        title = "delete_endpoint"
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        final_path = f"{self._host}/{path}"
        self.disp.log_debug(f"final_path = {final_path}", title)
        self.disp.log_debug(f"content = {content}", title)
        self.disp.log_debug(f"header = {header}", title)
        if content is not None and header is None:
            return requests.delete(final_path, json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.delete(final_path, headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.delete(final_path, json=content, headers=header, timeout=self._delay)
        return requests.delete(final_path, timeout=self._delay)

    def head_endpoint(self, path: str, content: Union[Dict[str, Any], None] = None, header: Union[Mapping[str, str], None] = None) -> requests.Response:
        """_summary_
            This function is in charge of sending a HEAD request to the server.
        Args:
            path (str): _description_: The path of the endpoint.
            content (Union[Dict[str, Any], None], optional): _description_: The content to be sent to the server.
            header (Union[Mapping[str, str], None], optional): _description_: The header to be sent to the server. Defaults to None.
        Returns:
            requests.Response: _description_: The response from the server.
        """
        title = "head_endpoint"
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        final_path = f"{self._host}/{path}"
        self.disp.log_debug(f"final_path = {final_path}", title)
        self.disp.log_debug(f"content = {content}", title)
        self.disp.log_debug(f"header = {header}", title)
        if content is not None and header is None:
            return requests.head(final_path, json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.head(final_path, headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.head(final_path, json=content, headers=header, timeout=self._delay)
        return requests.head(final_path, timeout=self._delay)

    def options_endpoint(self, path: str, content: Union[Dict[str, Any], None] = None, header: Union[Mapping[str, str], None] = None) -> requests.Response:
        """_summary_
            This function is in charge of sending a OPTIONS request to the server.
        Args:
            path (str): _description_: The path of the endpoint.
            content (Union[Dict[str, Any], None], optional): _description_: The content to be sent to the server.
            header (Union[Mapping[str, str], None], optional): _description_: The header to be sent to the server. Defaults to None.
        Returns:
            requests.Response: _description_: The response from the server.
        """
        title = "options_endpoint"
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        final_path = f"{self._host}/{path}"
        self.disp.log_debug(f"final_path = {final_path}", title)
        self.disp.log_debug(f"content = {content}", title)
        self.disp.log_debug(f"header = {header}", title)
        if content is not None and header is None:
            return requests.options(final_path, json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.options(final_path, headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.options(final_path, json=content, headers=header, timeout=self._delay)
        return requests.options(final_path, timeout=self._delay)

    def get_status(self, response: requests.Response) -> int:
        """_summary_
            This function is in charge of getting the status code from the response.
        Args:
            response (requests.Response): _description_: The response from the server.
        Returns:
            int: _description_: The status code from the response.
        """
        return response.status_code

    def get_content_type(self, response: requests.Response) -> str:
        """_summary_
            This function is in charge of getting the content type from the response.

        Args:
            response (requests.Response): _description_: The response from the server.

        Raises:
            UnknownContentTypeError: _description_: If no content type is found in the header.

        Returns:
            str: _description_: The content type from the response.
        """
        response = response.headers.get("Content-Type")
        if response is not None:
            return response
        raise UnknownContentTypeError("No Content-Type found in the header")

    def get_content(self, response: requests.Response) -> Dict[str, Union[str, bytes, Dict[str, Any], None]]:
        """
        Retrieve and parse content from an HTTP response based on its Content-Type.

        Args:
            response (requests.Response): The HTTP response from the server.

        Raises:
            ValueError: If the response content is not valid JSON.

        Returns:
            Dict[str, Union[str, bytes, Dict[str, Any], None]]: A dictionary with parsed response content.
            Contains two keys:
                - ACONST.CONTENT_TYPE_KEY: str - The content type of the response.
                - ACONST.CONTENT_KEY: Union[Dict[str, Any], str, bytes, None] - Parsed content.
                    - JSON (application/json, application/ld+json) -> Dict
                    - Text (text/html, text/plain, text/csv, text/xml) -> str
                    - XML (application/xml) -> str
                    - Binary data (e.g., application/octet-stream, application/pdf) -> bytes
                    - None for unhandled types.
        """
        title = "get_content"
        node = None
        try:
            content_type = self.get_content_type(response)
            node = content_type.split(";")[0]
        except UnknownContentTypeError as e:
            self.disp.log_error(
                f"Response content type is unknown, {e}", title
            )
            return {ACONST.CONTENT_TYPE_KEY: None, ACONST.CONTENT_KEY: None}

        if node in ACONST.CONTENT_TYPES_JSON:
            try:
                return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: response.json()}
            except ValueError as e:
                raise ValueError("Response content is not valid JSON") from e
        elif node in ACONST.CONTENT_TYPES_TEXT:
            return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: response.text}
        elif node in ACONST.CONTENT_TYPES_XML:
            return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: response.text}
        elif node in ACONST.CONTENT_TYPES_BINARY:
            return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: response.content}
        elif node in ACONST.CONTENT_TYPES_AUDIO:
            return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: response.content}
        elif node in ACONST.CONTENT_TYPES_IMAGES:
            return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: response.content}
        elif node in ACONST.CONTENT_TYPES_VIDEO:
            return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: response.content}
        else:
            self.disp.log_error(f"Unhandled content type: {content_type}")
            return {ACONST.CONTENT_TYPE_KEY: content_type, ACONST.CONTENT_KEY: None}

    def compile_response_data(self, response: requests.Response) -> Dict[str, Union[int, Dict[str, Union[str, bytes, Dict[str, Any], None]]]]:
        """
        Compile the response from an HTTP request into a dictionary.

        Args:
            response (requests.Response): The HTTP response from the server.

        Returns:
            Dict[str, Union[int, Dict[str, Union[str, bytes, Dict[str, Any], None]]]: A dictionary with the response status code and content.
        """
        title = "compile_response_data"
        self.disp.log_debug("Compiling response data", title)
        self.disp.log_debug(f"response = {response}", title)
        compiled = {}
        data = self.get_content(response)
        self.disp.log_debug(f"data = {data}", title)
        compiled[ACONST.RESPONSE_NODE_BODY_KEY] = data[ACONST.CONTENT_KEY]
        compiled[ACONST.RESPONSE_NODE_BODY_TYPE_KEY] = data[ACONST.CONTENT_TYPE_KEY]
        compiled[ACONST.RESPONSE_NODE_STATUS_CODE_KEY] = response.status_code
        compiled[ACONST.RESPONSE_NODE_HEADERS_KEY] = response.headers
        compiled[ACONST.RESPONSE_NODE_HEADERS_TYPE_KEY] = type(
            response.headers)
        compiled[ACONST.RESPONSE_NODE_ENCODING_KEY] = response.encoding
        compiled[ACONST.RESPONSE_NODE_HISTORY_KEY] = response.history
        compiled[ACONST.RESPONSE_NODE_COOKIES_KEY] = response.cookies
        compiled[ACONST.RESPONSE_NODE_ELAPSED_KEY] = response.elapsed
        compiled[ACONST.RESPONSE_NODE_REASON_KEY] = response.reason
        compiled[ACONST.RESPONSE_NODE_URL_KEY] = response.url
        compiled[ACONST.RESPONSE_NODE_URL_KEY] = response.request.method
        self.disp.log_debug(f"compiled = {compiled}", title)
        return compiled

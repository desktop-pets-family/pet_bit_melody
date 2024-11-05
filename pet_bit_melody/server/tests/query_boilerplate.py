from typing import Union, Mapping, Dict, Any
import requests


class QueryEndpoint:
    """_summary_
        This is the class in charge of containing the boilerplate endpoint functions.
    """

    def __init__(self, host: str = "http://127.0.0.1", port: int = 6000, delay: int = 2) -> None:
        if host.startswith("http") is False:
            self._host = f"http://{host}"
        else:
            self._host = host
        self._port = port
        self._delay = delay

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
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        if content is not None and header is None:
            return requests.get(f"{self._host}:{self._port}/{path}", json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.get(f"{self._host}:{self._port}/{path}", headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.get(f"{self._host}:{self._port}/{path}", json=content, headers=header, timeout=self._delay)
        return requests.get(f"{self._host}:{self._port}/{path}", timeout=self._delay)

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
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        if content is not None and header is None:
            return requests.post(f"{self._host}:{self._port}/{path}", json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.post(f"{self._host}:{self._port}/{path}", headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.post(f"{self._host}:{self._port}/{path}", json=content, headers=header, timeout=self._delay)
        return requests.post(f"{self._host}:{self._port}/{path}", timeout=self._delay)

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
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        if content is not None and header is None:
            return requests.put(f"{self._host}:{self._port}/{path}", json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.put(f"{self._host}:{self._port}/{path}", headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.put(f"{self._host}:{self._port}/{path}", json=content, headers=header, timeout=self._delay)
        return requests.put(f"{self._host}:{self._port}/{path}", timeout=self._delay)

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
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        if content is not None and header is None:
            return requests.patch(f"{self._host}:{self._port}/{path}", json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.patch(f"{self._host}:{self._port}/{path}", headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.patch(f"{self._host}:{self._port}/{path}", json=content, headers=header, timeout=self._delay)
        return requests.patch(f"{self._host}:{self._port}/{path}", timeout=self._delay)

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
        if isinstance(path, str) is False:
            raise ValueError(
                f"Expected an input of type string but got {type(path)}"
            )
        if path[0] == "/":
            path = path[1:]
        if content is not None and header is None:
            return requests.delete(f"{self._host}:{self._port}/{path}", json=content, timeout=self._delay)
        if content is None and header is not None:
            return requests.delete(f"{self._host}:{self._port}/{path}", headers=header, timeout=self._delay)
        if content is not None and header is not None:
            return requests.delete(f"{self._host}:{self._port}/{path}", json=content, headers=header, timeout=self._delay)
        return requests.delete(f"{self._host}:{self._port}/{path}", timeout=self._delay)

    def get_status(self, response: requests.Response) -> int:
        """_summary_
            This function is in charge of getting the status code from the response.
        Args:
            response (requests.Response): _description_: The response from the server.
        Returns:
            int: _description_: The status code from the response.
        """
        return response.status_code

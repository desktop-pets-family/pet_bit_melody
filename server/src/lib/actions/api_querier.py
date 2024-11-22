"""
    File in charge of querying the data from the API
"""

from typing import Dict, Any, List

import json
import urllib.parse
from requests import Response
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME

from .secrets import Secrets
from .variables import Variables
from .logger import ActionLogger
from . import constants as ACONST
from .query_boilerplate import QueryEndpoint

from ..components import constants as CONST
from ..components.runtime_data import RuntimeData


class APIQuerier:
    """_summary_
    """

    def __init__(self, service: Dict[str, Any], variable: Variables, scope: str, runtime_data: RuntimeData, logger: ActionLogger, action_id: int, error: int = 84, success: int = 0, debug: bool = False) -> None:
        """_summary_
            Class in charge of querying the data from the API

        Args:
            service (Dict[str, Any]): _description_
            variable (Variables): _description_: The class variable in charge of tracking the variables for the runtime.
            scope (str): _description_: The scope of the trigger.
            runtime_data (RuntimeData): _description_
            logger (ActionLogger): _description_: The class logger in charge of logging the actions.
            action_id (int): _description_: The action ID to log.
            error (int, optional): _description_. Defaults to 84.
            success (int, optional): _description_. Defaults to 0.
            debug (bool, optional): _description_. Defaults to False.
        """
        title = "APIQuerier"
        self.error: int = error
        self.scope: str = scope
        self.debug: bool = debug
        self.success: int = success
        self.action_id: str = str(action_id)
        self.logger: ActionLogger = logger
        self.variable: Variables = variable
        self.service: Dict[str, Any] = service
        self.runtime_data: RuntimeData = runtime_data
        # ---------------------- The visual logger class  ----------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )
        self.disp.log_debug(f"service: {self.service}", title)
        # ------------------ The class containing the secrets ------------------
        self.secrets: Secrets = Secrets(
            success=self.success,
            error=self.error,
            debug=self.debug
        )
        # ------------------------- Info about the api -------------------------
        self.api_info: Dict[str, Any] = self.get_api_info(
            self.service.get("ignore:id")
        )
        self.update_secrets(self.api_info)
        # ------------------------- The gathered data ---------------------------
        self.disp.log_debug(f"API info: {self.api_info}", title)

    def _log_fatal(self, title: str, msg, action_id: int, raise_item: bool = False, raise_func: object = ValueError) -> int:
        """_summary_
            A function that will log a provided fatal error.

        Args:
            title (str): _description_: the title of the function
            msg (str): _description_: The message to log
            raise_item (bool, optional): _description_. Inform if the logger should raise or just return an error. Defaults to False.
            raise_func (object, optional): _description_. The function to raise if required. Defaults to ValueError.

        Raises:
            ValueError: _description_: One of the possible errors to raise.

        Returns:
            int: _description_: Will return self.error if raise_item is False
        """
        self.disp.log_error(msg, title)
        self.logger.log_fatal(
            ACONST.TYPE_SERVICE_TRIGGER,
            action_id=action_id,
            message=msg,
            resolved=False
        )
        if raise_item is True:
            raise_func(msg)
        else:
            return self.error

    def strip_descriptor(self, node: str) -> str:
        """_summary_
            A function that will strip the descriptor of the given node.

        Args:
            descriptor (str): _description_: The descriptor to strip.

        Returns:
            str: _description_: The stripped descriptor.
        """
        title = "strip_descriptor"
        self.disp.log_debug(f"Node: {node}", title)
        node = node.split(':')[1]
        self.disp.log_debug(f"Node (stripped): {node}", title)
        return node

    def get_api_info(self, api_id: int) -> Dict[str, Any]:
        """_summary_
            Get the API information

        Args:
            api_id (int): _description_

        Returns:
            Dict[str, Any]: _description_
        """
        title = "get_api_info"
        if api_id is None:
            self._log_fatal(
                title=title,
                msg="The API ID is None",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        data = self.runtime_data.database_link.get_data_from_table(
            table=CONST.TAB_SERVICES,
            column="*",
            where=f"id='{api_id}'",
            beautify=True
        )
        if isinstance(data, int) is True or len(data) == 0:
            msg = "Failed to get the API information for"
            msg += f" the API ID: {api_id}"
            self._log_fatal(
                title=title,
                msg=msg,
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        self.disp.log_debug(f"Gathered API info: {data[0]}", title)
        return data[0]

    def update_secrets(self, api_info: Dict[str, Any]) -> None:
        """_summary_
            Update the secrets

        Args:
            api_info (Dict[str, Any]): _description_
        """
        title = "update_secrets"
        if api_info is None:
            self._log_fatal(
                title=title,
                msg="The API info is None",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        node = None
        oauth = api_info.get("oauth")
        if str(oauth) == "0":
            node = api_info.get("api_key")
        elif str(oauth) == "1":
            usr_id = self.variable.get_variable("user_id", self.scope)
            service_id = api_info.get("id")
            if service_id is None or usr_id is None:
                self._log_fatal(
                    title=title,
                    msg="The service ID or user ID is None",
                    action_id=self.action_id,
                    raise_item=True,
                    raise_func=ValueError
                )
            data: Dict[str, Any] = self.runtime_data.database_link.get_data_from_table(
                table=CONST.TAB_ACTIVE_OAUTHS,
                column="*",
                where=[
                    f"user_id='{usr_id}'",
                    f"service_id='{service_id}'"
                ],
                beautify=True
            )
            node = data.get("token")
        else:
            self._log_fatal(
                title=title,
                msg="The oauth token is not valid",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        if node is None:
            self._log_fatal(
                title=title,
                msg="The token is None",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        self.secrets.set_token(node)

    def sanitize_parameter_value(self, url_param: str) -> str:
        """_summary_
            Sanitize the parameter value

        Args:
            url_param (str): _description_

        Returns:
            str: _description_
        """
        title = "sanitize_parameter_value"
        self.disp.log_debug(f"url_param: {url_param}", title)
        if url_param is None:
            return ""
        url_param = urllib.parse.quote(url_param)
        self.disp.log_debug(f"url_param (sanitised): {url_param}", title)
        return url_param

    def get_variable_name(self, var: str) -> str:
        """_summary_
            Get the variable name

        Args:
            var (str): _description_

        Returns:
            str: _description_
        """
        title = "get_variable_name"
        self.disp.log_debug(f"var: {var}", title)
        result = ""
        for i in var:
            if i == "{":
                continue
            if i == "}":
                break
            result += i
        self.disp.log_debug(f"result: {result}", title)
        return result

    def get_special_content(self, var_name: str) -> str:
        """_summary_
            Get the content of a special variable

        Args:
            var_name (str): _description_

        Returns:
            str: _description_
        """
        title = "get_special_content"
        self.disp.log_debug(f"var_name: {var_name}", title)
        node = ""
        lvar_name = var_name.lower()
        if lvar_name in ("secrets.token", "secret.token", "token"):
            node = self.secrets.get_token()
        if lvar_name in ("secrets.bearer", "secret.bearer", "bearer"):
            node = self.secrets.get_bearer()
        if lvar_name in ACONST.SECRETS_EQUIVALENCE:
            msg = f"lvar_name: {lvar_name} found in "
            msg += "ACONST.SECRETS_EQUIVALENCE"
            self.disp.log_debug(msg, title)
            node = ACONST.SECRETS_EQUIVALENCE[lvar_name]()
        self.disp.log_debug(f"node: {node}", title)
        return node

    def get_normal_content(self, var_name: str) -> str:
        """_summary_
            Get the content of a normal variable

        Args:
            var_name (str): _description_

        Returns:
            str: _description_
        """
        title = "get_normal_content"
        self.disp.log_debug(f"var_name: {var_name}", title)
        if self.variable.has_variable(var_name, self.scope) is False:
            self.disp.log_debug(f"Variable {var_name} not found", title)
            return ""
        data = self.variable.get_variable(var_name, self.scope)
        self.disp.log_debug(f"{var_name}: {data}", title)
        return data

    def check_special_vars(self, var: str) -> str:
        """_summary_
            Check the variables

        Args:
            var (str): _description_

        Returns:
            str: _description_
        """
        title = "check_special_vars"
        if var is None or var == "":
            self.disp.log_debug("var is None or empty", title)
            return var
        var_list = var.split("$ref")
        self.disp.log_debug(f"var_list: {var_list}", title)
        for index, item in enumerate(var_list):
            if item == "":
                continue
            if item[0] == "{":
                var_name = self.get_variable_name(item[1:])
                var_content = self.get_special_content(var_name)
                item_new = f"{var_content}{item[len(var_name) + 2:]}"
                self.disp.log_debug(f"item_new: {item_new}", title)
                var_list[index] = item_new
        data = "".join(var_list)
        self.disp.log_debug(f"data: {data}", title)
        return data

    def check_normal_vars(self, var: str) -> str:
        """_summary_
            Check the normal variables

        Args:
            var (str): _description_

        Returns:
            str: _description_
        """
        title = "check_normal_vars"
        if var is None or var == "":
            self.disp.log_debug("var is None or empty", title)
            return var
        var_list = var.split("${")
        self.disp.log_debug(f"var_list: {var_list}", title)
        for index, item in enumerate(var_list):
            if item == "":
                continue
            if item[0] == "{":
                var_name = self.get_variable_name(item[1:])
                var_content = self.get_normal_content(var_name)
                item_new = f"{var_content}{item[len(var_name) + 3:]}"
                self.disp.log_debug(f"item_new: {item_new}", title)
                var_list[index] = item_new
        data = "".join(var_list)
        self.disp.log_debug(f"data: {data}", title)
        return data

    def compile_url_parameters(self, url_params: Dict[str, Any]) -> str:
        """_summary_
            Compile the URL parameters

        Args:
            url_params (Dict[str, Any]): _description_

        Returns:
            str: _description_
        """
        title = "compile_url_parameters"
        url = ""
        param_length = len(url_params)
        index = 0
        self.disp.log_debug(f"url_params: {url_params}", title)
        for key, value in url_params.items():
            key_stripped = self.strip_descriptor(key)
            value = self.check_special_vars(value)
            value = self.check_normal_vars(value)
            if "input:additional_params" == key:
                if value == "":
                    index += 1
                    continue
                url += "&"
                url += self.sanitize_parameter_value(value)
                self.disp.log_debug(f"url: {url}", title)
            url += f"{key_stripped}={self.sanitize_parameter_value(value)}"
            if index < param_length - 2:
                url += "&"
            index += 1
        self.disp.log_debug(f"url: {url}", title)
        return url

    def process_extra_headers(self, header: str) -> Dict[str, Any]:
        """_summary_
            Process the extra headers

        Args:
            header (Dict[str, Any]): _description_

        Returns:
            Dict[str, Any]: _description_
        """
        title = "process_extra_headers"
        if header is None or header == "":
            return {}
        self.disp.log_debug(f"header: {header}", title)
        try:
            header: Dict[str, Any] = json.loads(header)
        except json.JSONDecodeError as e:
            self.disp.log_error(f"Error processing header: {e}", title)
            return {}
        self.disp.log_debug(f"header: {header}", title)
        result = {}
        for key, value in header.items():
            value = self.check_special_vars(value)
            value = self.check_normal_vars(value)
            key_stripped = self.strip_descriptor(key)
            self.disp.log_debug(f"key: {key_stripped}, value: {value}", title)
            result[key_stripped] = value
        self.disp.log_debug(f"header: {result}", title)
        return result

    def process_headers(self, header: Dict[str, Any]) -> Dict[str, Any]:
        """_summary_
            Process the header

        Args:
            header (Dict[str, Any]): _description_

        Returns:
            Dict[str, Any]: _description_
        """
        title = "process_headers"
        if header is None:
            self.disp.log_debug("header: None", title)
            return {}
        self.disp.log_debug(f"header: {header}", title)
        result = {}
        for key, value in header.items():
            if "input:additional_header" == key:
                result.update(self.process_extra_headers(value))
                continue
            value = self.check_special_vars(value)
            value = self.check_normal_vars(value)
            key_stripped = self.strip_descriptor(key)
            self.disp.log_debug(f"key: {key_stripped}, value: {value}", title)
            result[key_stripped] = value
        self.disp.log_debug(f"header: {result}", title)
        return result

    def process_extra_body(self, body: str) -> Dict[str, Any]:
        """_summary_
            Process the extra body

        Args:
            body (str): _description_

        Returns:
            Dict[str, Any]: _description_
        """
        title = "process_extra_body"
        if body is None or body == "":
            return {}
        self.disp.log_debug(f"body: {body}", title)
        try:
            body: Dict[str, Any] = json.loads(body)
        except json.JSONDecodeError as e:
            self.disp.log_error(f"Error processing body: {e}", title)
            return {}
        self.disp.log_debug(f"body: {body}", title)
        result = {}
        for key, value in body.items():
            value = self.check_special_vars(value)
            value = self.check_normal_vars(value)
            key_stripped = self.strip_descriptor(key)
            self.disp.log_debug(f"key: {key_stripped}, value: {value}", title)
            result[key_stripped] = value
        self.disp.log_debug(f"body: {result}", title)
        return result

    def process_body(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """_summary_
            Process the body

        Args:
            body (Dict[str, Any]): _description_

        Returns:
            Dict[str, Any]: _description_
        """
        title = "process_body"
        if body is None:
            self.disp.log_debug("body: None", title)
            return {}
        result = {}
        for key, value in body.items():
            if "input:additional_body" == key:
                result.update(self.process_extra_body(value))
                continue
            value = self.check_special_vars(value)
            value = self.check_normal_vars(value)
            key_stripped = self.strip_descriptor(key)
            self.disp.log_debug(f"key: {key_stripped}, value: {value}", title)
            result[key_stripped] = value
        self.disp.log_debug(f"body: {result}", title)
        return result

    def get_method(self, method: List[str]) -> str:
        """_summary_
            Get the method

        Args:
            method (str): _description_

        Returns:
            str: _description_
        """
        if method is None:
            return "GET"
        selected = None
        default = None
        for i in method:
            if i.startswith("selected:"):
                selected = self.strip_descriptor(i)
                break
            if i.startswith("default:"):
                default = self.strip_descriptor(i)
        if selected is not None:
            return selected
        if default is not None:
            return default
        return "GET"

    def extract_response_code(self, code: Dict[str, Any]) -> int:
        """_summary_
            Extract the code code

        Args:
            code (Dict[str, Any]): _description_

        Returns:
            int: _description_
        """
        title = "extract_response_code"
        default_response: int = 200
        node: str = code.get("int:code")
        if node is None:
            self.disp.log_debug(f"code: {code}", title)
            return default_response
        if isinstance(node, int) is True:
            self.disp.log_debug(f"code: {node}", title)
            return node
        if isinstance(node, str) is True:
            if node.startswith("default:"):
                self.disp.log_debug(f"code: {node}", title)
                return int(self.strip_descriptor(node))
            if node.startswith("selected:"):
                self.disp.log_debug(f"code: {node}", title)
                return int(self.strip_descriptor(node))
            try:
                node = int(node)
                self.disp.log_debug(f"code: {node}", title)
                return node
            except ValueError as e:
                self.disp.log_error(f"code: {node}, err: {e}", title)
                return default_response
        if isinstance(node, List) is False:
            self.disp.log_error(f"code: {node}", title)
            node1 = None
            node2 = None
            for i in node:
                if i.startswith("default:"):
                    node1 = int(self.strip_descriptor(i))
                if i.startswith("selected:"):
                    node2 = int(self.strip_descriptor(i))
            if node2 is not None:
                self.disp.log_debug(f"code: {node2}", title)
                return node2
            if node1 is not None:
                self.disp.log_debug(f"code: {node1}", title)
                return node1
        return default_response

    def check_response_code(self, response: Response, expected_response: int) -> None:
        """_summary_
            Check the response code

        Args:
            response (Response): _description_
            expected_response (int): _description_
        """
        title = "check_response_code"
        if response is None:
            self._log_fatal(
                title=title,
                msg="Response is None",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        if response.status_code != expected_response:
            msg = f"Expected response code: {expected_response},"
            msg += f" got: {response.status_code}"
            self._log_fatal(
                title=title,
                msg=msg,
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )

    def compile_url(self, url_extra: str, url_params: Dict[str, Any]) -> str:
        """_summary_
            Compile the URL

        Args:
            url_extra (str): _description_
            url_params (Dict[str, Any]): _description_

        Returns:
            str: _description_
        """
        url = ""
        if url_extra is not None and len(url_extra) > 0:
            if url_extra[0] == "/":
                url_extra = url_extra[1:]
            url += url_extra
        if url_params is not None and len(url_params) > 0:
            data = self.compile_url_parameters(url_params)
            if data != "":
                url += "?" + data
        return url

    def query(self) -> Response:
        """_summary_
            Query the API

        Returns:
            Response: _description_
        """
        title = "query"
        self.disp.log_debug("In query", title)
        self.disp.log_debug(f"API info: {self.api_info}", title)
        self.disp.log_debug(f"Service info: {self.service}", title)
        self.disp.log_debug("Processing url", title)
        url_extra = self.service.get("input:url_extra")
        url_params = self.service.get("url_params")
        self.disp.log_debug(
            f"url_extra: {url_extra}, url_params: {url_params}", title
        )
        self.disp.log_debug("Processing body", title)
        body = self.process_body(self.service.get("body"))
        self.disp.log_debug("Processing method", title)
        method = self.get_method(self.service.get("drop:method"))
        self.disp.log_debug("Processing headers", title)
        headers = self.process_headers(self.service.get("header"))
        self.disp.log_debug("Compiling url", title)
        url = self.compile_url(url_extra, url_params)
        url_base = self.api_info.get("url")
        if url_base[-1] != "/":
            url_base += "/"
        msg = "Processed data: '"
        msg += f"url_extra: {url_extra}, url_params: {url_params},"
        msg += f" body: {body}, method: {method}, headers: {headers},"
        msg += f" url: {url}, url_base: {url_base}'"
        self.disp.log_debug(msg, title)
        expected_response: Dict[str, Any] = self.service.get("response")
        if expected_response is not None:
            expected_response = self.extract_response_code(expected_response)
        else:
            self._log_fatal(
                title=title,
                msg="Response section not found in service.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        msg = f"Expected response: {expected_response},"
        msg += f" type: {type(expected_response)}"
        self.disp.log_debug(msg, title)
        qei = QueryEndpoint(
            host=url_base,
            port=None,
            delay=CONST.API_REQUEST_DELAY,
            debug=self.debug
        )
        self.disp.log_debug(f"qei = {qei}", title)
        if not body:
            body = None
        if not headers:
            headers = None
        self.disp.log_debug(
            f"final_body = {body}, final_headers = {headers}", title
        )
        self.disp.log_debug(f"url_base = {url_base}", title)
        if url_base in ("https://mail.google.com", "https://mail.google.com/"):
            self.disp.log_debug("Sending email", title)
            receiver = body.get("input:to")
            if receiver is None:
                receiver = body.get("to")
            if receiver is None:
                self._log_fatal(
                    title=title,
                    msg="'to' field not found in body.",
                    action_id=self.action_id,
                    raise_item=True,
                    raise_func=ValueError
                )
            self.disp.log_debug(f"receiver: {receiver}", title)
            subject = body.get("input:subject")
            if subject is None:
                subject = body.get("subject")
            if subject is None:
                self._log_fatal(
                    title=title,
                    msg="'subject' field not found in body.",
                    action_id=self.action_id,
                    raise_item=True,
                    raise_func=ValueError
                )
            self.disp.log_debug(f"subject: {subject}", title)
            email_content = body.get("input:body")
            if email_content is None:
                email_content = body.get("textarea:body")
            if email_content is None:
                email_content = body.get("textearea:body")
            if email_content is None:
                email_content = body.get("body")
            if email_content is None:
                email_content = body.get("input:emailbody")
            if email_content is None:
                email_content = body.get("textarea:emailbody")
            if email_content is None:
                email_content = body.get("textearea:emailbody")
            if email_content is None:
                email_content = body.get("emailbody")
            if email_content is None:
                self._log_fatal(
                    title=title,
                    msg="'body' field not found in body.",
                    action_id=self.action_id,
                    raise_item=True,
                    raise_func=ValueError
                )
            self.disp.log_debug(f"email_content: {email_content}", title)
            response = self.runtime_data.mail_management_initialised.send_email(
                receiver=receiver,
                subject=subject,
                body=email_content,
                body_type="html"
            )
            self.disp.log_debug(f"response: {response}", title)
            if response == self.error:
                self._log_fatal(
                    title=title,
                    msg=f"Failed to send email to {receiver}.",
                    action_id=self.action_id,
                    raise_item=True,
                    raise_func=ValueError
                )
            return response

        response = None
        if method == "GET":
            response = qei.get_endpoint(url, content=body, header=headers)
        elif method == "POST":
            response = qei.post_endpoint(url, content=body, header=headers)
        elif method == "PUT":
            response = qei.put_endpoint(url, content=body, header=headers)
        elif method == "PATCH":
            response = qei.patch_endpoint(url, content=body, header=headers)
        elif method == "DELETE":
            response = qei.delete_endpoint(url, content=body, header=headers)
        elif method == "HEAD":
            response = qei.head_endpoint(url, content=body, header=headers)
        elif method == "OPTIONS":
            response = qei.options_endpoint(url, content=body, header=headers)
        else:
            msg = f"Method {method} is not supported"
            self._log_fatal(
                title=title,
                msg=msg,
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        self.disp.log_debug(f"Response: {response}", title)
        self.disp.log_debug(
            f"Response status_code: {response.status_code}", title
        )
        self.disp.log_debug(f"Expected response: {expected_response}", title)
        self.check_response_code(response, expected_response)
        return response

"""_summary_
    File in charge of checking the trigger rules.
"""

import os
import json
from typing import Any, Dict

from requests import Response
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME

from .secrets import Secrets
from .variables import Variables
from .logger import ActionLogger
from . import constants as ACONST
from .api_querier import APIQuerier
from .query_boilerplate import QueryEndpoint

from ..components import constants as CONST
from ..components.runtime_data import RuntimeData


class TriggerManagement:
    """_summary_
    """

    def __init__(self, variable: Variables, logger: ActionLogger, runtime_data: RuntimeData, scope: Any = "default_scope", action_id: int = 0, error: int = 84, success: int = 0, debug: bool = False, delay: int = 10):
        """_summary_
            This is the class in charge of checking the triggers and storing variables if required.

        Args:
            variable (Variables): _description_: The class variable in charge of tracking the variables for the runtime.
            logger (ActionLogger): _description_: The class logger in charge of logging the actions.
            runtime_data (RuntimeData): _description_: The class runtime data in charge of containing important connections.
            action_id (int): _description_: The action ID to log.
            scope (Any, optional): _description_: The scope of the trigger. Defaults to "default_scope".
            error (int, optional): _description_. Defaults to 84.: The error value
            success (int, optional): _description_. Defaults to 0.: The success value
            debug (bool, optional): _description_. Defaults to False.: Set to True if you wish to activate debug mode.
        """
        # -------------------------- Inherited values --------------------------
        self.error: int = error
        self.scope: Any = scope
        self.delay: int = delay
        self.debug: bool = debug
        self.success: int = success
        self.action_id: str = str(action_id)
        self.logger: ActionLogger = logger
        self.variable: Variables = variable
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
        # ------------------ The class containing the secrets ------------------
        self.secrets: Secrets = Secrets(
            success=self.success,
            error=self.error,
            debug=self.debug
        )
        # ------------- The class in charge of managing endpoints  -------------
        self.query_endpoint: QueryEndpoint = QueryEndpoint(
            host="",
            port=None,
            delay=0,
            debug=self.debug
        )
        # ---------------- The class containing the api querier ----------------
        self.api_querier_initialised: APIQuerier = None
        self.api_response: Dict[str, Any] = None

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

    def get_verification_operator(self, operator: str) -> Any:
        """_summary_
            Get the verification operator.

        Args:
            operator (str): _description_

        Returns:
            Any: _description_
        """
        title = "get_verification_operator"
        self.disp.log_debug(f"Operator: {operator}", title)
        if operator is None or operator == "":
            self._log_fatal(
                title=title,
                msg="No operator found.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=TypeError
            )
        node1 = None
        node2 = None
        for i in operator:
            if i.startswith("selected:"):
                node1 = self.api_querier_initialised.strip_descriptor(i)
            if i.startswith("default:"):
                node2 = self.api_querier_initialised.strip_descriptor(i)
        self.disp.log_debug(f"Node1: {node1}, Node2: {node2}", title)
        if node1 is None and node2 is None:
            self._log_fatal(
                title=title,
                msg="No node found in operator.",
                action_id=0,
                raise_item=True,
                raise_func=TypeError
            )
        self.disp.log_debug(f"Node1: {node1}, Node2: {node2}", title)
        if node1 not in ACONST.OPERATOR_EXCHANGE:
            self.disp.log_debug(
                f"Node1: {node1} not in ACONST.OPERATOR_EXCHANGE", title
            )
            if node2 not in ACONST.OPERATOR_EXCHANGE:
                self.disp.log_debug(
                    f"Node2: {node2} not in ACONST.OPERATOR_EXCHANGE", title
                )
                self._log_fatal(
                    title=title,
                    msg="No node found in operator.",
                    action_id=self.action_id,
                    raise_item=True,
                    raise_func=TypeError
                )
            else:
                response = ACONST.OPERATOR_EXCHANGE[node2]
                self.disp.log_debug(f"Response: {response}", title)
                return response
        else:
            response = ACONST.OPERATOR_EXCHANGE[node1]
            self.disp.log_debug(f"Response: {response}", title)
            return response

    def get_response_verification(self, response_node: Dict[str, Any]) -> Any:
        """_summary_
            Get the response verification.

        Args:
            response_node (Dict[str, Any]): _description_

        Returns:
            Any: _description_
        """
        title = "get_response_verification"
        self.disp.log_debug(f"response_node: {response_node}", title)
        if response_node is None or response_node == "":
            self._log_fatal(
                title=title,
                msg="No response node found.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=TypeError
            )

        for key, values in response_node.items():
            self.disp.log_debug(f"Key: {key}, Values: {values}", title)
            if ":" not in key:
                if key == "response_content":
                    self.disp.log_debug(f"Values: {values}", title)
                    node = values
                    break
            elif self.api_querier_initialised.strip_descriptor(key) == "response_content":
                self.disp.log_debug(f"Values: {values}", title)
                node = values
                break
            else:
                self.disp.log_debug(f"Skipping key: {key}", title)

        self.disp.log_debug(f"Node: {node}", title)
        return node

    def get_verification_value(self, response_node: Dict[str, Any]) -> Any:
        """_summary_
            Get the verification value.

        Args:
            response_node (Dict[str, Any]): _description_

        Returns:
            Any: _description_
        """
        title = "get_verification_value"
        self.disp.log_debug(f"response_node: {response_node}", title)
        if response_node is None or response_node == "":
            self._log_fatal(
                title=title,
                msg="No response node found.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=TypeError
            )

        node = None
        for key, values in response_node.items():
            self.disp.log_debug(f"Key: {key}, Values: {values}", title)
            if ":" not in key:
                if key == "verification_value":
                    self.disp.log_debug(f"Values: {values}", title)
                    node = values
                    break
            elif self.api_querier_initialised.strip_descriptor(key) == "verification_value":
                self.disp.log_debug(f"Values: {values}", title)
                node = values
                break
            else:
                self.disp.log_debug(f"Skipping key: {key}", title)

        self.disp.log_debug(f"Node: {node}", title)
        return node

    def get_response_content(self, variable_name: str) -> Any:
        """_summary_
            Get the response content.

        Args:
            variable_name (str): _description_

        Returns:
            Any: _description_
        """
        title = "get_response_content"
        self.disp.log_debug(f"Variable name: {variable_name}", title)
        if self.api_response is None:
            msg = "No response found"
            msg += f" in {title} for {variable_name} in {self.api_response}."
            self.disp.log_critical(msg, title)
            self._log_fatal(
                title=title,
                msg="No response found.",
                action_id=self.action_id,
                raise_item=False,
                raise_func=TypeError
            )
            return ""
        variable_name_list = variable_name.split(".")
        list_length = len(variable_name_list)
        self.disp.log_debug(f"List length: {list_length}", title)
        if variable_name_list[0] == "body":
            data_type: str = self.api_response.get(
                ACONST.RESPONSE_NODE_BODY_TYPE_KEY
            )
            msg = f"Data type: {data_type}, list_length: {list_length}"
            msg += f" Variable name list: {variable_name_list}"
            self.disp.log_debug(msg, title)
            if data_type is None:
                self._log_fatal(
                    title=title,
                    msg="No data type found.",
                    action_id=self.action_id,
                    raise_item=False,
                    raise_func=TypeError
                )
                return ""
            if data_type.split(";")[0] not in ACONST.CONTENT_TYPES_JSON and list_length > 1:
                msg = "Search depth is not possible for"
                msg += f" this data type {data_type}."
                self._log_fatal(
                    title=title,
                    msg=msg,
                    action_id=self.action_id,
                    raise_item=False,
                    raise_func=TypeError
                )
                return ""
        else:
            msg = "Variable name list: "
            msg += f"{variable_name_list}"
            self.disp.log_debug(msg, title)

        node = self.api_response.copy()
        for index, item in enumerate(variable_name_list):
            if index == 0:
                if item in ACONST.RESPONSE_NODE_KEY_EQUIVALENCE:
                    node: Dict[str, Any] = node.get(
                        ACONST.RESPONSE_NODE_KEY_EQUIVALENCE[item]
                    )
                    self.disp.log_debug(f"Node[{index}]: {node}", title)
                    continue
            if item not in node:
                self.disp.log_error(f"Item: {item} not in node: {node}", title)
                return ""
            node: Dict[str, Any] = node.get(item)
            self.disp.log_debug(f"Node[{index}]: {node}", title)
        self.disp.log_debug(f"Node: {node}", title)
        return node

    def get_variable_data_if_required(self, node: str, attempt_bruteforce: bool = True) -> Any:
        """_summary_
            Get the variable data if required.

        Args:
            node (Dict[str, Any]): _description_

        Returns:
            Any: _description_
        """
        title = "get_variable_data_if_required"
        node_list = node.split("$ref")
        if len(node_list) > 1:
            for index, item in enumerate(node_list):
                if item == "":
                    continue
                if item[0] == "{":
                    var_name = self.api_querier_initialised.get_variable_name(
                        item[1:]
                    )
                    var_content = self.api_querier_initialised.get_special_content(
                        var_name
                    )
                    self.disp.log_debug(f"var_content: {var_content}", title)
                    if var_content == "":
                        var_content = self.get_response_content(var_name)
                        self.disp.log_debug(
                            f"var_content: {var_content}", title
                        )
                    item_new = f"{var_content}{item[len(var_name) + 2:]}"
                    self.disp.log_debug(f"item_new: {item_new}", title)
                    node_list[index] = item_new
            node = "".join(node_list)
        self.disp.log_debug(f"Processed node: {node}", title)
        node_list = node.split("${")
        self.disp.log_debug(f"Node list: {node_list}", title)
        if len(node_list) > 1:
            self.disp.log_debug(f"node_list: {node_list}", title)
            for index, item in enumerate(node_list):
                if item == "":
                    continue
                if item[0] == "{":
                    var_name = self.api_querier_initialised.get_variable_name(
                        item[1:]
                    )
                    var_content = self.api_querier_initialised.get_normal_content(
                        var_name
                    )
                    self.disp.log_debug(f"var_content: {var_content}", title)
                    item_new = f"{var_content}{item[len(var_name) + 3:]}"
                    self.disp.log_debug(f"item_new: {item_new}", title)
                    node_list[index] = item_new
            node = "".join(node_list)
        self.disp.log_debug(f"Node: {node}", title)
        if attempt_bruteforce is True:
            node = ACONST.detect_and_convert(node)
            self.disp.log_warning(f"Node: {node}, type = {type(node)}", title)
        return node

    def check_data_comparison(self, data: Any, operator: ACONST.operator, verification_value: Any) -> bool:
        """_summary_
            Check the data comparison.

        Args:
            data (Any): _description_
            operator (Any): _description_
            verification_value (Any): _description_

        Returns:
            bool: _description_
        """
        title = "check_data_comparison"
        msg = f"data: {data}, operator: {operator}, "
        msg += f"verification_value: {verification_value}"
        self.disp.log_debug(msg, title)
        try:
            operation_result = operator(data, verification_value)
            self.disp.log_debug(f"Operation result: {operation_result}", title)
        except Exception as e:
            self._log_fatal(
                title=title,
                msg=f"Error while comparing data: {e}",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        return operation_result

    def set_runtime_variables(self, data: Dict[str, Any]) -> None:
        """_summary_
            Set the runtime variables.

        Args:
            data (Any): _description_
        """
        title = "set_runtime_variables"
        self.disp.log_debug(f"Data: {data}", title)
        if data is None:
            self._log_fatal(
                title=title,
                msg="No data found.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=TypeError
            )
        if isinstance(data, Dict) is False:
            self._log_fatal(
                title=title,
                msg="Data is not a dictionary.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=TypeError
            )
        for key, value in data.items():
            self.disp.log_debug(f"Key: {key}, Value: {value}", title)
            node = self.get_variable_data_if_required(value)
            self.variable.add_variable(
                key, node, type(node), self.scope
            )

    def run(self, key: str) -> int:
        """_summary_
            Run the trigger checking.

        Returns:
            int: _description_: Returns self.success if the program succeeded, self.error otherwise.
        """
        title = "run"
        self.disp.log_debug("Running trigger management.", title)
        data = self.variable.get_scope(self.scope)
        self.disp.log_debug(
            f"Scope: {self.scope}, scope_content = {data}", title
        )
        if self.variable.has_variable(key, self.scope) is False:
            msg = f"No applet data found for scope {self.scope}"
            msg += f" in pid {os.getpid()}."
            self._log_fatal(
                title, msg, self.action_id, raise_item=True,
                raise_func=ValueError
            )

        action_node = self.variable.get_variable(name=key, scope=self.scope)
        if "trigger" not in action_node:
            self._log_fatal(
                title=title,
                msg="No trigger data found in applet data.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        trigger_node = action_node["trigger"]
        self.disp.log_debug(f"Trigger node: {trigger_node}", title)
        if isinstance(trigger_node, Dict) is False:
            try:
                trigger = json.loads(trigger_node)
            except json.JSONDecodeError as e:
                msg = f"Error while decoding trigger data: {e}"
                self._log_fatal(
                    title, msg, self.action_id, raise_item=True,
                    raise_func=ValueError
                )
        else:
            trigger: Dict[str, Any] = trigger_node
        self.disp.log_debug(f"Trigger data: {trigger}", title)
        node_of_interest = "service"
        if node_of_interest not in trigger:
            self._log_fatal(
                title=title,
                msg="No service data found in trigger data.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        node: Dict[str, Any] = trigger.get(node_of_interest)
        self.api_querier_initialised = APIQuerier(
            service=node,
            variable=self.variable,
            scope=self.scope,
            runtime_data=self.runtime_data,
            logger=self.logger,
            action_id=self.action_id,
            error=self.error,
            success=self.success,
            debug=self.debug
        )
        self.disp.log_debug("self.api_querier_initialised initialised", title)
        response: Response = self.api_querier_initialised.query()
        if response is None:
            self._log_fatal(
                title=title,
                msg="No response found from API query.",
                action_id=self.action_id,
                raise_item=True,
                raise_func=ValueError
            )
        self.disp.log_debug(f"Response: {response}", title)
        data = self.query_endpoint.compile_response_data(response)
        self.disp.log_debug(f"Data: {data}, type = {type(data)}", title)
        self.variable.add_variable(
            "trigger_data", data, type(data), self.scope
        )
        self.api_response = data
        self.disp.log_debug("Variable added.", title)
        verification_operator = self.get_verification_operator(
            node.get("drop:verification_operator")
        )
        response_data = self.get_response_verification(
            node.get("response")
        )
        verification_value = self.get_verification_value(
            node
        )
        self.disp.log_debug("raw Verification info gathered", title)
        msg = f"Verification operator: {verification_operator}, "
        msg += f"response_data = {response_data}, "
        msg += f"verification_value = {verification_value}"
        self.disp.log_debug(msg, title)
        self.disp.log_info("Getting content for response_data", title)
        response_data = self.get_variable_data_if_required(response_data)
        self.disp.log_info("Getting content for verification_value", title)
        verification_value = self.get_variable_data_if_required(
            verification_value
        )
        self.disp.log_debug("Content gathered.", title)
        self.disp.log_debug(f"response_data: {response_data}", title)
        self.disp.log_debug(f"verification_value: {verification_value}", title)
        response = self.check_data_comparison(
            data=response_data,
            operator=verification_operator,
            verification_value=verification_value
        )
        if response is False:
            return self.error
        self.disp.log_debug("Data comparison successful.", title)
        var1 = node.get("variables")
        var2 = node.get("vars")
        if var1 is not None:
            self.set_runtime_variables(var1)
        if var2 is not None:
            self.set_runtime_variables(var2)
        return self.success

"""_summary_
    File in charge of tracking the variables for the current action.
"""

from typing import Dict, Any, Type, Union
import base64
from display_tty import Disp, TOML_CONF, FILE_DESCRIPTOR, SAVE_TO_FILE, FILE_NAME


class ScopeError(Exception):
    """Custom exception to handle scope-related errors."""

    def __init__(self, message="There is a problem with the scope."):
        super().__init__(message)


class VariableNotFoundError(Exception):
    """Custom exception to handle variable-related errors."""

    def __init__(self, message="The variable was not found."):
        super().__init__(message)


class Variables:
    """_summary_
    """

    def __init__(self, success: int = 0, error: int = 84, debug: bool = False):
        """_summary_
            Class in charge of storing and restoring variables.

        Args:
            success (int, optional): _description_. Defaults to 0.
            error (int, optional): _description_. Defaults to 84.
            debug (bool, optional): _description_. Defaults to False.
        """
        # -------------------------- Inherited values --------------------------
        self.success: int = success
        self.error: int = error
        self.debug: bool = debug
        # -------------- The variable tracking runtime variables  --------------
        self.variables: Dict[str, Dict[str, Any]] = {}
        # ---------------------- The visual logger class  ----------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            FILE_DESCRIPTOR,
            debug=self.debug,
            logger=self.__class__.__name__
        )

    def __del__(self) -> None:
        """_summary_
            Destructor for the class.
        """
        title = "__del__"
        self.disp.log_debug("Clearing content", title)
        self.clear_scopes()
        self.disp.log_debug("Scopes cleared", title)

    def create_scope(self, scope_name: Any) -> int:
        """_summary_
            Create a new scope.

        Args:
            scope_name (Any): _description_: The name of the scope.

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise.
        """
        title = "create_scope"
        if scope_name in self.variables:
            self.disp.log_warning(
                f"Scope {scope_name} already present.", title
            )
            return self.error
        self.variables[scope_name] = {}
        self.disp.log_debug(f"Scope {scope_name} created.", title)
        return self.success

    def add_variable(self, name: str, variable_data: Any, variable_type: Type = str, scope: Any = "default_scope") -> int:
        """_summary_
            Add a variable to the current action.

        Args:
            name (str): _description_: The name of the variable
            variable_data (Any): _description_: The data of the given variable
            variable_type (Type): _description_: The type of the data
            scope (str, optional): _description_: The scope of the variable, defaults to "default_scope"

        Raises:
            TypeError: _description_: If the type of the variable is incorrect.

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise.
        """
        title = "add_variable"
        if scope not in self.variables:
            self.disp.log_warning(
                f"scope {scope} not present, creating", title
            )
            self.variables[scope] = {}
        if name in self.variables[scope]:
            self.disp.log_error(f"Variable: {name} is already present.", title)
            return self.error
        if isinstance(variable_data, variable_type) is False:
            msg = f"Incorrect type for variable {name}."
            self.disp.log_error(msg, title)
            raise TypeError(msg)
        self.variables[scope][name] = {
            "data": variable_data, "type": variable_type
        }
        msg = f"Variable: {name} of type {variable_type}"
        msg += f" containing {variable_data} successfully added"
        msg += f" to scope {scope}."
        self.disp.log_debug(msg, title)
        return self.success

    def update_variable(self, name: str, variable_data: Any, variable_type: Type = str, scope: Any = "default_scope") -> int:
        """_summary_
            Update the variable from the current action.

        Args:
            name (str): _description_: The name of the variable
            variable_data (Any): _description_: The data of the given variable
            variable_type (Type): _description_: The type of the data
            scope (str, optional): _description_: The scope in which the data is stored. Defaults to "default_scope"

        Raises:
            ScopeError: _description_: If the scope is not found.
            VariableNotFoundError: _description_: If the variable is not found.
            TypeError: _description_: If the type of the variable is incorrect

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise.
        """
        title = "update_variable"
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_error(msg, title)
            raise ScopeError(msg)
        if name not in self.variables[scope]:
            msg = f"Variable: {name} is not present."
            self.disp.log_error(msg, title)
            raise VariableNotFoundError(msg)
        if isinstance(variable_data, variable_type) is False:
            msg = f"Incorrect type for variable {name}."
            self.disp.log_error(msg, title)
            raise TypeError(msg)
        self.variables[name] = {"data": variable_data, "type": variable_type}
        msg = f"Variable: {name} of type {variable_type}"
        msg += f" containing {variable_data} successfully added"
        msg += f" to scope {scope}."
        self.disp.log_debug(msg, title)
        return self.success

    def insert_or_update(self, name: str, variable_data: Any, variable_type: Type = str, scope: Any = "default_scope") -> int:
        """_summary_
            Insert or update the variable from the current action.

        Args:
            name (str): _description_: The name of the variable
            variable_data (Any): _description_: The data of the given variable
            variable_type (Type): _description_: The type of the data
            scope (str, optional): _description_: The scope in which the data is stored. Defaults to "default_scope"

        Raises:
            ValueError: _description_: If the variable does not exist.
            TypeError: _description_: If the type of the variable is incorrect
            ScopeError: _description_: If the scope is not found.
            VariableNotFoundError: _description_: If the variable is not found.

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise.
        """
        title = "insert_or_update"
        if scope not in self.variables:
            self.disp.log_warning(
                "Scope is not present in the list, adding.", title
            )
            return self.add_variable(name, variable_data, variable_type, scope)
        if name in self.variables[scope]:
            self.disp.log_debug(
                "Variable is already present in the list, updating.", title
            )
            return self.update_variable(name, variable_data, variable_type, scope)
        self.disp.log_debug(
            "Variable is not present in the list, adding.", title
        )
        return self.add_variable(name, variable_data, variable_type, scope)

    def has_variable(self, name: str, scope: Any = "default_scope") -> bool:
        """_summary_
            Check if the variable exists in the current action.

        Args:
            name (str): _description_: The name of the variable
            scope (str, optional): _description_: The scope in which we wish to search for the variable. Enter '*' to search all the variable scopes. Defaults to "default_scope"

        Raises:
            ScopeError: _description_: If the scope is not found.

        Returns:
            bool: _description_: Returns True if the variable exists, False otherwise.
        """
        title = "has_variable"
        self.disp.log_debug(f"Checking if variable {name} exists.", title)
        if scope == "*":
            for key, value in self.variables.items():
                if name in value:
                    self.disp.log_debug(
                        f"Variable {name} exists in scope {key}.", title
                    )
                    return True
            self.disp.log_debug(
                f"Variable {name} does not exist in any scopes.", title
            )
            return False
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_debug(msg, title)
            raise ScopeError(msg)
        if name not in self.variables[scope]:
            self.disp.log_debug(f"Variable {name} does not exist.", title)
            return False
        self.disp.log_debug(f"Variable {name} exists.", title)
        return True

    def get_variable(self, name: str, scope: Any = "default_scope") -> Any:
        """_summary_
            Get the variable from the current action.

        Args:
            name (str): _description_: The name of the variable
            scope (str, optional): _description_: The scope in which to get the variable. Defaults to "default_scope".

        Raises:
            ScopeError: _description_: If the scope is not found.
            ValueError: _description_: If the variable does not exist.

        Returns:
            Any: _description_: Returns the variable if it exists, self.error otherwise.
        """
        title = "get_variable"
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_error(msg, title)
            raise ScopeError(msg)
        if name not in self.variables[scope]:
            msg = f"Variable {name} not found."
            self.disp.log_error(msg, title)
            raise ValueError(msg)
        self.disp.log_debug(f"Variable {name} found.", title)
        return self.variables[scope][name]["data"]

    def get_variables(self, scope: Any = "default_scope") -> Dict[str, Any]:
        """_summary_
            Get all the variables from the current action.

        Args:
            scope (str, optional): _description_: The scope in which to get the variables. User '*' to return all the vairables from all the scopes. Defaults to "default_scope".

        Raises:
            ScopeError: _description_: If the scope is not found.

        Returns:
            Dict[str, Any]: _description_: Returns all the variables.
        """
        title = "get_variables"
        if scope == "*":
            self.disp.log_debug("Returning all the variables.", title)
            return self.variables.copy()
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_error(msg, title)
            raise ScopeError(msg)
        return self.variables[scope]

    def get_scope(self, scope: Any = "default_scope") -> Dict[str, Any]:
        """_summary_
            The function in charge of returning the content of a scope.
            This function is just there for program logic.
            This is function behaves the exact same way as the get_variables function.

        Args:
            scope (str, optional): _description_: The scope in which to get the variables. User '*' to return all the vairables from all the scopes. Defaults to "default_scope".

        Raises:
            ScopeError: _description_: If the scope is not found.

        Returns:
            Dict[str, Any]: _description_: Returns all the variables.
        """
        return self.get_variables(scope=scope)

    def get_variable_type(self, name: str, scope: Any = "default_scope") -> Union[int, Type]:
        """_summary_
            Get the type of the variable from the current action.

        Args:
            name (str): _description_: The name of the variable
            scope (str, optional): _description_: The scope in which to get the variable. Defaults to "default_scope".

        Raises:
            ScopeError: _description_: If the scope is not
            ValueError: _description_: If the variable does not exist.

        Returns:
            Type: _description_: Returns the type of the variable if it exists, self.error otherwise.
        """
        title = "get_variable_type"
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_error(msg, title)
            raise ScopeError(msg)
        if name not in self.variables[scope]:
            msg = f"Variable {name} does not exist in scope {scope}."
            self.disp.log_error(msg, title)
            raise ValueError(msg)
        self.disp.log_debug(f"Retrieving type for {name}", title)
        return self.variables[scope][name]["type"]

    def remove_variable(self, name: str, scope: Any = "default_scope") -> int:
        """_summary_
            Remove the variable from the current action.

        Args:
            name (str): _description_: The name of the variable
            scope (str, optional): _description_:  The scope in which the variable is stored. Defaults to "default_scope".

        Raises:
            ScopeError: _description_: If the scope is not found.
            VariableNotFoundError: _description_: If the variable is not found.

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise.
        """
        title = "remove_variable"
        msg = f"Removing variable {name} from the scope {scope}"
        msg += " if present."
        self.disp.log_debug(msg, title)
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_error(msg, title)
            raise ScopeError(msg)
        if name not in self.variables[scope]:
            msg = f"Variable {name} is not present"
            msg += f" in scope {scope}."
            self.disp.log_error(msg, title)
            raise VariableNotFoundError(msg)
        msg = f"Removing variable {name} "
        msg += f"from the scope {scope}."
        self.disp.log_debug(msg, title)
        del self.variables[scope][name]
        return self.success

    def clear_variables(self, scope: Any = "default_scope") -> int:
        """_summary_
            Clear all the variables from the current action.

        Args:
            scope (str, optional): _description_: The scope in which to clear the variables. Enter '*' to clear the content of all the scopes. Defaults to "default_scope".

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise.
        """
        title = "clear_variables"
        self.disp.log_debug(
            f"Clearing all the variables in scope {scope}.", title
        )
        if scope == "*":
            for i in self.variables:
                self.disp.log_debug(f"Clearing content for scope {i}", title)
                self.variables[i] = {}
            self.disp.log_debug("All the variables have been cleared.", title)
            return self.success
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_error(msg, title)
            raise ScopeError(msg)
        self.variables[scope] = {}
        self.disp.log_debug(
            f"All the variables have been cleared for scope {scope}.", title
        )
        return self.success

    def clear_scopes(self) -> int:
        """_summary_
            Clear all the scopes from the current action.

        Returns:
            int: _description_
        """
        title = "clear_scopes"
        self.disp.log_debug("Clearing all the scopes.", title)
        self.variables = {}
        self.disp.log_debug("All the scopes have been cleared.", title)
        return self.success

    def clear_scope_contents(self) -> int:
        """_summary_
            Clear all the scopes content from the current action.

        Returns:
            int: _description_
        """
        title = "clear_scope_contents"
        self.disp.log_debug("Clearing all the scopes.", title)
        for i in self.variables:
            self.disp.log_debug(f"Clearing content for scope {i}", title)
            self.variables[i] = {}
        self.disp.log_debug("All the scopes have been cleared.", title)
        return self.success

    def remove_scope(self, scope: Any) -> int:
        """_summary_
            Remove the scope from the current action.

        Args:
            scope (str): _description_: The scope to remove.

        Raises:
            ScopeError: _description_: If the scope is not found.

        Returns:
            int: _description_: Returns self.success if it succeeds, self.error otherwise.
        """
        title = "remove_scope"
        self.disp.log_debug(f"Removing scope {scope}.", title)
        if scope not in self.variables:
            msg = f"Scope {scope} not found."
            self.disp.log_error(msg, title)
            raise ScopeError(msg)
        del self.variables[scope]
        self.disp.log_debug(f"Scope {scope} removed.", title)
        return self.success

    def sanitize_for_json(self, data_or_scope: Any, use_scope: bool = False) -> Any:
        """_summary_
            Sanitize the data for json serialization.

        Args:
            data (Any): _description_: The data to sanitize.
            use_scope (bool, optional): _description_: Specify if the data to process is to be queried in the variable scopes. Default: False

        Raises:
            ScopeError: _description_: If the scope is not found.

        Returns:
            Any: _description_: The sanitized data.
        """
        title = "sanitize_for_json"
        if use_scope is True:
            if data_or_scope not in self.variables:
                msg = f"The provided scope {data_or_scope}"
                msg += " was not found in the current dataset."
                self.disp.log_debug(msg, title)
                raise ScopeError(msg)
            self.disp.log_debug(f"Sanitising scope {data_or_scope}", title)
            return self.sanitize_for_json(self.variables[data_or_scope], False)
        if isinstance(data_or_scope, dict):
            for key, value in data_or_scope.items():
                data_or_scope[key] = self.sanitize_for_json(value)
        elif isinstance(data_or_scope, list):
            for index, item in enumerate(data_or_scope):
                data_or_scope[index] = self.sanitize_for_json(item)
        elif isinstance(data_or_scope, set):
            data_or_scope = list(data_or_scope)
            for index, item in enumerate(data_or_scope):
                data_or_scope[index] = self.sanitize_for_json(item)
        elif isinstance(data_or_scope, tuple):
            data_or_scope = list(data_or_scope)
            for index, item in enumerate(data_or_scope):
                data_or_scope[index] = self.sanitize_for_json(item)
            data_or_scope = tuple(data_or_scope)
        elif isinstance(data_or_scope, bytes):
            data_or_scope = base64.b64encode(data_or_scope).decode('utf-8')
        elif isinstance(data_or_scope, (int, float, str, bool)) is False:
            data_or_scope = str(data_or_scope)
        return data_or_scope

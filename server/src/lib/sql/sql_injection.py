"""
    EPITECH PROJECT, 2022
    Desktop_pet (Workspace)
    File description:
    injection.py

    The file un charge of checking if an injection is attempted with the open database
"""

import base64
from typing import Union, List

from display_tty import Disp, TOML_CONF, SAVE_TO_FILE, FILE_NAME


class SQLInjection:
    """ Check if an sql injection is present """

    def __init__(self, error: int = 84, success: int = 0, debug: bool = False) -> None:
        # ---------------------------- Status codes ----------------------------
        self.debug: bool = debug
        self.error: int = error
        self.success: int = success
        # ---------------------------- Logging data ----------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            self.debug,
            logger=self.__class__.__name__
        )
        # ------------------ Injection checking related data  ------------------
        self.injection_err: int = (-1)
        self.injection_message: str = "Injection attempt detected"
        self.symbols: List[str] = [';', '--', '/*', '*/']
        self.keywords: List[str] = [
            'SELECT', 'INSERT', 'UPDATE', 'DELETE',
            'DROP', 'CREATE', 'ALTER', 'TABLE', 'UNION', 'JOIN', 'WHERE'
        ]
        self.command: List[str] = self.keywords
        self.logic_gates: List[str] = ['OR', 'AND', 'NOT']
        self.all: List[str] = []
        self.all.extend(self.keywords)
        self.all.extend(self.symbols)
        self.all.extend(self.keywords)

    def _perror(self, string: str = "") -> None:
        """ Print an error message """
        self.disp.disp_print_error(f"(Injection) {string}")

    def _is_base64(self, string: str) -> bool:
        """ Check if a string is base64 encoded """
        try:
            base64.b64decode(string, validate=True)
            return True
        except Exception:
            return False

    def check_if_symbol_sql_injection(self, string: Union[str, List[str]]) -> bool:
        """ Check if symbols are the source of the injection """
        if isinstance(string, List) is True:
            for i in string:
                if self.check_if_symbol_sql_injection(i) is True:
                    return True
            return False
        if isinstance(string, str) is True:
            if ";base64" in string:
                return self._is_base64(string)
            for i in self.symbols:
                if i in string:
                    self.disp.log_debug(
                        f"Failed for {string}, node {i} was found.",
                        "check_if_symbol_sql_injection"
                    )
                    return True
        else:
            msg = "(check_if_symbol_sql_injection) string must be a string or a List of strings"
            self._perror(msg)
            return True
        return False

    def check_if_command_sql_injection(self, string: Union[str, List[str]]) -> bool:
        """ Check if sql keywords are present """
        if self.debug is True:
            msg = "(check_if_command_sql_injection) string = "
            msg += f"'{string}', type(string) = '{type(string)}'"
            self.disp.disp_print_debug(msg)
        if isinstance(string, List) is True:
            for i in string:
                if self.check_if_command_sql_injection(i) is True:
                    return True
            return False
        if isinstance(string, str) is True:
            for i in self.keywords:
                if i in string:
                    self.disp.log_debug(
                        f"Failed for {string}, node {i} was found.",
                        "check_if_command_sql_injection"
                    )
                    return True
        else:
            msg = "(check_if_command_sql_injection) string must be a string or a List of strings"
            self._perror(msg)
            return True
        return False

    def check_if_logic_gate_sql_injection(self, string: Union[str, List[str]]) -> bool:
        """ Check if a logic gate is present """
        if isinstance(string, List) is True:
            for i in string:
                if self.check_if_logic_gate_sql_injection(i) is True:
                    return True
            return False
        if isinstance(string, str) is True:
            for i in self.logic_gates:
                if i in string:
                    self.disp.log_debug(
                        f"Failed for {string}, node {i} was found.",
                        "check_if_logic_gate_sql_injection"
                    )
                    return True
        else:
            msg = "(check_if_logic_gate_sql_injection) string must be a string or a List of strings"
            self._perror(msg)
            return True
        return False

    def check_if_symbol_and_command_injection(self, string: Union[str, List[str]]) -> bool:
        """ Check if symbols and commands are the source of the injection """
        is_symbol = self.check_if_symbol_sql_injection(string)
        is_command = self.check_if_command_sql_injection(string)
        if is_symbol is True or is_command is True:
            return True
        return False

    def check_if_symbol_and_logic_gate_injection(self, string: Union[str, List[str]]) -> bool:
        """ Check if symbols and logic gates are the source of the injection """
        is_symbol = self.check_if_symbol_sql_injection(string)
        is_logic_gate = self.check_if_logic_gate_sql_injection(string)
        if is_symbol is True or is_logic_gate is True:
            return True
        return False

    def check_if_command_and_logic_gate_injection(self, string: Union[str, List[str]]) -> bool:
        """ Check if command and logic gates are the source of the injection """
        is_command = self.check_if_command_sql_injection(string)
        is_logic_gate = self.check_if_logic_gate_sql_injection(string)
        if is_command is True or is_logic_gate is True:
            return True
        return False

    def check_if_sql_injection(self, string: Union[str, List[str]]) -> bool:
        """ Check if there is an sql injection, uses all the parameters """
        if isinstance(string, List) is True:
            for i in string:
                if self.check_if_sql_injection(i) is True:
                    return True
            return False
        if isinstance(string, str) is True:
            if ";base64" in string:
                return self._is_base64(string)
            for i in self.all:
                if i in string:
                    return True
        else:
            msg = "(check_if_sql_injection) string must be a string or a List of strings"
            self._perror(msg)
            return True
        return False

    def check_if_injections_in_strings(self, array_of_strings: Union[str, List[str], List[List[str]]]) -> bool:
        """ Check if there is an injection in the provided array of strings """
        if isinstance(array_of_strings, List) is True:
            for i in array_of_strings:
                if isinstance(i, List) is True:
                    if self.check_if_injections_in_strings(i) is True:
                        return True
                    continue
                if isinstance(i, str) is False:
                    err_message = "(check_if_injections_in_strings) Expected a string but "
                    err_message += f"got an {type(i)}"
                    self._perror(err_message)
                    return True
                if self.check_if_sql_injection(i) is True:
                    return True
            return False
        if isinstance(array_of_strings, str) is True:
            if self.check_if_sql_injection(array_of_strings) is True:
                return True
            return False
        err_message = "(check_if_injections_in_strings) The provided item is neither a List a table or a string"
        self._perror(err_message)
        return False

    def run_test(self, title: str, array: List[str], function: object, expected_response: bool = False, global_status: int = 0) -> int:
        """ Run a test and return it's status"""
        err = 84
        global_response = global_status
        print(f"{title}", end="")
        for i in array:
            print(".", end="")
            response = function(i)
            if response != expected_response:
                print("[error]")
                global_response = err
        print("[success]")
        return global_response

    def test_injection_class(self) -> int:
        """ Test the injection class """
        success = 0
        global_status = success
        test_sentences = [
            "SHOW TABLES;",
            "SHOW Databases;",
            "DROP TABLES;",
            "SHOW DATABASE;",
            "SELECT * FROM table;",
        ]
        global_status = self.run_test(
            title="Logic gate test:",
            array=self.logic_gates,
            function=self.check_if_logic_gate_sql_injection,
            expected_response=True,
            global_status=global_status
        )
        global_status = self.run_test(
            title="Keyword check:",
            array=self.keywords,
            function=self.check_if_command_sql_injection,
            expected_response=True,
            global_status=global_status
        )
        global_status = self.run_test(
            title="Symbol check:",
            array=self.symbols,
            function=self.check_if_symbol_sql_injection,
            expected_response=True,
            global_status=global_status
        )
        global_status = self.run_test(
            title="All injections:",
            array=self.all,
            function=self.check_if_sql_injection,
            expected_response=True,
            global_status=global_status
        )
        global_status = self.run_test(
            title="Array check:",
            array=[self.all],
            function=self.check_if_injections_in_strings,
            expected_response=True,
            global_status=global_status
        )
        global_status = self.run_test(
            title="Double array check:",
            array=[self.all, self.all],
            function=self.check_if_injections_in_strings,
            expected_response=True,
            global_status=global_status
        )
        global_status = self.run_test(
            title="SQL sentences:",
            array=test_sentences,
            function=self.check_if_sql_injection,
            expected_response=True,
            global_status=global_status
        )
        return global_status


if __name__ == "__main__":
    II = SQLInjection()
    res = II.test_injection_class()
    print(f"test status = {res}")

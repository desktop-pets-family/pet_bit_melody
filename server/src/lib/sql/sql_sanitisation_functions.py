"""
    File in charge of cleaning and sanitising sql queries before they are submitted to the database.
"""

from typing import List, Dict, Any, Union

from display_tty import Disp, TOML_CONF, SAVE_TO_FILE, FILE_NAME

from . import sql_constants as SCONST
from .sql_time_manipulation import SQLTimeManipulation


class SQLSanitiseFunctions:
    """_summary_
    """

    def __init__(self, success: int = 0, error: int = 84, debug: bool = False) -> None:
        """_summary_
            This is the class that contains functions in charge of sanitising sql queries.

        Args:
            debug (bool, optional): _description_. Defaults to False.: enable debug mode
        """
        self.error: int = error
        self.debug: bool = debug
        self.success: int = success
        # --------------------------- logger section ---------------------------
        self.disp: Disp = Disp(
            TOML_CONF,
            SAVE_TO_FILE,
            FILE_NAME,
            debug=self.debug,
            logger=self.__class__.__name__
        )
        # ----------------- Database risky keyword sanitising  -----------------
        self.risky_keywords: List[str] = SCONST.RISKY_KEYWORDS
        self.keyword_logic_gates: List[str] = SCONST.KEYWORD_LOGIC_GATES
        # ---------------------- Time manipulation class  ----------------------
        self.sql_time_manipulation: SQLTimeManipulation = SQLTimeManipulation(
            self.debug
        )

    def protect_sql_cell(self, cell: str) -> str:
        """_summary_
            This is a function in charge of cleaning by nullifying (escaping) characters that could cause the sql command to break.

        Args:
            cells (str): _description_: The cell to be checked

        Returns:
            str: _description_: A (hopfully) clean string.
        """
        result = ""
        for char in cell:
            if char in ("'", '"', "\\", '\0', "\r"):
                self.disp.log_info(
                    f"Escaped character '{char}' in '{cell}'.",
                    "_protect_sql_cell"
                )
                result += "\\"+char
            else:
                result += char
        return result

    def escape_risky_column_names(self, columns: Union[List[str], str]) -> Union[List[str], str]:
        """_summary_
            Escape the risky column names.

        Args:
            columns (List[str]): _description_

        Returns:
            List[str]: _description_
        """
        title = "_escape_risky_column_names"
        self.disp.log_debug("Escaping risky column names.", title)
        if isinstance(columns, str):
            data = [columns]
        else:
            data = columns
        for index, item in enumerate(data):
            if "=" in item:
                key, value = item.split("=", maxsplit=1)
                self.disp.log_debug(f"key = {key}, value = {value}", title)
                if key.lower() in self.risky_keywords:
                    self.disp.log_warning(
                        f"Escaping risky column name '{key}'.",
                        "_escape_risky_column_names"
                    )
                    data[index] = f"`{key}`={value}"
            elif item.lower() in self.risky_keywords:
                self.disp.log_warning(
                    f"Escaping risky column name '{item}'.",
                    "_escape_risky_column_names"
                )
                data[index] = f"`{item}`"
            else:
                continue
        self.disp.log_debug("Escaped risky column names.", title)
        if isinstance(columns, str):
            return data[0]
        return columns

    def _protect_value(self, value: str) -> str:
        """Ensures the value is safely passed as a string in an SQL query.
        It wraps the value in single quotes and escapes any single quotes within the value.

        Args:
            value (str): The value that needs to be protected.

        Returns:
            str: The value with protection applied, safe for SQL queries.
        """
        title = "_protect_value"
        self.disp.log_debug(f"protecting value: {value}", title)
        if value is None:
            self.disp.log_debug("Value is none, thus returning NULL", title)
            return "NULL"

        if isinstance(value, str) is False:
            self.disp.log_debug("Value is not a string, converting", title)
            value = str(value)

        if len(value) == 0:
            self.disp.log_debug("Value is empty, returning ''", title)
            return "''"

        if value[0] == '`' and value[-1] == '`':
            self.disp.log_debug(
                "string has special backtics, skipping.", title
            )
            return value

        if value[0] == "'":
            self.disp.log_debug(
                "Value already has a single quote at the start, removing", title
            )
            value = value[1:]
        if value[-1] == "'":
            self.disp.log_debug(
                "Value already has a single quote at the end, removing", title
            )
            value = value[:-1]

        self.disp.log_debug(
            f"Value before quote escaping: {value}", title
        )
        protected_value = value.replace("'", "''")
        self.disp.log_debug(
            f"Value after quote escaping: {protected_value}", title
        )

        protected_value = f"'{protected_value}'"
        self.disp.log_debug(
            f"Value after being converted to a string: {protected_value}.",
            title
        )
        return protected_value

    def escape_risky_column_names_where_mode(self, columns: Union[List[str], str]) -> Union[List[str], str]:
        """
        Escape the risky column names in where mode, except for those in keyword_logic_gates.

        Args:
            columns (Union[str, List[str]]): Column names to be processed.

        Returns:
            Union[List[str], str]: Processed column names with risky ones escaped.
        """
        title = "_escape_risky_column_names_where_mode"
        self.disp.log_debug(
            "Escaping risky column names in where mode.", title
        )

        if isinstance(columns, str):
            data = [columns]
        else:
            data = columns

        for index, item in enumerate(data):
            if "=" in item:
                key, value = item.split("=", maxsplit=1)
                self.disp.log_debug(f"key = {key}, value = {value}", title)

                protected_value = self._protect_value(value)
                if key.lower() not in self.keyword_logic_gates and key.lower() in self.risky_keywords:
                    self.disp.log_warning(
                        f"Escaping risky column name '{key}'.", title
                    )
                    data[index] = f"`{key}`={protected_value}"
                else:
                    data[index] = f"{key}={protected_value}"

            elif item.lower() not in self.keyword_logic_gates and item.lower() in self.risky_keywords:
                self.disp.log_warning(
                    f"Escaping risky column name '{item}'.",
                    title
                )
                protected_value = self._protect_value(item)
                data[index] = protected_value

        self.disp.log_debug("Escaped risky column names in where mode.", title)

        if isinstance(columns, str):
            return data[0]
        return data

    def check_sql_cell(self, cell: str) -> str:
        """_summary_
            Check if the cell is a string or a number.

        Args:
            cell (str): _description_

        Returns:
            str: _description_
        """
        if isinstance(cell, (str, float)) is True:
            cell = str(cell)
        if isinstance(cell, str) is False:
            msg = "The expected type of the input is a string,"
            msg += f"but got {type(cell)}"
            self.disp.log_error(msg, "_check_sql_cell")
            return cell
        cell = self.protect_sql_cell(cell)
        tmp = cell.lower()
        if tmp in ("now", "now()"):
            tmp = self.sql_time_manipulation.get_correct_now_value()
        elif tmp in ("current_date", "current_date()"):
            tmp = self.sql_time_manipulation.get_correct_current_date_value()
        else:
            tmp = str(cell)
        if ";base" not in tmp:
            self.disp.log_debug(f"result = {tmp}", "_check_sql_cell")
        return f"\"{str(tmp)}\""

    def beautify_table(self, column_names: List[str], table_content: List[List[Any]]) -> Union[List[Dict[str, Any]], int]:
        """_summary_
            Convert the table to an easier version for navigating.

        Args:
            column_names (List[str]): _description_
            table_content (List[List[Any]]): _description_

        Returns:
            Union[List[Dict[str, Any]], int]: _description_: the formated content or self.error if an error occured.
        """
        data: List[Dict[str, Any]] = []
        v_index: int = 0
        if len(column_names) == 0:
            self.disp.log_error(
                "There are not provided table column names.",
                "_beautify_table"
            )
            return table_content
        if len(table_content) == 0:
            self.disp.log_error(
                "There is no table content.",
                "_beautify_table"
            )
            return self.error
        column_length = len(column_names)
        for i in table_content:
            cell_length = len(i)
            if cell_length != column_length:
                self.disp.log_warning(
                    "Table content and column lengths do not correspond.",
                    "_beautify_table"
                )
            data.append({})
            for index, items in enumerate(column_names):
                if index == cell_length:
                    self.disp.log_warning(
                        "Skipping the rest of the tuple because it is shorter than the column names.",
                        "_beautify_table"
                    )
                    break
                data[v_index][items[0]] = i[index]
            v_index += 1
        self.disp.log_debug(f"beautified_table = {data}", "_beautify_table")
        return data

    def compile_update_line(self, line: List, column: List, column_length: int) -> str:
        """_summary_
            Compile the line required for an sql update to work.

        Args:
            line (List): _description_
            column (List): _description_
            column_length (int): _description_

        Returns:
            str: _description_
        """
        title = "compile_update_line"
        final_line = ""
        self.disp.log_debug("Compiling update line.", title)
        for i in range(0, column_length):
            cell_content = self.check_sql_cell(line[i])
            final_line += f"{column[i]} = {cell_content}"
            if i < column_length - 1:
                final_line += ", "
            if i == column_length:
                break
        self.disp.log_debug(f"line = {final_line}", title)
        return final_line

    def process_sql_line(self, line: List[str], column: List[str], column_length: int = (-1)) -> str:
        """_summary_
            Convert a List of strings to an sql line so that it can be inserted into a table.

        Args:
            line (List[str]): _description_

        Returns:
            str: _description_
        """
        if column_length == -1:
            column_length = len(column)
        line_length = len(line)

        line_final = "("
        if self.debug is True and ";base" not in str(line):
            msg = f"line = {line}"
            self.disp.log_debug(msg, "_process_sql_line")
        for i in range(0, column_length):
            line_final += self.check_sql_cell(line[i])
            if i < column_length - 1:
                line_final += ", "
            if i == column_length:
                if i < line_length:
                    msg = "The line is longer than the number of columns, truncating."
                    self.disp.log_warning(msg, "_process_sql_line")
                break
        line_final += ")"
        if ";base" not in str(line_final):
            msg = f"line_final = '{line_final}'"
            msg += f", type(line_final) = '{type(line_final)}'"
            self.disp.log_debug(msg, "_process_sql_line")
        return line_final

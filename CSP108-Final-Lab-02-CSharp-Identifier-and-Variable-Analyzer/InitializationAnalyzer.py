import re

from BaseAnalyzer import BaseAnalyzer
from Lexer import Lexer


class InitializationAnalyzer(
    BaseAnalyzer
):
    """
    Checks C# variable initialization.

    Example:
    int age = 21;
    """

    def analyze(self):

        text = (
            self.get_input().strip()
        )

        tokens = (
            self._lexer.tokenize(text)
        )

        if not text.endswith(";"):

            self._errors.add_error(
                "Syntax Error",
                "Initialization must end with ';'."
            )

        pattern = (
            r"(\S+)\s+(\S+)"
            r"\s*=\s*(.+?)\s*;"
        )

        match = re.fullmatch(
            pattern,
            text
        )

        if match is None:

            self._errors.add_error(
                "Syntax Error",
                "Correct format: "
                "dataType variableName = value;"
            )

            return (
                tokens,
                self._errors.get_errors()
            )

        data_type = match.group(1)

        variable_name = match.group(2)

        value = match.group(3)

        if data_type not in (
            Lexer.DATA_TYPES
        ):

            self._errors.add_error(
                "Semantic Error",
                data_type
                + " is not a supported data type."
            )

        self.check_identifier(
            variable_name
        )

        self.check_value(
            data_type,
            value
        )

        return (
            tokens,
            self._errors.get_errors()
        )

    def check_value(
        self,
        data_type,
        value
    ):
        """
        Checks whether the value
        matches the selected data type.
        """

        value = value.strip()

        valid = False

        if data_type == "int":

            valid = bool(
                re.fullmatch(
                    r"[+-]?\d+",
                    value
                )
            )

        elif data_type in {
            "long",
            "short",
            "byte"
        }:

            valid = bool(
                re.fullmatch(
                    r"[+-]?\d+",
                    value
                )
            )

        elif data_type == "double":

            valid = bool(
                re.fullmatch(
                    r"[+-]?\d+(\.\d+)?",
                    value
                )
            )

        elif data_type == "float":

            valid = bool(
                re.fullmatch(
                    r"[+-]?\d+(\.\d+)?[fF]",
                    value
                )
            )

        elif data_type == "decimal":

            valid = bool(
                re.fullmatch(
                    r"[+-]?\d+(\.\d+)?[mM]",
                    value
                )
            )

        elif data_type == "string":

            valid = bool(
                re.fullmatch(
                    r'"[^"]*"',
                    value
                )
            )

        elif data_type == "char":

            valid = bool(
                re.fullmatch(
                    r"'[^']'",
                    value
                )
            )

        elif data_type == "bool":

            valid = value in {
                "true",
                "false"
            }

        if not valid:

            self._errors.add_error(
                "Semantic Error",
                "Value "
                + value
                + " is not compatible with "
                + data_type
                + "."
            )
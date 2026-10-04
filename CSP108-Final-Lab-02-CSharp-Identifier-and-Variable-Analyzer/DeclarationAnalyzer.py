import re

from BaseAnalyzer import BaseAnalyzer
from Lexer import Lexer


class DeclarationAnalyzer(
    BaseAnalyzer
):
    """
    Checks C# variable declarations.

    Example:
    int age;
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
                "Declaration must end with ';'."
            )

        pattern = (
            r"(\S+)\s+(\S+)\s*;"
        )

        match = re.fullmatch(
            pattern,
            text
        )

        if match is None:

            self._errors.add_error(
                "Syntax Error",
                "Correct format: dataType variableName;"
            )

            return (
                tokens,
                self._errors.get_errors()
            )

        data_type = match.group(1)

        variable_name = match.group(2)

        if data_type not in (
            Lexer.DATA_TYPES
        ):

            self._errors.add_error(
                "Semantic Error",
                data_type
                + " is not a valid supported data type."
            )

        self.check_identifier(
            variable_name
        )

        return (
            tokens,
            self._errors.get_errors()
        )
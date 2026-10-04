import re

from abc import ABC, abstractmethod

from Lexer import Lexer
from ErrorHandler import ErrorHandler


class BaseAnalyzer(ABC):
    """
    Parent class for all analyzers.

    Abstraction:
    analyze() is abstract.

    Encapsulation:
    input is stored privately.
    """

    def __init__(self, input_text):

        self.__input_text = (
            input_text
        )

        self._lexer = Lexer()

        self._errors = ErrorHandler()

    def get_input(self):

        return self.__input_text

    def check_identifier(
        self,
        identifier
    ):

        if identifier in (
            Lexer.DATA_TYPES
        ):

            self._errors.add_error(
                "Syntax Error",
                identifier
                + " is a reserved data type."
            )

            return

        if identifier in (
            Lexer.RESERVED_WORDS
        ):

            self._errors.add_error(
                "Syntax Error",
                identifier
                + " is a reserved keyword."
            )

            return

        if not re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*",
            identifier
        ):

            self._errors.add_error(
                "Syntax Error",
                "Invalid identifier name."
            )

    @abstractmethod
    def analyze(self):

        pass
from abc import ABC, abstractmethod

from Lexer import Lexer
from ErrorHandler import ErrorHandler


class BaseAnalyzer(ABC):
    """
    Abstract parent class.

    OOP:
    Abstraction - analyze() is abstract.
    Encapsulation - source code is private.
    """

    def __init__(self, code):

        # Encapsulation
        self.__code = code

        self._lexer = Lexer()
        self._errors = ErrorHandler()

    def get_code(self):
        return self.__code

    @abstractmethod
    def analyze(self):
        """
        Every child class must
        create its own analyze method.
        """
        pass
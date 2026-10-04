from BaseAnalyzer import BaseAnalyzer

from Lexer import Lexer


class DataTypeAnalyzer(BaseAnalyzer):
    """
    Checks C# data types.
    """

    def analyze(self):

        text = (
            self.get_input().strip()
        )

        tokens = (
            self._lexer.tokenize(text)
        )

        if text not in Lexer.DATA_TYPES:

            self._errors.add_error(
                "Semantic Error",
                text
                + " is not a supported C# data type."
            )

        return (
            tokens,
            self._errors.get_errors()
        )
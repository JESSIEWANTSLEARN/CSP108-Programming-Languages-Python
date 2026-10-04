from BaseAnalyzer import BaseAnalyzer


class IdentifierAnalyzer(BaseAnalyzer):
    """
    Checks whether a C# identifier
    is valid or invalid.
    """

    def analyze(self):

        text = (
            self.get_input().strip()
        )

        tokens = (
            self._lexer.tokenize(text)
        )

        if text == "":

            self._errors.add_error(
                "Syntax Error",
                "Identifier cannot be empty."
            )

        else:

            self.check_identifier(text)

        return (
            tokens,
            self._errors.get_errors()
        )
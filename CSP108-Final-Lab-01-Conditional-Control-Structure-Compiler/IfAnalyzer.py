import re

from BaseAnalyzer import BaseAnalyzer


class IfAnalyzer(BaseAnalyzer):
    """
    Analyzes C# if statements.

    Inheritance:
    IfAnalyzer inherits BaseAnalyzer.

    Polymorphism:
    analyze() is overridden.
    """

    def analyze(self):

        code = self.get_code().strip()

        tokens = self._lexer.tokenize(code)

        # Check if statement starts with IF.
        if not code.startswith("if"):
            self._errors.add_error(
                "Syntax Error",
                "Statement must start with 'if'."
            )

        # Find condition inside parentheses.
        condition = re.search(
            r"if\s*\((.*?)\)",
            code
        )

        if condition is None:
            self._errors.add_error(
                "Syntax Error",
                "Missing or invalid condition parentheses."
            )

        else:

            condition_text = (
                condition.group(1).strip()
            )

            if condition_text == "":
                self._errors.add_error(
                    "Syntax Error",
                    "IF condition cannot be empty."
                )

            # Detect assignment instead of comparison.
            if re.search(
                r"(?<![=!<>])=(?!=)",
                condition_text
            ):
                self._errors.add_error(
                    "Semantic Error",
                    "Use '==' for comparison, not '='."
                )

            # Example: if (5)
            if re.fullmatch(
                r"\d+",
                condition_text
            ):
                self._errors.add_error(
                    "Semantic Error",
                    "IF condition must evaluate to Boolean."
                )

        # Check brackets.
        if code.count("(") != code.count(")"):
            self._errors.add_error(
                "Syntax Error",
                "Unbalanced parentheses."
            )

        if code.count("{") != code.count("}"):
            self._errors.add_error(
                "Syntax Error",
                "Unbalanced braces."
            )

        return (
            tokens,
            self._errors.get_errors()
        )
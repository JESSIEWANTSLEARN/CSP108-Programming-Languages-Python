import re

from BaseAnalyzer import BaseAnalyzer


class SwitchAnalyzer(BaseAnalyzer):
    """
    Analyzes C# switch statements.

    Inheritance:
    SwitchAnalyzer inherits BaseAnalyzer.

    Polymorphism:
    analyze() is overridden.
    """

    def analyze(self):

        code = self.get_code().strip()

        tokens = self._lexer.tokenize(code)

        if not code.startswith("switch"):
            self._errors.add_error(
                "Syntax Error",
                "Statement must start with 'switch'."
            )

        # Check switch expression.
        expression = re.search(
            r"switch\s*\((.*?)\)",
            code
        )

        if expression is None:
            self._errors.add_error(
                "Syntax Error",
                "Switch requires parentheses."
            )

        else:

            value = (
                expression.group(1).strip()
            )

            if value == "":
                self._errors.add_error(
                    "Syntax Error",
                    "Switch expression cannot be empty."
                )

        # Check braces.
        if "{" not in code or "}" not in code:
            self._errors.add_error(
                "Syntax Error",
                "Switch body must use braces { }."
            )

        # Get case labels.
        cases = re.findall(
            r"case\s+([^:]+):",
            code
        )

        # Check duplicate cases.
        used_cases = []

        for case in cases:

            case = case.strip()

            if case in used_cases:

                self._errors.add_error(
                    "Semantic Error",
                    "Duplicate case value: "
                    + case
                )

            used_cases.append(case)

        # Check default.
        default_count = len(
            re.findall(
                r"default\s*:",
                code
            )
        )

        if default_count > 1:
            self._errors.add_error(
                "Semantic Error",
                "Only one default case is allowed."
            )

        if len(cases) == 0 and default_count == 0:
            self._errors.add_error(
                "Syntax Error",
                "Switch must contain a case or default."
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
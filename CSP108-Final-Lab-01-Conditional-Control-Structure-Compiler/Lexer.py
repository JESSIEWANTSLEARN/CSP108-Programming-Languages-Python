import re


class Lexer:
    """
    Converts C# source code into
    lexemes and corresponding tokens.
    """

    KEYWORDS = {
        "if": "IF_KEYWORD",
        "else": "ELSE_KEYWORD",
        "switch": "SWITCH_KEYWORD",
        "case": "CASE_KEYWORD",
        "default": "DEFAULT_KEYWORD",
        "break": "BREAK_KEYWORD",
        "true": "BOOLEAN_LITERAL",
        "false": "BOOLEAN_LITERAL"
    }

    def tokenize(self, code):

        pattern = (
            r'"[^"]*"|'
            r"'[^']'|"
            r'\d+(?:\.\d+)?|'
            r'==|!=|>=|<=|&&|\|\||'
            r'[><=+\-*/%!]|'
            r'[(){}:;,.]|'
            r'[A-Za-z_][A-Za-z0-9_]*|'
            r'\S'
        )

        lexemes = re.findall(pattern, code)

        tokens = []

        for lexeme in lexemes:

            if lexeme in self.KEYWORDS:
                token = self.KEYWORDS[lexeme]

            elif re.fullmatch(r'"[^"]*"', lexeme):
                token = "STRING_LITERAL"

            elif re.fullmatch(r"'[^']'", lexeme):
                token = "CHAR_LITERAL"

            elif re.fullmatch(
                r"\d+(?:\.\d+)?",
                lexeme
            ):
                token = "NUMBER_LITERAL"

            elif lexeme in {
                "==", "!=", ">=",
                "<=", ">", "<"
            }:
                token = "RELATIONAL_OPERATOR"

            elif lexeme in {
                "&&", "||", "!"
            }:
                token = "LOGICAL_OPERATOR"

            elif lexeme == "=":
                token = "ASSIGNMENT_OPERATOR"

            elif lexeme in {
                "+", "-", "*", "/", "%"
            }:
                token = "ARITHMETIC_OPERATOR"

            elif lexeme == "(":
                token = "LEFT_PARENTHESIS"

            elif lexeme == ")":
                token = "RIGHT_PARENTHESIS"

            elif lexeme == "{":
                token = "LEFT_BRACE"

            elif lexeme == "}":
                token = "RIGHT_BRACE"

            elif lexeme == ":":
                token = "COLON"

            elif lexeme == ";":
                token = "SEMICOLON"

            elif lexeme == ".":
                token = "MEMBER_ACCESS"

            elif re.fullmatch(
                r"[A-Za-z_][A-Za-z0-9_]*",
                lexeme
            ):
                token = "IDENTIFIER"

            else:
                token = "UNKNOWN"

            tokens.append(
                (lexeme, token)
            )

        return tokens
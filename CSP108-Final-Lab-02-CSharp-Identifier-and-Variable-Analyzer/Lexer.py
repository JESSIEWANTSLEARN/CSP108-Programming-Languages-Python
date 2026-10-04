import re


class Lexer:
    """
    Identifies lexemes and tokens
    from C# variable-related inputs.
    """

    DATA_TYPES = {
        "int",
        "double",
        "float",
        "decimal",
        "string",
        "char",
        "bool",
        "long",
        "short",
        "byte"
    }

    RESERVED_WORDS = {
        "if",
        "else",
        "switch",
        "case",
        "default",
        "while",
        "for",
        "class",
        "public",
        "private",
        "return",
        "true",
        "false"
    }

    def tokenize(self, code):

        pattern = (
            r'"[^"]*"|'
            r"'[^']'|"
            r'[+-]?\d+\.\d+[fFmM]?|'
            r'[+-]?\d+|'
            r'[A-Za-z_][A-Za-z0-9_]*|'
            r'=|;|,|\S'
        )

        lexemes = re.findall(
            pattern,
            code
        )

        tokens = []

        for lexeme in lexemes:

            if lexeme in self.DATA_TYPES:

                token = "DATA_TYPE"

            elif lexeme in {
                "true",
                "false"
            }:

                token = "BOOLEAN_LITERAL"

            elif lexeme in self.RESERVED_WORDS:

                token = "KEYWORD"

            elif re.fullmatch(
                r'"[^"]*"',
                lexeme
            ):

                token = "STRING_LITERAL"

            elif re.fullmatch(
                r"'[^']'",
                lexeme
            ):

                token = "CHAR_LITERAL"

            elif re.fullmatch(
                r"[+-]?\d+\.\d+[fF]",
                lexeme
            ):

                token = "FLOAT_LITERAL"

            elif re.fullmatch(
                r"[+-]?\d+\.\d+",
                lexeme
            ):

                token = "DOUBLE_LITERAL"

            elif re.fullmatch(
                r"[+-]?\d+",
                lexeme
            ):

                token = "INTEGER_LITERAL"

            elif lexeme == "=":

                token = (
                    "ASSIGNMENT_OPERATOR"
                )

            elif lexeme == ";":

                token = "SEMICOLON"

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
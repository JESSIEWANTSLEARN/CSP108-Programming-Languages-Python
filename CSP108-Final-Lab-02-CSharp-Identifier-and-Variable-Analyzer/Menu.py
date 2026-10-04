from IdentifierAnalyzer import IdentifierAnalyzer
from DataTypeAnalyzer import DataTypeAnalyzer
from DeclarationAnalyzer import DeclarationAnalyzer
from InitializationAnalyzer import InitializationAnalyzer


class Menu:
    """
    Displays the user menu
    and analysis result.
    """

    def show_tokens(
        self,
        tokens
    ):

        print(
            "\nLEXEMES AND TOKENS"
        )

        print("-" * 45)

        print(
            f"{'LEXEME':<20} TOKEN"
        )

        print("-" * 45)

        for lexeme, token in tokens:

            print(
                f"{lexeme:<20} {token}"
            )

    def show_result(
        self,
        analyzer
    ):
        """
        Polymorphism:
        different analyzer objects
        use the same analyze() call.
        """

        tokens, errors = (
            analyzer.analyze()
        )

        self.show_tokens(tokens)

        print("\nRESULT")

        print("-" * 45)

        if len(errors) == 0:

            print(
                "STATUS: VALID"
            )

            print(
                "No errors detected."
            )

        else:

            print(
                "STATUS: INVALID"
            )

            print("\nERRORS:")

            for number, error in enumerate(
                errors,
                start=1
            ):

                print(
                    str(number)
                    + ". "
                    + error
                )

    def start(self):

        while True:

            print(
                "\n================================"
            )

            print(
                "C# VARIABLE ANALYZER"
            )

            print(
                "================================"
            )

            print(
                "1. Name / Identifier"
            )

            print(
                "2. Data Type"
            )

            print(
                "3. Variable Declaration"
            )

            print(
                "4. Variable Initialization"
            )

            print(
                "5. Exit"
            )

            choice = input(
                "Enter choice: "
            )

            if choice == "1":

                text = input(
                    "Enter identifier: "
                )

                analyzer = (
                    IdentifierAnalyzer(text)
                )

                self.show_result(
                    analyzer
                )

            elif choice == "2":

                text = input(
                    "Enter data type: "
                )

                analyzer = (
                    DataTypeAnalyzer(text)
                )

                self.show_result(
                    analyzer
                )

            elif choice == "3":

                text = input(
                    "Enter declaration: "
                )

                analyzer = (
                    DeclarationAnalyzer(
                        text
                    )
                )

                self.show_result(
                    analyzer
                )

            elif choice == "4":

                text = input(
                    "Enter initialization: "
                )

                analyzer = (
                    InitializationAnalyzer(
                        text
                    )
                )

                self.show_result(
                    analyzer
                )

            elif choice == "5":

                print(
                    "Program terminated."
                )

                break

            else:

                print(
                    "Invalid menu choice."
                )
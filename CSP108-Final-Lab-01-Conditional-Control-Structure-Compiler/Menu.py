from IfAnalyzer import IfAnalyzer
from SwitchAnalyzer import SwitchAnalyzer


class Menu:
    """
    Controls user interaction.
    """

    def show_tokens(self, tokens):

        print("\nLEXEMES AND TOKENS")
        print("-" * 45)

        print(
            f"{'LEXEME':<20} TOKEN"
        )

        print("-" * 45)

        for lexeme, token in tokens:

            print(
                f"{lexeme:<20} {token}"
            )

    def show_result(self, analyzer):
        """
        Polymorphism happens here.

        analyzer can be:
        IfAnalyzer
        or
        SwitchAnalyzer

        Both use analyze().
        """

        tokens, errors = (
            analyzer.analyze()
        )

        self.show_tokens(tokens)

        print("\nRESULT")
        print("-" * 45)

        if len(errors) == 0:

            print("STATUS: VALID")

            print(
                "No syntax or semantic "
                "errors detected."
            )

        else:

            print("STATUS: INVALID")

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
                "\n=============================="
            )

            print(
                "C# CONDITIONAL ANALYZER"
            )

            print(
                "=============================="
            )

            print("1. IF Statement")
            print("2. SWITCH Statement")
            print("3. Exit")

            choice = input(
                "Enter choice: "
            )

            if choice == "1":

                code = input(
                    "\nEnter C# IF statement:\n"
                )

                analyzer = IfAnalyzer(code)

                self.show_result(
                    analyzer
                )

            elif choice == "2":

                code = input(
                    "\nEnter C# SWITCH statement:\n"
                )

                analyzer = SwitchAnalyzer(
                    code
                )

                self.show_result(
                    analyzer
                )

            elif choice == "3":

                print(
                    "Program terminated."
                )

                break

            else:

                print(
                    "Invalid menu choice."
                )
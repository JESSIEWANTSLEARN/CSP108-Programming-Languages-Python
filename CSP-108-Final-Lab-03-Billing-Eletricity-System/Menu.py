from Customer import Customer
from ElectricityBilling import ElectricityBilling


class Menu:
    """
    Handles user input
    and displays the bill.
    """

    def validate_name(self, name):
        """
        Checks whether the customer's
        name is valid.

        Valid:
        John
        John Palarao

        Invalid:
        empty input
        """

        if name.strip() == "":

            return False

        return True

    def validate_consumption(
        self,
        consumption
    ):
        """
        Checks whether electricity
        consumption is valid.

        Valid:
        0 or greater

        Invalid:
        Negative values
        Non-numeric values
        """

        try:

            value = float(
                consumption
            )

            if value < 0:

                return False

            return True

        except ValueError:

            return False

    def display_bill(
        self,
        customer,
        calculator
    ):
        """
        Displays complete billing
        information.
        """

        consumption = (
            customer.get_consumption()
        )

        base_bill, vat, total_bill = (
            calculator.calculate_bill(
                consumption
            )
        )

        print(
            "\n=================================="
        )

        print(
            "       ELECTRICITY BILL"
        )

        print(
            "=================================="
        )

        print(
            "Customer Name:",
            customer.get_name()
        )

        print(
            "Consumption:",
            f"{consumption:.2f}",
            "kWh"
        )

        print(
            "----------------------------------"
        )

        print(
            "Base Bill:",
            f"P{base_bill:.2f}"
        )

        print(
            "12% VAT:",
            f"P{vat:.2f}"
        )

        print(
            "----------------------------------"
        )

        print(
            "TOTAL BILL:",
            f"P{total_bill:.2f}"
        )

        print(
            "=================================="
        )

    def start(self):
        """
        Main program menu.
        """

        while True:

            print(
                "\n=================================="
            )

            print(
                " ELECTRICITY BILLING SYSTEM"
            )

            print(
                "=================================="
            )

            print(
                "1. Calculate Monthly Bill"
            )

            print(
                "2. Exit"
            )

            choice = input(
                "Enter choice: "
            )

            if choice == "1":

                name = input(
                    "\nEnter customer name: "
                )

                # Validate name
                if not self.validate_name(
                    name
                ):

                    print(
                        "\nINVALID INPUT:"
                    )

                    print(
                        "Customer name "
                        "cannot be empty."
                    )

                    continue

                consumption_input = input(
                    "Enter electricity "
                    "consumption in kWh: "
                )

                # Validate consumption
                if not self.validate_consumption(
                    consumption_input
                ):

                    print(
                        "\nINVALID INPUT:"
                    )

                    print(
                        "Consumption must be "
                        "a number that is "
                        "0 or greater."
                    )

                    continue

                consumption = float(
                    consumption_input
                )

                # Create customer object
                customer = Customer(
                    name,
                    consumption
                )

                # Polymorphic calculator object
                calculator = (
                    ElectricityBilling()
                )

                self.display_bill(
                    customer,
                    calculator
                )

            elif choice == "2":

                print(
                    "\nProgram terminated."
                )

                break

            else:

                print(
                    "\nINVALID INPUT:"
                )

                print(
                    "Please enter "
                    "1 or 2 only."
                )
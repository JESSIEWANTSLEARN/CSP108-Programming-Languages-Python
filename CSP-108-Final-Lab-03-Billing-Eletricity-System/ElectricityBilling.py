from BillingCalculator import BillingCalculator


class ElectricityBilling(BillingCalculator):
    """
    Performs electricity bill calculations.

    Inheritance:
    ElectricityBilling inherits
    BillingCalculator.

    Polymorphism:
    calculate_bill() overrides the
    abstract method from BillingCalculator.
    """

    VAT_RATE = 0.12

    def calculate_base_bill(self, consumption):
        """
        Calculates the bill before VAT.

        Rates:
        First 100 kWh  = P10 per kWh
        Next 100 kWh   = P12 per kWh
        Above 200 kWh  = P15 per kWh

        Parameter:
        consumption - customer's kWh usage
        """

        # First 100 kWh
        if consumption <= 100:

            base_bill = (
                consumption * 10
            )

        # 101 to 200 kWh
        elif consumption <= 200:

            first_100 = (
                100 * 10
            )

            remaining = (
                consumption - 100
            )

            next_100 = (
                remaining * 12
            )

            base_bill = (
                first_100
                + next_100
            )

        # Above 200 kWh
        else:

            first_100 = (
                100 * 10
            )

            next_100 = (
                100 * 12
            )

            remaining = (
                consumption - 200
            )

            above_200 = (
                remaining * 15
            )

            base_bill = (
                first_100
                + next_100
                + above_200
            )

        return base_bill

    def calculate_vat(self, base_bill):
        """
        Calculates 12% VAT.

        Parameter:
        base_bill - amount before VAT
        """

        vat = (
            base_bill
            * self.VAT_RATE
        )

        return vat

    def calculate_bill(self, consumption):
        """
        Calculates the complete bill.

        This method overrides the abstract
        calculate_bill() method.

        Parameter:
        consumption - customer's kWh usage
        """

        base_bill = (
            self.calculate_base_bill(
                consumption
            )
        )

        vat = (
            self.calculate_vat(
                base_bill
            )
        )

        total_bill = (
            base_bill
            + vat
        )

        return (
            base_bill,
            vat,
            total_bill
        )
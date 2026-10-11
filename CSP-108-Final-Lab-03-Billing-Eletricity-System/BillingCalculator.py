from abc import ABC, abstractmethod


class BillingCalculator(ABC):
    """
    Abstract parent class.

    Abstraction:
    calculate_bill() is an abstract method.

    Any billing calculator that inherits
    this class must create its own
    calculate_bill() method.
    """

    @abstractmethod
    def calculate_bill(self, consumption):
        """
        Abstract method with a parameter.

        consumption - number of kWh used
        """

        pass
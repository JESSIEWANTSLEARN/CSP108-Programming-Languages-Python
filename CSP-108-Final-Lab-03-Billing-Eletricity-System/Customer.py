class Customer:
    """
    Stores the customer's information.

    Encapsulation:
    The customer's name and consumption
    are stored in private attributes.
    """

    def __init__(self, name, consumption):
        self.__name = name
        self.__consumption = consumption

    def get_name(self):
        return self.__name

    def get_consumption(self):
        return self.__consumption
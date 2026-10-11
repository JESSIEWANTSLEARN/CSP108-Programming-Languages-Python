from Menu import Menu

class Program:
    """
    Main program class.

    The main method only creates
    and starts the menu.
    """

    @staticmethod
    def main():

        menu = Menu()
        menu.start()


if __name__ == "__main__":
    Program.main()
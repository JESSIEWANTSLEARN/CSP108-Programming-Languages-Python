class ErrorHandler:
    """
    Handles errors detected
    during analysis.
    """

    def __init__(self):

        # Encapsulation
        self.__errors = []

    def add_error(
        self,
        error_type,
        message
    ):

        self.__errors.append(
            f"{error_type}: {message}"
        )

    def get_errors(self):

        return self.__errors.copy()
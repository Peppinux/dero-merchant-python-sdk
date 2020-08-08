class APIError(Exception):
    """Exception that represents the error object returned by the API.

    Attributes:
        code: Integer of the error code returned by the API
        message: String of the error message returned by the API
    """

    def __init__(self, code: int, message: str):
        """Inits APIError with code and message
        
        Args:
            code: Integer of the error code returned by the API
            message: String of the error message returned by the API
        """
        self.code = code
        self.message = message

    def __str__(self):
        """Describes the exception.
        
        Returns:
            A string with the description of the error.
        """
        return f'API Error {self.code}: {self.message}'

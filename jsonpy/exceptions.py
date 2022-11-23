class JsonSchemaException(ValueError):
    """
    This exception is raised by validation function.
    Contains custom message as well as the actual error message
    """

    def __init__(self, message):
        self.message = message

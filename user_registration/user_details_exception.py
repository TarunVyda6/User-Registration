class InvalidCredentialsException(Exception):
    def __init__(self, message):
        self.message = message


class NoValueException(Exception):
    def __init__(self, message):
        self.message = message

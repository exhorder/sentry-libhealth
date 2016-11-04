from libtervis._compat import implements_to_string


@implements_to_string
class TervisException(Exception):

    def __init__(self, message=None):
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        return self.message


class ValidationError(TervisException):
    pass

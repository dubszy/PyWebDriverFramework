class ComponentException(Exception):
    """
    Raised when there is a general issue with a Component.
    """
    pass


class DriverEnvironmentException(Exception):
    """
    Raised when the DriverEnvironment encounters an issue.
    """
    pass


class SessionException(Exception):
    """
    Raised when the Session encounters an issue.
    """
    pass


class StoreException(Exception):
    """
    Raised when the Store encounters an issue.
    """
    pass


class TimeoutException(Exception):
    """
    Raised when Selector timed out waiting for a condition to be satisfied.
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Message: %s\n" % self.message

from .driver_env import DriverEnvironment
from .exceptions import SessionException
from .store import Store

class Session:
    """
    Creates, configures, stores, and maintains the environment and data for a
    single test.

    Makes use of:
        Store: for storing any data the tester deems necessary for the current
                test
        DriverEnvironment: for managing the connection to WebDriver

    The idea behind this class is to have an easy way to create a fresh
    environment for each test to avoid leaking data and resources from one test
    to another. Due to the design of this framework, and this class
    specifically, it would be considered an anti-pattern to use one Session for
    more than one test, although it is possible. Creating a new Session at the
    start of each test allows each test to be effectively free from side-effects
    and external influences. For example, by starting with a fresh browser
    instance each time a new test is run, we don't run the risk of the browser
    carrying its state over to another test, and thus potentially invalidating
    the results of latter tests.
    """

    def __init__(self, browser: str, host: str):
        self._store = Store()
        self._driver_env = DriverEnvironment(browser)
        self._host = host
        self.__closed = False

    def start(self):
        self._driver_env.go_to_url(self._host)

    def get_store(self):
        if self.__closed:
            raise SessionException("This Session has been closed")
        if self._store is None:
            raise SessionException("Store for this Session is None")
        return self._store

    def get_host(self):
        if self.__closed:
            raise SessionException("This Session has been closed")
        if self._host is "" or None:
            raise SessionException("Host for this Session is None or empty")
        return self._host

    def get_driver_env(self) -> DriverEnvironment:
        if self.__closed:
            raise SessionException("This Session has been closed")
        if self._driver_env is None:
            raise SessionException("Driver Environment for this Session is "
                                   "None")
        # noinspection PyProtectedMember
        # We may as well check this here before we try to access _driver_env
        if self._driver_env._closed:
            raise SessionException("Driver Environment for this Session is "
                                   "closed")
        return self._driver_env

    def close(self):
        self.__closed = True
        self._driver_env.close()

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver  # For type hinting

from .exceptions import DriverEnvironmentException


class DriverEnvironment:
    """
    Creates an abstraction layer between WebDriver and the rest of the
    framework. This is done to limit the scope of where WebDriver methods can be
    used so they don't leak into page objects or tests.
    """
    class _BrowserSwitch(str):
        """
        Get a new instance of a specific driver. (ChromeDriver, FirefoxDriver,
        etc).
        """
        def string_to_browser(self, browser_string):
            """
            Find the matching driver to create a new instance of based on a
            supplied string.

            :param browser_string: The string matching the name of the browser
            :return: The result of the method that returns a new instance of a
            driver
            """
            method = getattr(self, browser_string.lower(), lambda: "invalid")
            return method()

        # TODO: Support preferences, capabilities, and driver path when creating
        #  a new driver. This will likely deserve its own class at that point

        @staticmethod
        def android():
            """
            Get the Android WebDriver.

            :return: A new instance of the Android WebDriver
            """
            return webdriver.Android()

        # TODO: BlackBerry (and only BB) needs a device password. BB support
        #  will be added at a later date

        @staticmethod
        def chrome():
            """
            Get the Google Chrome WebDriver.

            :return: A new instance of the Chrome WebDriver
            """
            return webdriver.Chrome()

        @staticmethod
        def edge():
            """
            Get the Microsoft Edge WebDriver.

            :return: A new instance of the Edge WebDriver
            """
            return webdriver.Edge()

        @staticmethod
        def ff():
            """
            Get the Firefox WebDriver. Passes to the next method.
            """
            pass

        @staticmethod
        def firefox():
            """
            Get the Firefox WebDriver.

            :return: A new instance of the Firefox WebDriver
            """
            return webdriver.Firefox()

        @staticmethod
        def ie():
            """
            Get the Internet Explorer WebDriver. Passes to the next method.
            """
            pass

        @staticmethod
        def internet_explorer():
            """
            Get the Internet Explorer WebDriver. Passes to the next method.
            :return:
            """
            pass

        @staticmethod
        def internetexplorer():
            """
            Get the Internet Explorer WebDriver.

            :return: A new instance of the Internet Explorer WebDriver.
            """
            return webdriver.Ie()

        @staticmethod
        def opera():
            """
            Get the Opera WebDriver.

            :return: A new instance of the Opera WebDriver
            """
            return webdriver.Opera()

        @staticmethod
        def phantom():
            """
            Get the PhantomJS WebDriver. Passes to the next method.
            """
            pass

        @staticmethod
        def phantomjs():
            """
            Get the PhantomJS WebDriver.

            :return: A new instance of the PhantomJS WebDriver
            """
            return webdriver.PhantomJS()

        @staticmethod
        def safari():
            """
            Get the Safari WebDriver.

            :return: A new instance of the Safari WebDriver
            """
            return webdriver.Safari()

    def __init__(self, browser_string: str):
        self._browser_string = browser_string
        self._driver = None
        self._started = False
        self._closed = False

    def get_driver(self) -> WebDriver:
        """
        Get the current WebDriver. This method lazy-starts the driver. If the
        driver has already been started, it is simply returned.

        :return: The current WebDriver instance

        :exception DriverEnvironmentException: If this driver environment is
        closed; if the driver was started, but is currently 'None'; if the
        browser string used to initialize this class is 'None'
        """
        if self._closed:
            raise DriverEnvironmentException("The DriverEnvironment is closed")
        if self._started and self._driver is None:
            raise DriverEnvironmentException(
                "There is no driver for this session. Either the driver was "
                "not set, or the Session is closed")
        if self._browser_string is None:
            raise DriverEnvironmentException(
                "Browser string not set or is invalid for this session. Please"
                "set a valid browser string when constructing this class.")
        return self._get_driver()

    def refresh(self):
        """
        Refresh the current page.
        """
        self.get_driver().refresh()

    def back(self):
        """
        Navigate one setup backward in the browser history.
        """
        self.get_driver().back()

    def forward(self):
        """
        Navigate one step forward in the browser history.
        """
        self.get_driver().forward()

    def go_to_url(self, url: str):
        """
        Navigate the browser to a supplied URL. This should be used instead of
        WebDriver.get(url) because we can drop the attempted URL into the
        exception thrown if something goes wrong.

        :param url: URL to navigate to
        :exception WebDriverException: If the URL could not be navigated to
        """
        try:
            self.get_driver().get(url)
        except WebDriverException as e:
            message = [e.msg, "\nAttempted URL: ", url]
            raise WebDriverException("".join(message), e.screen, e.stacktrace)

    # Note that 'async' is a reserved word in Python 3.7+
    def execute_js(self, asynchronous: bool, js: str, args=None):
        """
        Execute arbitrary JavaScript in the current window or frame. Note that
        this method can potentially invalidate the results of tests because it
        injects JS directly into the current frame and runs it as if it were
        part of the frame. The caller of this method effectively has full
        control of the JS sandbox in the current frame. As such, usage of this
        method is strongly discouraged, and should be avoided in favor of other
        available solutions.

        :param asynchronous: Whether the JS should be executed asynchronously
        :param js: JavaScript to execute
        :param args: Arguments to pass into the JavaScript

        :return: What the script executed returned; equivalent to what the
        script would return if it were run on a page under normal conditions
        """
        return self.get_driver().execute_async_script(js, *args) \
            if asynchronous else self.get_driver().execute_script(js, args)

    def _get_driver(self):
        """
        Creates a new instance of a WebDriver. This method exists so that the
        driver can be lazily started.

        By creating a new instance, the driver service is automatically started.

        :return: New instance of the type of driver specified by browser_string
        """
        if not self._started:
            # Sanity check to make sure we're not abandoning an open stream
            if self._driver is not None and not self._closed:
                self._driver.quit()
            self._started = True
            self._driver = self._BrowserSwitch()\
                .string_to_browser(self._browser_string)
        return self._driver

    def close(self):
        self._closed = True
        self._driver.quit()

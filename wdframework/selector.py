from typing import List
import time

from .exceptions import TimeoutException
from .session import Session

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ExpectedCondition


class Selector(object):
    """
    Wraps a web element's selector (CSS, XPATH, etc) for the purpose of quickly
    creating, using, and discarding web element instances. Selectors can be
    created using any of the 'by' mechanisms.

    The benefit of this class is that, because web element instances are
    discarded after one use, it greatly reduces the amount of
    StaleElementReferenceExceptions that would be thrown by WebDriver due to DOM
    changes after creating an instance of a web element.
    """

    def __init__(self, session: Session, locator: str,
                 by: str = "css_selector"):
        self.__session = session
        self.__locator = locator
        self.__by = by.lower()

    @staticmethod
    def with_container(session: Session, container: str, css_locator: str):
        """
        Create a new Selector with a parent container.

        :param session: The current Session
        :param container: Parent container the new Selector will use as its
        frame-of-reference
        :param css_locator: CSS locator for the new Selector

        :return: A new instance of a Selector inside of a parent container
        """
        locator = [container, css_locator]
        return Selector(session, "".join(locator))

    def get_locator(self):
        """
        Get the locator for this Selector

        :return: Locator string
        """
        return self.__locator

    def get_by(self):
        """
        Get the method by which WebElements will be located using this Selector

        :return: The 'by' type (css, xpath, etc)
        """
        return self.__by

    def get_session(self):
        """
        Get the Session this Selector is part of

        :return: The current testing Session
        """
        return self.__session

    def __get_find_element_method(self, multiple: bool):
        """
        Private method for finding the proper method to call in WebDriver to
        locate an element based on a selector. Do not use this method directly,
        instead use get() or get_multiple()

        :param multiple: Whether we should look for multiple elements

        :return: The element(s) found, if any

        :exception NoSuchElementException: If no elements could be found
        """
        method_name = ["find_elements_by_" if multiple else "find_element_by_",
                       self.__by]
        find_element_method = getattr(
            self.__session.get_driver_env().get_driver(),
            "".join(method_name),
            lambda: "INVALID_BY")
        return find_element_method(self.__locator)

    def get(self) -> WebElement:
        """
        Attempt to get a WebElement from the page

        :return: The WebElement found if it exists
        """
        return self.__get_find_element_method(False)

    def get_multiple(self):
        """
        Attempt to get multiple WebElements from the page

        :return: The WebElements found, if they exist
        """
        return self.__get_find_element_method(True)

    # Web Element Information #

    def is_present(self) -> bool:
        """
        Whether the WebElement located by this Selector is present.

        :return: True if the element is present, False otherwise
        """
        try:
            self.get()
            return True
        except NoSuchElementException:
            return False

    def get_css_classes(self) -> List[str]:
        """
        Get the CSS classes present on the WebElement located by this Selector.

        :return: A list of CSS classes present on the WebElement
        """
        return self.get().get_attribute("class").split(" ")

    def is_displayed(self) -> bool:
        """
        Whether the WebElement located by this Selector is displayed.

        :return: True if the element is displayed, False otherwise
        """
        return self.get().is_displayed()

    def is_enabled(self) -> bool:
        """
        Whether the WebElement located by this Selector is enabled.

        :return: True if the element is enabled, False otherwise
        """
        return self.get().is_enabled()

    def is_selected(self) -> bool:
        """
        Whether the WebElement located by this Selector is selected.

        :return: True if the element is selected, False otherwise
        """
        return self.get().is_selected()

    def get_attribute(self, name: str) -> str:
        """
        Get an attribute from the WebElement located by this Selector.

        :param name: The name of the attribute

        :return: The value of the attribute
        """
        return self.get().get_attribute(name)

    def get_css_value(self, property_name: str) -> str:
        """
        Get a CSS value from the WebElement located by this Selector.

        :param property_name: The name of the CSS property

        :return: The value of the CSS property
        """
        return self.get().value_of_css_property(property_name)

    def get_tag_name(self) -> str:
        """
        Get the name of the tag for the WebElement located by this Selector.

        :return: The tag name
        """
        return self.get().tag_name

    def get_text(self) -> str:
        """
        Get the visible text of the WebElement located by this Selector.

        :return: The visible text
        """
        return self.get().text

    def get_location(self):
        """
        Get the location (in the frame) of the WebElement located by this
        Selector.

        :return: The origin location as a coordinate
        """
        return self.get().location

    def get_size(self):
        """
        Get the dimensions (in the frame) of the WebElement located by this
        Selector.

        :return: The dimensions of the element
        """
        return self.get().size

    def get_rect(self):
        """
        Get the rectangle (size and dimensions in the frame) of the WebElement
        located by this Selector.

        :return: The rectangle of the element
        """
        return self.get_rect()

    # Web Element Actions #

    def clear(self):
        """
        Clear the WebElement located by this Selector of its current value.

        :return: This instance
        """
        self.get().clear()
        return self

    def click(self):
        """
        Click the WebElement located by this Selector.

        :return: This instance
        """
        self.get().click()
        return self

    def send_keys(self, value):
        """
        Send keys (type into) the WebElement located by this Selector.

        :param value: The value to type into the element

        :return: This instance
        """
        self.get().send_keys(value)
        return self

    def submit(self):
        """
        Submit the WebElement located by this Selector.

        :return: This instance
        """
        self.get().submit()
        return self

    # Waiting #

    def wait_until(self, condition: ExpectedCondition, test=None):
        """
        Wait for the WebElement identified by this Selector to match an
        expected condition. WebDriver has expected conditions are defined in
        `selenium.webdriver.support.expected_conditions`, but custom expected
        conditions can also be used.

        This method should only be used with expected conditions that match
        web elements (such as `visibility_of` or `element_to_be_clickable`).
        This is because this method tests against this Selector.

        This method calls the 'condition' function supplied with the single
        argument 'test' (expected conditions should only take a single object
        argument). 'test' should be an object that matches what 'condition'
        expects to receive as its single argument when it's executed.

        If testing for a condition that requires matching of any sort, 'test'
        should be the value to match. If testing for a condition that does not
        require matching, 'test' must be left as the default. If 'test' is
        'None', 'condition' will be executed like so: ``condition(self.get())``
        if 'test' is not 'None', 'condition' will be executed like so:
        ``condition(self.get(), test)``

        :param condition: Expected condition function to call
        :param test: Matcher to supply to the expected condition if performing
            matching

        :return: This instance

        :raises TimeoutException: If a timeout occurred waiting for the first
            found element to match the expected condition
        """
        now = time.time()
        delay = now + 10

        while now < delay:
            if test is None:  # If 'None', just pass our WebElement as the
                                # object
                result = condition(self.get())
            else:  # Otherwise, we're matching something, so we need to pass the
                    # matcher as well
                result = condition(self.get(), test)

            if result:
                return self
            time.sleep(0.2)

        raise TimeoutException("Timed out after %d seconds waiting for the "
                               "first found element to match the expected"
                               "condition" % delay)



# This class is for testing the framework itself, it should not be used as a
# guideline for how to use this framework.

import os
import sys

from selenium.webdriver.support import expected_conditions as ExpectedCondition


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import wdframework


def test_selector_find_element():
    session = wdframework.Session("chrome", "http://www.google.com")
    session.start()
    search_input = wdframework.selector.Selector(session, "input[type='text']")
    search_input.wait_until(ExpectedCondition.visibility_of)
    assert search_input.is_present()
    session.close()


if __name__ == '__main__':
    test_selector_find_element()

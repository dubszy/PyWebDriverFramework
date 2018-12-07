# This class is for testing the framework itself, it should not be used as a
# guideline for how to use this framework.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import wdframework


def test_go_to_url():
    driver_env = wdframework.DriverEnvironment("phantomjs")
    driver_env.go_to_url("http://www.google.com")
    assert "Google" in driver_env.get_driver().title

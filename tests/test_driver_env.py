# This class is for testing the framework itself, it should not be used as a
# guideline for how to use this framework.

from .context import wdframework


def test_go_to_url():
    driver_env = wdframework.DriverEnvironment("phantomjs")
    driver_env.go_to_url("http://www.google.com")
    assert "Google" in driver_env.get_driver().title

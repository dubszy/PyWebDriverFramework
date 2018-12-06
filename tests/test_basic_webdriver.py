# For now, just assert that the WebDriver package is installed
from selenium import webdriver


def test_webdriver_version():
    assert "3.6.0" in webdriver.__version__

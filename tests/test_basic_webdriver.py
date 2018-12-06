# For now, just assert that the WebDriver package is installed
from selenium import webdriver

assert "3.6.0" in webdriver.__version__

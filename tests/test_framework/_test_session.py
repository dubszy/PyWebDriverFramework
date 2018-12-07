# This class is for testing the framework itself, it should not be used as a
# guideline for how to use this framework.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import wdframework


def test_session_go_to_url():
    session = wdframework.Session("chrome", "http://www.google.com")
    session.start()
    assert "Google" in session.get_driver_env().get_driver().title
    session.close()


if __name__ == '__main__':
    test_session_go_to_url()

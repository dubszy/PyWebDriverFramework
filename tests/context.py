# For tests to be able to locate the wdframework package.
# To make use of this file in tests, simply write:
# from .context import wdframework
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import wdframework

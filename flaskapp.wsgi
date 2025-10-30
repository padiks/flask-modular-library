# Import necessary modules to interact with the system
import sys  # Provides access to system-specific parameters and functions
import os   # Provides functions to interact with the operating system

# Add the directory of this WSGI file to the Python path
# sys.path is a list of directories that the Python interpreter searches for modules.
# By inserting the directory of this file at the start of the path, we ensure that Python
# will look for modules in this directory first.
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application object for Apache/mod_wsgi.
# 'application' is the Flask app object that mod_wsgi expects to be callable.
# Apache mod_wsgi requires the Flask app to be exposed as 'application' for WSGI to work correctly.
from app import application

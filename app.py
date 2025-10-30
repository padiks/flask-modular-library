# Importing the Flask class from the Flask module
from flask import Flask

# Importing the create_app function from the common package
# This function is used to initialize and configure the Flask application
from apps import create_app

# Create an instance of the Flask application by calling the create_app function.
# The create_app function is typically a factory function that sets up the app 
# and returns the Flask app object.
application = create_app()

# If this script is being run directly (not imported), run the app with debugging enabled.
# This allows you to easily test and debug your app locally.
if __name__ == "__main__":
    application.run(debug=True)

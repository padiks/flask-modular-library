import os
from flask import Blueprint
from apps.utils.sections import render_section  

# apps/routes/books.py 
# Import utility function to render sections dynamically
# 'os' module is used for interacting with the operating system, such as handling file and directory paths.
# 'Blueprint' is used to organize routes and views into modular components within the Flask app.
# 'render_section' is a custom function used to render a section's content, passed with folder and optional subpath.

# Create a Blueprint instance for the 'books' section
bp = Blueprint('books', __name__)  # Blueprint 'books' to organize routes for the book section

# Define the root directory of the project, used to access files from the project folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))  # Get the absolute path to the project root
FOLDER_DIR = os.path.join(PROJECT_ROOT, 'books')  # Construct the path to the 'books' directory

# Define the route for the main books page
@bp.route('/', strict_slashes=False)
def index():
    """
    Render the main books section.
    This route serves the index page for the books section.
    """
    return render_section('books', FOLDER_DIR)  # Render the books section using the render_section function

# Define a dynamic route to handle subpaths (e.g., 'books/chapter-1')
@bp.route('/<path:subpath>/', strict_slashes=False)
def dynamic(subpath):
    """
    Render a specific subpath within the books section.
    This route allows for rendering content based on dynamic subpaths.
    """
    return render_section('books', FOLDER_DIR, subpath)  # Render the content based on the dynamic subpath

from flask import Blueprint, render_template

# apps/routes/home.py
# 'Blueprint' is used to organize routes and views into modular components within the Flask app.
# 'render_template' is a function used to render HTML templates, passing variables to the template.

# Create a Blueprint instance for the 'home' section
bp = Blueprint('home', __name__)  # Blueprint 'home' to organize routes for this section

# Define a route for the Home page
@bp.route('/')
def index():
    """
    Render the Home page with the standard base layout.
    
    The page includes a `page_title` variable to be used in the template.
    The template `home.html` is rendered with this title.
    """
    page_title = "ライトノベル図書館"  # Set the homepage title
    
    # Render the 'home.html' template and pass the page_title variable to it
    return render_template('home.html', page_title=page_title)

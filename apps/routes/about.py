from flask import Blueprint, render_template

# apps/routes/home.py
# 'Blueprint' is used to organize routes and views into modular components within the Flask app.
# 'render_template' is a function used to render HTML templates, passing variables to the template.

# Create a Blueprint instance for the 'about' section
bp = Blueprint('about', __name__)

# Define a route for the About page
@bp.route('/')
def index():
    """
    Render the About page with the standard base layout.
    
    The page includes a `page_title` variable to be used in the template.
    The template `about.html` is rendered with this title.
    """
    page_title = "About Page"
    return render_template('about.html', page_title=page_title)

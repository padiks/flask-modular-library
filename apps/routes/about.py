from flask import Blueprint, render_template

bp = Blueprint('about', __name__)

@bp.route('/')
def index():
    """Render the About page with the standard base layout."""
    page_title = "About Page"
    return render_template('about.html', page_title=page_title)

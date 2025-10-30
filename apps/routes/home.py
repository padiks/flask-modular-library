from flask import Blueprint, render_template

# Use same variable name style as books
bp = Blueprint('home', __name__)

# Root route
@bp.route('/')
def home():   # function name = home
    """Render the homepage."""
    return render_template('home.html')

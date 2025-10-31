import os
from flask import Blueprint
from apps.utils.sections import render_section

bp = Blueprint('books', __name__)

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
FOLDER_DIR = os.path.join(PROJECT_ROOT, 'books')

@bp.route('/', strict_slashes=False)
def index():
    return render_section('books', FOLDER_DIR)

@bp.route('/<path:subpath>/', strict_slashes=False)
def dynamic(subpath):
    return render_section('books', FOLDER_DIR, subpath)

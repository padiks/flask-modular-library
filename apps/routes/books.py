import os
from flask import Blueprint, render_template, abort
from markdown import markdown

bp = Blueprint('books', __name__)

# --- Path setup -------------------------------------------------
# This resolves to /home/user/Public/web/flaskfps
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
# This resolves to /home/user/Public/web/flaskfps/books
BOOKS_DIR = os.path.join(PROJECT_ROOT, 'books')

# --- Debug info -------------------------------------------------
print("PROJECT_ROOT:", PROJECT_ROOT)
print("BOOKS_DIR:", BOOKS_DIR)
print("BOOKS_DIR exists?", os.path.exists(BOOKS_DIR))

# --- Helper: Markdown parser ------------------------------------
def parse_markdown(file_path):
    """Read a markdown file and convert it to HTML."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return markdown(text)

# --- Routes ------------------------------------------------------
@bp.route('/', strict_slashes=False)
def books_index():
    """List all available books."""
    print("BOOKS_DIR:", BOOKS_DIR)
    if not os.path.exists(BOOKS_DIR):
        print("BOOKS_DIR does not exist:", BOOKS_DIR)
        abort(404)

    # List all book directories
    books = [
        d for d in os.listdir(BOOKS_DIR)
        if os.path.isdir(os.path.join(BOOKS_DIR, d))
    ]
    print("Books found:", books)

    return render_template('books/index.html', books=books, content=None)


@bp.route('/<book_name>/', strict_slashes=False)
def book_index(book_name):
    """Display the README.md for a specific book."""
    book_path = os.path.join(BOOKS_DIR, book_name)
    if not os.path.exists(book_path):
        abort(404)

    readme_path = os.path.join(book_path, 'README.md')
    content = parse_markdown(readme_path)
    if content is None:
        content = "<p>No README.md found for this book.</p>"

    return render_template('books/index.html', books=None, content=content)


@bp.route('/<book_name>/<volume>/', strict_slashes=False)
def volume_index(book_name, volume):
    """Display README.md inside a specific volume."""
    volume_path = os.path.join(BOOKS_DIR, book_name, volume)
    readme_path = os.path.join(volume_path, 'README.md')
    content = parse_markdown(readme_path)
    if content is None:
        abort(404)

    return render_template('books/index.html', books=None, content=content)


@bp.route('/<book_name>/<volume>/<chapter>/', strict_slashes=False)
def chapter_page(book_name, volume, chapter):
    """Display a specific chapter markdown."""
    chapter_path = os.path.join(BOOKS_DIR, book_name, volume, f'{chapter}.md')
    content = parse_markdown(chapter_path)
    if content is None:
        abort(404)

    return render_template('books/index.html', books=None, content=content)

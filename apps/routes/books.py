import os
from flask import Blueprint, render_template, abort
from markdown import markdown

bp = Blueprint('books', __name__)

# --- Path setup -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
BOOKS_DIR = os.path.join(PROJECT_ROOT, 'books')

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

# --- Helper: Pretty name formatter ------------------------------
def pretty_name(name):
    """Convert folder/file name like 'lorem-ipsum' to 'Lorem ipsum'."""
    s = name.replace('_', ' ').replace('-', ' ').lower()
    return s[:1].upper() + s[1:]

# --- Helper: Breadcrumb builder --------------------------------
def build_breadcrumb(subpath):
    """
    Convert a subpath like 'lorem-ipsum/volume-1/chapter-1' into
    a list of tuples: (name, url) for breadcrumb.
    """
    parts = subpath.strip('/').split('/')
    breadcrumb = [('Books', '/books/')]
    accumulated_path = ''
    for part in parts:
        accumulated_path = f"{accumulated_path}/{part}".lstrip('/')
        breadcrumb.append((pretty_name(part), f"/books/{accumulated_path}/"))
    return breadcrumb

# --- Recursive route handler ------------------------------------
@bp.route('/<path:subpath>/', strict_slashes=False)
def render_path(subpath):
    """
    Handles any nested folder or markdown file inside books/
    - If folder: check for README.md, list subfolders and .md files
    - If .md file: render it
    """
    full_path = os.path.join(BOOKS_DIR, subpath)

    # 1️⃣ Folder
    if os.path.isdir(full_path):
        subfolders = [d for d in os.listdir(full_path)
                      if os.path.isdir(os.path.join(full_path, d))]
        md_files = [f for f in os.listdir(full_path)
                    if f.endswith('.md') and f.lower() != 'readme.md']

        readme_path = os.path.join(full_path, 'README.md')
        content = parse_markdown(readme_path)

        if not subfolders and not md_files and content is None:
            content = None  # Nothing to show

        links = []
        for d in sorted(subfolders):
            links.append({
                'name': pretty_name(d),
                'url': f"/books/{subpath}/{d}/"
            })
        for f in sorted(md_files):
            name = os.path.splitext(f)[0]
            links.append({
                'name': pretty_name(name),
                'url': f"/books/{subpath}/{name}/"
            })

        breadcrumb = build_breadcrumb(subpath)
        return render_template('books/index.html',
                               content=content,
                               links=links,
                               breadcrumb=breadcrumb)

    # 2️⃣ Markdown file
    md_path = full_path if full_path.endswith('.md') else full_path + '.md'
    if os.path.exists(md_path):
        content = parse_markdown(md_path)
        breadcrumb = build_breadcrumb(subpath)
        return render_template('books/index.html',
                               content=content,
                               links=None,
                               breadcrumb=breadcrumb)

    # 3️⃣ Not found
    abort(404)


# --- Root books index ------------------------------------------
@bp.route('/', strict_slashes=False)
def books_index():
    if not os.path.exists(BOOKS_DIR):
        abort(404)

    books = [d for d in os.listdir(BOOKS_DIR)
             if os.path.isdir(os.path.join(BOOKS_DIR, d))]
    links = [{'name': pretty_name(b), 'url': f'/books/{b}/'} for b in sorted(books)]
    breadcrumb = [('Books', '/books/')]

    return render_template('books/index.html',
                           content=None,
                           links=links,
                           breadcrumb=breadcrumb)

import os
from flask import Blueprint, render_template, abort, current_app
from ..utils.markdown import parse_markdown

# apps/routes/markdown_render.py
# 'os' module is used to interact with the operating system, such as file and directory operations.
# 'Blueprint' is used to organize routes and views into modular components within the Flask app.
# 'render_template' is a function used to render HTML templates, passing variables to the template.
# 'abort' is used to abort a request and return an HTTP error code (e.g., 404).
# 'current_app' provides access to the Flask app instance for the current request context.
# 'parse_markdown' is a custom function from the 'utils/markdown.py' file used to parse the markdown files.

bp = Blueprint('md', __name__)  # Create a Blueprint instance for handling markdown rendering

@bp.route('/<path:md_path>/')
def render_md(md_path):
    """
    Render any markdown file dynamically.
    
    Example of `md_path`: 'books/lorem-ipsum/chapter-1'.
    This function constructs the full path to the markdown file, checks if it exists, 
    and then renders the corresponding HTML page with the parsed content.
    """
    base_dir = os.path.dirname(os.path.dirname(current_app.root_path))  # Get the base directory of the app
    full_path = os.path.join(base_dir, md_path + '.md')  # Construct the full path to the markdown file

    # If the markdown file does not exist, abort the request with a 404 error
    if not os.path.exists(full_path):
        abort(404)

    content = parse_markdown(full_path)  # Parse the markdown file content

    # Extract section name from the md_path (e.g., 'books', 'tutorials')
    section_name = md_path.split('/')[0]
    
    # Set the page title based on the markdown file path
    page_title = md_path.split('/')[-1].replace('-', ' ').title()

    # Render the HTML template corresponding to the section (e.g., 'books/index.html')
    return render_template(
        f'{section_name}/index.html',  # Template name based on the section
        content=content,  # Parsed markdown content to display in the template
        links=None,  # Optional links, if any
        breadcrumb=None,  # Optional breadcrumb, if any
        page_title=page_title  # Page title dynamically set based on the markdown file name
    )

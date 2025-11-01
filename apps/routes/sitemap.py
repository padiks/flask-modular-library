import os
from flask import Blueprint, render_template, current_app
from ..utils.sections import render_section, pretty_name

bp = Blueprint('sitemap', __name__)

@bp.route('/')
def index():
    """
    Generate a modular sitemap for all top-level sections (books, tutorials, etc.).
    Uses utils/sections.py to find subfolders and Markdown files dynamically.
    """

    # Define your top-level sections here (or configure via config.py)
    sections = {
        'books': current_app.config.get(
            'BOOKS_DIR',
            os.path.join(current_app.root_path, '..', 'books')
        ),
        'tutorials': current_app.config.get(
            'TUTORIALS_DIR',
            os.path.join(current_app.root_path, '..', 'tutorials')
        ),
        # add more sections if needed
    }

    sitemap_data = {}

    for section_name, folder_dir in sections.items():
        if not os.path.exists(folder_dir):
            continue

        items = []

        # list directories and markdown files
        for entry in sorted(os.listdir(folder_dir)):
            full_path = os.path.join(folder_dir, entry)
            if os.path.isdir(full_path):
                items.append({
                    'title': pretty_name(entry),
                    'path': f"{section_name}/{entry}"
                })
            elif entry.endswith('.md') and entry.lower() != 'readme.md':
                items.append({
                    'title': pretty_name(os.path.splitext(entry)[0]),
                    'path': f"{section_name}/{os.path.splitext(entry)[0]}"
                })

        if items:
            sitemap_data[pretty_name(section_name)] = items

    # pass as 'sections' to match template variable
    return render_template('sitemap.html', sections=sitemap_data, page_title="Sitemap")

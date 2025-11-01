import os
import re
from flask import Blueprint, render_template, request, current_app

bp = Blueprint('search', __name__)

# Define the sections here manually, same as in the sitemap
def get_sections():
    """Manually return all top-level sections."""
    sections = {
        'books': current_app.config.get(
            'BOOKS_DIR',
            os.path.join(current_app.root_path, '..', 'books')
        ),
        'tutorials': current_app.config.get(
            'TUTORIALS_DIR',
            os.path.join(current_app.root_path, '..', 'tutorials')
        ),
    }
    return sections

def search_in_section(query, section_name, section_dir):
    """Search within a specific section's directory."""
    results = []
    if query:
        for root, dirs, files in os.walk(section_dir):
            for file in files:
                if file.endswith('.md'):  # Only search in markdown files
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except Exception:
                        continue
                    
                    match = re.search(re.escape(query), content, re.IGNORECASE)
                    if match:
                        pos = match.start()
                        snippet_start = max(0, pos - 30)
                        snippet = content[snippet_start: pos + 150]
                        snippet = re.sub(r'[#>*_`~\-]+', '', snippet)  # Clean up the snippet
                        snippet = re.sub(r'<[^>]*>', '', snippet).strip()  # Remove HTML tags

                        # Get relative path for section and file, remove dash and backslashes
                        rel_path = os.path.relpath(full_path, section_dir)
                        url_path = rel_path.replace('\\', '/').replace('.md', '')  # Ensure forward slashes

                        results.append({
                            'section': section_name,
                            'path': url_path,
                            'match_snippet': snippet + '...'
                        })
    return results

def search_in_all_sections(query):
    """Search across all sections."""
    results = []
    sections = get_sections()

    for section_name, section_dir in sections.items():
        results.extend(search_in_section(query, section_name, section_dir))

    return results

# Use the function name "index" here and route it to the home page
@bp.route('/', endpoint='index')  # Explicitly set endpoint as "index"
def index():
    """Search page, replacing the previous search function with index."""
    query = request.args.get('q', '').strip()

    results = []
    if query:
        results = search_in_all_sections(query)

    return render_template('search.html', page_title="Search results", query=query, results=results)

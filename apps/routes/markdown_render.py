import os
from flask import Blueprint, render_template, abort, current_app
from ..utils.markdown import parse_markdown

bp = Blueprint('md', __name__)

@bp.route('/<path:md_path>/')
def render_md(md_path):
    """
    Render any markdown file dynamically.
    md_path example: 'books/lorem-ipsum/chapter-1'
    """
    base_dir = os.path.dirname(os.path.dirname(current_app.root_path))
    full_path = os.path.join(base_dir, md_path + '.md')

    if not os.path.exists(full_path):
        abort(404)

    content = parse_markdown(full_path)
    section_name = md_path.split('/')[0]  # 'books', 'tutorials', etc.
    page_title = md_path.split('/')[-1].replace('-', ' ').title()

    return render_template(
        f'{section_name}/index.html',
        content=content,
        links=None,
        breadcrumb=None,
        page_title=page_title
    )

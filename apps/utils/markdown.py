import os
from markdown import markdown

def parse_markdown(file_path):
    """Read a markdown file and convert it to HTML."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return markdown(text)

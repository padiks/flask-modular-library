# apps/utils/markdown.py

import os
from markdown import markdown  # Import the markdown module to convert markdown text to HTML

def parse_markdown(file_path):
    """Read a markdown file and convert it to HTML."""
    # Check if the markdown file exists at the specified path
    if not os.path.exists(file_path):
        return None  # Return None if the file does not exist

    # Open and read the markdown file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()  # Read the contents of the markdown file
    
    # Convert the markdown text to HTML and return it
    return markdown(text)

# apps/utils/breadcrumb.py

def pretty_name(name):
    """
    Convert a string (e.g., 'book_title') into a more readable format (e.g., 'Book title').
    
    This function replaces underscores and hyphens with spaces, converts the string to lowercase,
    and then capitalizes the first letter of the string.
    """
    s = name.replace('_', ' ').replace('-', ' ').lower()  # Replace underscores and hyphens with spaces, then convert to lowercase
    return s[:1].upper() + s[1:]  # Capitalize the first letter and return the modified string

def build_breadcrumb(section_name, subpath=''):
    """
    Build a breadcrumb trail for a section with an optional subpath.
    
    The breadcrumb trail shows the hierarchy of the section and subpath, making it easy to navigate.
    Each breadcrumb is a tuple containing the human-readable name and the corresponding URL path.
    
    Example:
    For `section_name='books'` and `subpath='chapter-1/part-a'`, it will return a breadcrumb like:
    [("Books", "/books/"), ("Chapter 1", "/books/chapter-1/"), ("Part A", "/books/chapter-1/part-a/")]
    """
    # Split the subpath into parts if any; else use an empty list
    parts = subpath.strip('/').split('/') if subpath else []
    
    # Start with the breadcrumb for the section (e.g., "Books")
    breadcrumb = [(pretty_name(section_name), f'/{section_name}/')]
    
    accumulated_path = ''  # Initialize an empty string to build the path dynamically
    # Loop through each part of the subpath to build breadcrumb links
    for part in parts:
        accumulated_path = f"{accumulated_path}/{part}".lstrip('/')  # Accumulate the path for each part
        breadcrumb.append((pretty_name(part), f"/{section_name}/{accumulated_path}/"))  # Add each part to the breadcrumb
    
    return breadcrumb  # Return the final breadcrumb list

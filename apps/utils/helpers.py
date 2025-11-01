# apps/utils/helpers.py

def pretty_name(name):
    """Convert folder/file name like 'lorem-ipsum' to 'Lorem ipsum'."""
    # Replaces underscores and hyphens with spaces, then converts the string to lowercase.
    s = name.replace('_', ' ').replace('-', ' ').lower()
    
    # Capitalizes the first letter of the string and returns the modified version.
    return s[:1].upper() + s[1:]

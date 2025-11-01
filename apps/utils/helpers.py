def pretty_name(name):
    """Convert folder/file name like 'lorem-ipsum' to 'Lorem ipsum'."""
    s = name.replace('_', ' ').replace('-', ' ').lower()
    return s[:1].upper() + s[1:]

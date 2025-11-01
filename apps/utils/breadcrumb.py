def pretty_name(name):
    s = name.replace('_', ' ').replace('-', ' ').lower()
    return s[:1].upper() + s[1:]

def build_breadcrumb(section_name, subpath=''):
    parts = subpath.strip('/').split('/') if subpath else []
    breadcrumb = [(pretty_name(section_name), f'/{section_name}/')]
    accumulated_path = ''
    for part in parts:
        accumulated_path = f"{accumulated_path}/{part}".lstrip('/')
        breadcrumb.append((pretty_name(part), f"/{section_name}/{accumulated_path}/"))
    return breadcrumb

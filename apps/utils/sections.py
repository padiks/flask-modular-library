import os
from flask import render_template, abort
from markdown import markdown
from .breadcrumb import build_breadcrumb, pretty_name

def parse_markdown(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return markdown(text)

def render_section(section_name, folder_dir, subpath=''):
    full_path = os.path.join(folder_dir, subpath)

    if os.path.isdir(full_path):
        subfolders = [d for d in os.listdir(full_path)
                      if os.path.isdir(os.path.join(full_path, d))]
        md_files = [f for f in os.listdir(full_path)
                    if f.endswith('.md') and f.lower() != 'readme.md']

        readme_path = os.path.join(full_path, 'README.md')
        content = parse_markdown(readme_path) if os.path.exists(readme_path) else None

        links = []
        for d in sorted(subfolders):
            links.append({'name': pretty_name(d),
                          'url': f"/{section_name}/{subpath}/{d}/".replace('//', '/')})
        for f in sorted(md_files):
            name = os.path.splitext(f)[0]
            links.append({'name': pretty_name(name),
                          'url': f"/{section_name}/{subpath}/{name}/".replace('//', '/')})

        breadcrumb = build_breadcrumb(section_name, subpath)
        page_title = pretty_name(subpath.split('/')[-1]) if subpath else pretty_name(section_name)

        return render_template(
            f'{section_name}/index.html',
            content=content,
            links=links,
            breadcrumb=breadcrumb,
            page_title=page_title
        )

    md_path = full_path if full_path.endswith('.md') else full_path + '.md'
    if os.path.exists(md_path):
        content = parse_markdown(md_path)
        breadcrumb = build_breadcrumb(section_name, subpath)
        page_title = pretty_name(os.path.splitext(subpath.split('/')[-1])[0])

        return render_template(
            f'{section_name}/index.html',
            content=content,
            links=None,
            breadcrumb=breadcrumb,
            page_title=page_title
        )

    abort(404)

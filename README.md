# Building a Modular Flask Library App with Dynamic Markdown Rendering

**"A modular Flask web application for dynamically rendering books from Markdown, allowing easy navigation through volumes and chapters."**

### Project Structure

```
flibrary/                      # Cross-platform Flask project (Windows and Debian, runs on Apache, Waitress, or console)
├── app.py                     # Entry point for production (Apache/Waitress); defines the `application` object
├── config.py                  # Configuration file for development and production; stores centralized settings
├── apps/                      # Core application modules (shared code, routing, etc.)
│   ├── __init__.py            # Initializes the Flask app, registers blueprints, and sets the global 404 handler
│   ├── routes/                # Application route definitions
│   │   ├── __init__.py        # Imports all route modules (home, books, etc.)
│   │   ├── home.py            # Home page routes
│   │   ├── about.py           # About page routes
│   │   ├── books.py           # Books, volumes, and chapters routes
│   │   ├── auth.py            # Authentication routes (login/logout)
│   │   ├── sitemap.py         # Modular sitemap blueprint, dynamic sections, works with markdown links
│   │   └── markdown_render.py # Markdown rendering blueprint, dynamic rendering for any md file
│   │   └── search.py          # Search blueprint
│   ├── models/                # Optional: database models or ORM classes
│   │   ├── __init__.py        # Marks the models directory as a Python package
│   │   └── user.py            # Example model: user account representation
│   └── utils/                 # Helper functions or shared utilities
│       ├── __init__.py        # Marks the utils directory as a Python package
│       ├── helpers.py         # General-purpose helper functions
│       ├── breadcrumb.py      # Builds breadcrumb navigation dynamically
│       ├── sections.py        # Handles section/volume/chapter organization
│       └── markdown.py        # Markdown parsing (convert .md to HTML)
├── templates/                 # HTML templates
│   ├── base.html              # Base layout template
│   ├── 404.html               # 404 error page
│   ├── home.html              # Home page template
│   ├── about.html             # About page template
│   ├── sitemap.html           # Updated modular sitemap template, links via md.render_md
│   ├── books/                 # Templates related to books
│   │   └── index.html         # Books listing template
│   └── auth/                  # Authentication templates
│       └── login.html         # Login page template
├── books/                     # Storage for all books (in Markdown format)
│   └── lorem-ipsum/           # Example book (one folder per book)
│       ├── README.md          # Root README for the book
│       └── volume-1/          # Subfolder for volumes
│           ├── README.md      # Volume README
│           └── chapter-1.md   # Chapter file
├── static/                    # Static assets (CSS, JavaScript, images)
│   ├── css/                   # CSS files
│   │   ├── paper.css          # PaperCSS — the less formal CSS framework
│   │   └── style.css          # Custom style file
│   ├── js/                    # JavaScript files
│   │   └── theme.js           # Dark/light mode toggle script
│   └── images/                # Image assets
│       ├── geometry2.png      # Background image
│       └── book_207114.png    # Favicon
├── data/                      # Data directory for SQLite or JSON storage
│   └── users.db               # SQLite database for the user authentication system
├── flaskapp.wsgi              # WSGI entry point for Apache/mod_wsgi
└── venv/                      # Virtual environment (excluded from version control)
```
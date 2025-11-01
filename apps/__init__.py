import os
from flask import Flask, render_template

# apps/__init__.py 
# Import necessary modules to create and configure the Flask app
# 'os' is used to interact with the operating system, such as file and directory operations.
# 'Flask' is the main class used to create the Flask app.
# 'render_template' is a function used to render HTML templates and pass variables to them.

# Create and configure the Flask application
def create_app():
    # Get the base directory of the project (flibrary/)
    base_dir = os.path.dirname(os.path.dirname(__file__))  
    # Define the paths for templates and static files
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    # Initialize the Flask app with the template and static directories
    app = Flask(
        __name__,
        template_folder=template_dir,  # Specify template directory
        static_folder=static_dir,      # Specify static folder
        static_url_path='/static'      # Set the URL prefix for static files
    )

    # ----------------------
    # Blueprints: Register different sections of the app
    # ----------------------
    # Register the 'home' blueprint
    from .routes.home import bp as home_bp
    app.register_blueprint(home_bp)

    # Register the 'about' blueprint with a URL prefix '/about'
    from .routes.about import bp as about_bp
    app.register_blueprint(about_bp, url_prefix='/about')  

    # Register the 'books' blueprint with a URL prefix '/books'
    from .routes.books import bp as books_bp
    app.register_blueprint(books_bp, url_prefix='/books')

    # Register the 'tutorials' blueprint with a URL prefix '/tutorials'
    from .routes.tutorials import bp as tutorials_bp
    app.register_blueprint(tutorials_bp, url_prefix='/tutorials')

    # Register the 'sitemap' blueprint with a URL prefix '/sitemap'
    from .routes.sitemap import bp as sitemap_bp
    app.register_blueprint(sitemap_bp, url_prefix='/sitemap')  

    # Register the 'markdown_render' blueprint
    from .routes.markdown_render import bp as md_bp  
    app.register_blueprint(md_bp)  

    # Register the 'search' blueprint with a URL prefix '/search'
    from .routes.search import bp as search_bp
    app.register_blueprint(search_bp, url_prefix='/search')
    
    # ----------------------
    # 404 handler: Custom handler for 404 errors (page not found)
    # ----------------------
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

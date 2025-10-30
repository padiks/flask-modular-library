import os
from flask import Flask, render_template

def create_app():
    # Determine the root folder of the project (flibrary)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Tell Flask where templates and static files are
    template_dir = os.path.join(root_dir, 'templates')
    static_dir = os.path.join(root_dir, 'static')

    # Create Flask app with explicit template and static folders
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    # Load configuration
    app.config.from_object('config.DevelopmentConfig')

    # ------------------------------
    # Import Blueprints
    # ------------------------------
    from .routes.home import bp as home_bp
    from .routes.books import bp as books_bp
    from .routes.tutorials import bp as tutorials_bp

    # ------------------------------
    # Register Blueprints
    # ------------------------------
    app.register_blueprint(home_bp)                  # home blueprint
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(tutorials_bp, url_prefix='/tutorials')

    # ------------------------------
    # Global 404 handler
    # ------------------------------
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app

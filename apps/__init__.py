import os
from flask import Flask, render_template

def create_app():
    base_dir = os.path.dirname(os.path.dirname(__file__))  # flibrary/
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir,
        static_url_path='/static'
    )

    # ----------------------
    # Blueprints
    # ----------------------
    from .routes.home import bp as home_bp
    from .routes.books import bp as books_bp
    from .routes.tutorials import bp as tutorials_bp
    # from .routes.lyrics import bp as lyrics_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(tutorials_bp, url_prefix='/tutorials')
    # app.register_blueprint(lyrics_bp, url_prefix='/lyrics')

    # ----------------------
    # 404 handler
    # ----------------------
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

from flask import Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    page_title = "ライトノベル図書館"
    return render_template('home.html', page_title=page_title, show_hero=False)

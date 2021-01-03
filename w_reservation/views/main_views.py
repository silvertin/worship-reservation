from flask import Blueprint, url_for, g
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    if g.user == None:
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('menu.mainmenu'))

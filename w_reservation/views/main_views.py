from flask import Blueprint, url_for, g, request, flash, render_template
from werkzeug.utils import redirect

from ..forms import ConnectForm

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    if g.user:
        return redirect(url_for('worship._list'))
    return redirect(url_for('main.connect_code'))


@bp.route('/connectcode/', methods=('GET','POST'))
def connect_code():
    form = ConnectForm()
    if request.method == 'POST' and form.validate_on_submit():
        if form.code.data == '5025':
            return redirect(url_for('menu.mainmenu'))
        else:
            flash('연결 코드가 다릅니다.')
    return render_template('menu/connect_form.html', form=form)


@bp.route('/admin')
def admin_login():
    if not g.user:
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('worship._list'))

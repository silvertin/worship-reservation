from flask import Blueprint, url_for, g, render_template, request, flash
from werkzeug.utils import redirect
from datetime import date

from .. import db
from .auth_views import login_required
from ..models import WorshipType
from ..forms import AddWorshipTypeForm

from colour import Color

bp = Blueprint('worshiptype', __name__, url_prefix='/worshiptype')


@bp.route('/list/')
@login_required
def _list():
    worshiptype_list = WorshipType.query.order_by(WorshipType.id.desc())
    return render_template('worship_type/worshiptype_list.html', worshiptype_list=worshiptype_list)


@bp.route('/add/', methods=('GET', 'POST'))
@login_required
def add():
    form = AddWorshipTypeForm()
    if request.method == 'POST' and form.validate_on_submit():
        worshiptype = WorshipType(detail=form.detail.data,
                          bgcolor=Color(form.bgcolor.data).get_hex_l()
                              )
        db.session.add(worshiptype)
        db.session.commit()
        return redirect(url_for('worshiptype._list'))
    return render_template('worship_type/addworshiptype_form.html', form=form)


@bp.route('/delete/<int:worshiptype_id>')
@login_required
def delete(worshiptype_id):
    worshiptype = WorshipType.query.get_or_404(worshiptype_id)
    db.session.delete(worshiptype)
    db.session.commit()
    return redirect(url_for('worshiptype._list'))

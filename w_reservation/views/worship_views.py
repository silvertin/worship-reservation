from flask import Blueprint, url_for, g, render_template, request, flash
from werkzeug.utils import redirect
from datetime import date

from .. import db
from .auth_views import login_required
from ..models import Worship, Seat, WorshipType
from ..forms import AddWorshipForm

bp = Blueprint('worship', __name__, url_prefix='/worship')


@bp.route('/list/')
@login_required
def _list():
    page = request.args.get('page', type=int, default=1)
    worship_list = Worship.query.order_by(Worship.date.desc())
    worship_list = worship_list.paginate(page, per_page=10)
    return render_template('worship/worship_list.html', worship_list=worship_list)


@bp.route('/add/', methods=('GET', 'POST'))
@login_required
def add():
    form = AddWorshipForm()
    worshiptype_list = WorshipType.query.order_by(WorshipType.id.desc())
    if request.method == 'POST' and form.validate_on_submit():
        worship = Worship(date=form.date.data,
                          part=form.part.data,
                          limit=form.limit.data,
                          worshiptype=form.worshiptype.data,
                          curnum='0')
        db.session.add(worship)
        for i in range(form.limit.data):
            seat = Seat(status=0, location=i+1)
            worship.seat_set.append(seat)
        db.session.commit()
        return redirect(url_for('worship._list'))
    return render_template('worship/addworship_form.html', form=form, worshiptype_list=worshiptype_list)


@bp.route('/delete/<int:worship_id>')
@login_required
def delete(worship_id):
    worship = Worship.query.get_or_404(worship_id)
    db.session.delete(worship)
    db.session.commit()
    return redirect(url_for('worship._list'))

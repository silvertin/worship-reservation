from flask import Blueprint, url_for, g, render_template, request, flash
from werkzeug.utils import redirect
from datetime import date
from operator import itemgetter

from .. import db
from .auth_views import login_required
from ..models import Worship, Seat, User
from ..forms import AddWorshipForm, RegisterSeatForm

bp = Blueprint('seat', __name__, url_prefix='/seat')


@bp.route('/list/<int:worship_id>', methods=('GET','POST'))
def _list(worship_id):
    worship = Worship.query.get_or_404(worship_id)
    form = RegisterSeatForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            seats = worship.seat_set
            for s in seats:
                if s.status == 0:
                    s.user = form.name.data
                    s.status = 1
                    worship.curnum = worship.curnum + 1
                    db.session.commit()
                    return redirect(url_for('seat._list',worship_id=worship_id))
            flash('예약이 가득 찼습니다.')
    return render_template('seat/seat_view.html', worship=worship, form=form)


@bp.route('/delete/<int:seat_id>')
@login_required
def delete(seat_id):
    seat = Seat.query.get_or_404(seat_id)
    seat.status = 0
    seat.user = None
    seat.worship.curnum = seat.worship.curnum - 1
    db.session.commit()
    return redirect(url_for('seat._list',worship_id=seat.worship_id))

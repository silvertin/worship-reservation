from flask import Blueprint, url_for, g, render_template, request, flash
from werkzeug.utils import redirect
from datetime import date

from .. import db
from .auth_views import login_required
from ..models import Worship, Seat, User
from ..forms import AddWorshipForm, RegisterSeatForm

bp = Blueprint('seat', __name__, url_prefix='/seat')


@bp.route('/list/<int:worship_id>', methods=('GET','POST'))
@login_required
def _list(worship_id):
    worship = Worship.query.get_or_404(worship_id)
    form = RegisterSeatForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            seats = worship.seat_set
            for s in seats:
                if s.location == form.seat.data:
                    s.user = g.user
                    s.status = 1
                    db.session.commit()
                    return redirect(url_for('seat._list',worship_id=worship_id))
    return render_template('seat/seat_view.html', worship=worship, form=form)



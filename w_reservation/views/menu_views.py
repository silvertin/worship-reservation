from flask import Blueprint, url_for, g, render_template, request
from werkzeug.utils import redirect
from datetime import date, timedelta

from .auth_views import login_required
from ..models import Worship

bp = Blueprint('menu', __name__, url_prefix='/menu')


@bp.route('/mainmenu/')
def mainmenu():
    worship_list = Worship.query.filter(Worship.date >= date.today()).filter(Worship.date <= date.today() + timedelta(days=7))
    menu = []
    for worship in worship_list:
        menu.append({'name': worship.date.strftime('%Y년%m월%d일')+'_'+str(worship.part), 'href': url_for('seat._list',worship_id=worship.id)})

    # if g.user.admin == 2:
    #    menu.append({'name':'-', 'href' : '#'})
    #    menu.append({'name': '예배현황', 'href': url_for('worship._list')})
    return render_template('menu/menu.html', menus=menu)


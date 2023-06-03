from flask import Blueprint,render_template, url_for
from werkzeug.utils import redirect

from pybo.models import Alarm

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('alarm._list'))

@bp.route('/detail/<int:alarm_id>/')
def detail(alarm_id):
    alarm = Alarm.query.get_or_404(alarm_id)
    return render_template('alarm/alarm_detail.html', alarm=alarm)
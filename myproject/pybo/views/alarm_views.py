from flask import Blueprint, render_template

from pybo.models import Alarm

bp = Blueprint('alarm', __name__, url_prefix='/alarm')


@bp.route('/list/')
def _list():
    alarm_list = Alarm.query.order_by(Alarm.alarmTime.asc())
    return render_template('alarm/alarm_list.html', alarm_list=alarm_list)


@bp.route('/detail/<int:alarm_id>/')
def detail(alarm_id):
    alarm = Alarm.query.get_or_404(alarm_id)
    return render_template('alarm/alarm_detail.html', alarm=alarm) 
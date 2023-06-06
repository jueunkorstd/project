from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Alarm
from pybo.forms import AlarmForm

bp = Blueprint('alarm', __name__, url_prefix='/alarm')
#alarm이라는 이름으로 블루프린트 객체를 생성
#__name__: 블루프린트의 이름, main_views를 인수로 가짐
#url_prefix='/alarm': 라우트 함수에 접두사로 사용할 경로를 지정

@bp.route('/ilst/')
def _list():
    alarm_list = Alarm.query.order_by(Alarm.alarmTime.asc())
    return render_template('alarm/alarm_list.html', alarm_list=alarm_list)

@bp.route('/detail/<int:alarm_id>/')
def detail(alarm_id):
    alarm = Alarm.query.get_or_404(alarm_id)
    return render_template('alarm/alarm_detail.html', alarm=alarm)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = AlarmForm()
    if request.method == 'POST' and form.validate_on_submit():
        alarm = Alarm(alarmName=form.alarmName.data, alarmTime=form.alarmTime.data)
        db.session.add(alarm)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('alarm/alarm_form.html', form=form)
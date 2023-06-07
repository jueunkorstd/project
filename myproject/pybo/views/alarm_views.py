from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from datetime import datetime
import paho.mqtt.client as mqtt


from pybo import db
from pybo.models import Alarm
from pybo.forms import AlarmForm

# MQTT 브로커에 연결합니다
broker_url = '44.202.115.227'  # MQTT 브로커의 URL을 입력하세요
broker_port = 1883  # MQTT 브로커의 포트 번호를 입력하세요
client = mqtt.Client()

bp = Blueprint('alarm', __name__, url_prefix='/alarm')
#alarm이라는 이름으로 블루프린트 객체를 생성
#__name__: 블루프린트의 이름, main_views를 인수로 가짐
#url_prefix='/alarm': 라우트 함수에 접두사로 사용할 경로를 지정

@bp.route('/ilst/')
def _list():
    current_datetime = datetime.now()
    page = request.args.get('page', type=int, default=1)
    alarm_list = Alarm.query.order_by(Alarm.alarmTime.asc())
    alarm_list = alarm_list.paginate(page=page, per_page=10)
    return render_template('alarm/alarm_list.html', alarm_list=alarm_list, current_datetime=current_datetime)

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

@bp.route('/delete/<int:alarm_id>')
def delete(alarm_id):
    alarm = Alarm.query.get_or_404(alarm_id)
    db.session.delete(alarm)
    db.session.commit()
    return redirect(url_for('main.index'))

# MQTT 브로커에 연결합니다
broker_url = '44.202.115.227'  # MQTT 브로커의 URL을 입력하세요
broker_port = 1883  # MQTT 브로커의 포트 번호를 입력하세요
client = mqtt.Client()

# 연결 성공 시 실행됩니다
def on_connect(client, userdata, flags, rc):
    print('MQTT 브로커에 연결되었습니다.')
    # 토픽을 구독합니다
    topic = 'home/garden/fountain'  # 구독할 토픽을 입력하세요
    client.subscribe(topic)
    print('토픽 구독 성공:', topic)

# 메시지를 수신할 때 실행됩니다
def on_message(client, userdata, msg):
    print('새로운 메시지 수신:', msg.topic, msg.payload.decode())
    # 메시지를 처리하는 추가 로직을 여기에 작성하세요

# 오류 발생 시 실행됩니다
def on_error(client, userdata, msg):
    print('MQTT 오류:', msg)

client.on_connect = on_connect
client.on_message = on_message
client.on_error = on_error

client.connect(broker_url, broker_port, 60)
client.loop_start()
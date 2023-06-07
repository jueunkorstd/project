from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt

from pybo import db
from pybo.models import Alarm
from pybo.forms import AlarmForm

broker_url = '44.202.115.227'
broker_port = 1883
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print('MQTT 브로커에 연결되었습니다.')
    topic = 'home/garden/fountain'
    client.subscribe(topic)
    print('토픽 구독 성공:', topic)

def on_message(client, userdata, msg):
    print('새로운 메시지 수신:', msg.topic, msg.payload.decode())
    
def on_error(client, userdata, msg):
    print('MQTT 오류:', msg)

client.on_connect = on_connect
client.on_message = on_message
client.on_error = on_error

client.connect(broker_url, broker_port, 60)
client.loop_start()

bp = Blueprint('alarm', __name__, url_prefix='/alarm')
#alarm이라는 이름으로 블루프린트 객체를 생성
#__name__: 블루프린트의 이름, main_views를 인수로 가짐
#url_prefix='/alarm': 라우트 함수에 접두사로 사용할 경로를 지정

@bp.route('/ilst/')
def _list():
    current_datetime = datetime.now()
    page = request.args.get('page', type=int, default=1)
    alarm_list = Alarm.query.order_by(Alarm.alarmTime.asc())
    alarm_list = alarm_list.paginate(page=page, per_page=100)


    for alarm in alarm_list.items:  # 페이지의 항목들을 순회합니다.
        alarm_datetime = datetime.strptime(alarm.alarmTime, '%H:%M')
        alarm_time = alarm_datetime.replace(second=0, microsecond=0).time()
        current_time = current_datetime.replace(second=0, microsecond=0).time()
        if alarm_time.hour == current_time.hour and alarm_time.minute == current_time.minute:
                print("Alarm!")
                return redirect(url_for('alarm.alarm_run'))
        
    return render_template('alarm/alarm_list.html', alarm_list=alarm_list, current_datetime=current_datetime)

@bp.route('/alarm/run/')
def alarm_run():
    current_datetime = datetime.now()
    print("Alarm On")
    #GPIO로 led, buzzer 제어
    return render_template('alarm/alarm_run.html', current_datetime=current_datetime)

@bp.route('/alarm/stop/', methods=['POST'])
def stop_alarm():
    print("Alarm Off")
    # 알람을 끄는 로직 구현
    # GPIO 등을 사용하여 알람을 제어
    
    # 알람을 끄고 나서 다른 페이지로 리다이렉트
    current_datetime = datetime.now()
    return redirect(url_for('main.index'))

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

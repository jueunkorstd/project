from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from pybo.models import Alarm

bp = Blueprint('main', __name__, url_prefix='/')
#main이라는 이름으로 블루프린트 객체를 생성
#__name__: 블루프린트의 이름, main_views를 인수로 가짐
#url_prefix='/': 라우트 함수에 접두사로 사용할 경로를 지정


@bp.route('/')
def index():
    return redirect(url_for('alarm._list'))


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class AlarmForm(FlaskForm):
    alarmName = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    alarmTime = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
from pybo import db

class Alarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alarmName = db.Column(db.String(200), nullable=False)
    alarmTime = db.Column(db.Text(), nullable=False)
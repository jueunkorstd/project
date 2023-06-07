from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, alarm_views
    app.register_blueprint(main_views.bp)
    #main_views.py에서 생성한 블루프린트 객체 bp를 등록
    app.register_blueprint(alarm_views.bp)

    

    return app
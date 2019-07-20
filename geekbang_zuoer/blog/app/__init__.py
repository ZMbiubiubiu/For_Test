#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 14:53
# @Author  : bingo
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
bootstap = Bootstrap(app)
db = SQLAlchemy(app)
db.init_app(app=app)
with app.app_context():
    db.create_all(app=app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'  # 强制用户在查看应用的特定页面之前登录

from app import routes, models, errors

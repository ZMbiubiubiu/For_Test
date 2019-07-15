#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 14:53
# @Author  : bingo
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'  # 强制用户在查看应用的特定页面之前登录

from app import routes





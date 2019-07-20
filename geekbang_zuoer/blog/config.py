#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 14:52
# @Author  : bingo
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+cymysql://root:mingyue6868@localhost:3306/blog?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ksjdflasjdflksaj'
    POSTS_PER_PAGE = 25
    # 电子邮件的配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['zhangmeng.lee@foxmail.com']
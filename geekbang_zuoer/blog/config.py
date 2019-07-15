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
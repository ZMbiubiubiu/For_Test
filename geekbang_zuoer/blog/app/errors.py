#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 22:59
# @Author  : bingo
# @Site    : 
# @File    : errors.py
# @Software: PyCharm

from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    # 500错误的错误处理程序应当在引发数据库错误后调用
    # 比如用户名重复实际上就是这种情况
    db.session.rollback()
    return render_template('500.html'), 500

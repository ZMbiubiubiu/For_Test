#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 15:30
# @Author  : bingo
# @Site    : 
# @File    : routes.py
# @Software: PyCharm
from werkzeug.urls import url_parse
from datetime import datetime

from app import app, db
from flask import render_template, flash, url_for, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from app.forms import LoginForm, RegistrationForm, EditUserProfileForm, PostForm


@app.before_request
def before_request():
    if current_user.is_authenticated:
        # 在调用current_user时，就会有一个区数据库中查找的过程，并将用户添加到数据库会话中的操作
        # 所以下面才可以直接 db.session.commit()
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post is now alive ")
        # 简单的技巧叫做Post/Redirect/Get模式。
        # 它避免了用户在提交网页表单后无意中刷新页面时插入重复的动态
        # 以下所有涉及到表单的试图函数，都采用上述的方法
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    # posts = current_user.followed_posts().all()  # all 返回值是包含所有结果的列表
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )
    next_page = url_for('index', page=posts.next_num) if posts.has_next else None
    prev_page = url_for('index', page=posts.prev_num) if posts.has_prev else None
    return render_template(
        'index.html', title='Home', form=form,
        posts=posts.items,
        prev_page=prev_page, next_page=next_page
    )


@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )
    prev_page = url_for('explore', page=posts.next_num) if posts.has_next else None
    next_page = url_for('explore', page=posts.prev_num) if posts.has_prev else None
    return render_template(
        'index.html', title="Explore",
        posts=posts.items,
        prev_page=prev_page, next_page=next_page,
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulation. You have Registered Successfully')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')
    # return redirect(url_for('register'))  #  报错 ERR_TOO_MANY_REDIRECTS 重定向次数太多


@app.route('/user/<username>')
# @login_required
def user(username):
    # 当有结果时它的工作方式与first()完全相同，但是在没有结果的情况下会自动发送404 error给客户端
    user = User.query.filter_by(username=username).first_or_404()
    # 从请求参数中获取page
    page = request.args.get('page', 1, type=int)
    posts = user.post.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )
    prev_page = url_for('user', username=username, page=posts.prev_num) if posts.has_prev else None
    next_page = url_for('user', username=username, page=posts.next_num) if posts.has_next else None
    return render_template(
        'user.html', user=user,
        posts=posts.items,
        prev_page=prev_page, next_page=next_page,
    )


@app.route('/edit_profile', methods=["POST", "GET"])
@login_required
def edit_profile():
    form = EditUserProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('profile.html', title='Edit Profile', form=form)


# follow someone
@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(f"User {username} is not Found!")
        return redirect('index')
    elif user == current_user:
        flash('You can"t follow yourself.')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(f'You have followed {username} successfully.')
    return redirect(url_for('user', username=username))


# unfollow someone
@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(f'User {username} is not Found!')
        return redirect('index')
    if current_user == user:
        flash('You can"t unfollow yourself')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(f'You have unfollowed {username} Successfully!')
    return redirect(url_for('user', username=username))

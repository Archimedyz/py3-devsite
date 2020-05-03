from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/index')
@app.route('/')
def index_page():
    return render_template('index.html', title='Home')

@app.route('/messages')
@login_required
def messages_page():
    messages = [
        {'username': 'Anonymous', 'text_content': 'Hello world!'},
        {'username': 'Admin', 'text_content': 'Good night.'}
    ]
    return render_template('messages.html', title='Messages', messages=messages)

@app.route('/login', methods=['GET','POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('index_page'))

    form = LoginForm()

    if form.validate_on_submit():
        _username = form.username.data
        _password = form.password.data
        _rm = form.remember_me.data

        # fetch user by username
        user = User.query.filter_by(username=_username).first()

        # check if user exists, and that password matches
        if user is None or not user.check_password(_password):
            flash('Invalid login credentials')
            return redirect(url_for('login_page'))

        # login the user
        login_user(user, remember=_rm)

        # redirect if needed
        next_page = request.args.get('next')
        if next_page and url_parse(next_page).netloc == '':
            return redirect(next_page)

        # retiderct to index page by default
        return redirect(url_for('index_page'))

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index_page'))


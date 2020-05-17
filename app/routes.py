from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

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

@app.route('/signup', methods=['GET','POST'])
def signup_page():

    if current_user.is_authenticated:
        return redirect(url_for('index_page'))

    form = SignUpForm()

    if form.validate_on_submit():
        _username = form.username.data
        _email = form.email.data
        _password = form.password.data

        # at this point, the form has done basic validation
        # we should be OK to create the user now
        user = User(username=_username, email=_email)
        user.set_password(_password)

        db.session.add(user)
        db.session.commit()

        flash('Congratulations! You\'ve successfully registered for the Devsite.')

        # retiderct to login page to let the new user login
        return redirect(url_for('login_page'))

    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/user/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.all()

    return render_template('user.html', user=user, posts=posts)


from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/index')
@app.route('/')
def index_page():
    user = {'username': 'Awais'}
    return render_template('index.html', title='Home', user=user)

@app.route('/messages')
def messages_page():
    user = {'username': 'Awais'}
    messages = [
        {'username': 'Anonymous', 'text_content': 'Hello world!'},
        {'username': 'Admin', 'text_content': 'Good night.'}
    ]
    return render_template('messages.html', title='Messages', user=user, messages=messages)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        rm = form.remember_me.data
        flash(f'Login requested for user {username}, remember_me={rm}')

        return redirect(url_for('index_page'))

    return render_template('login.html', title='Login', form=form)


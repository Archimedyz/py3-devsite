from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
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

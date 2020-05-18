from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

### SMTP handling for errors
if not app.debug and app.config['MAIL_SERVER']:
    # set authorization credentials
    auth = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

    # determine security use for SMTP
    secure = None
    if app.config['MAIL_USE_TLS']:
        secure = ()

    # initialize SMTP handler
    mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr=f'no-reply@' + app.config['MAIL_SERVER'],
        toaddrs=app.config['ADMINS'],
        subject='Devsite Failure',
        credentials=auth,
        secure=secure
    )

    # only use the handler for ERROR (or higher) logs.
    mail_handler.setLevel(logging.ERROR)

    # hook the handler into the app.
    app.logger.addHandler(mail_handler)

from app import routes, models, errors

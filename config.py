import os

path_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'test_site_secret_key'

    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(path_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SMTP configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admin@example.com']

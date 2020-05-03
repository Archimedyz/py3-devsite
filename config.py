import os

path_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'test_site_secret_key'

    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(path_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

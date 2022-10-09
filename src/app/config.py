import os


basedir = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.abspath('../dist/html/templates')
STATIC_DIR = os.path.abspath('../dist')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://sid:12345@localhost/checkers'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

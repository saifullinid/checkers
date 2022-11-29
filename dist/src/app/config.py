import os


basedir = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.abspath('src/html/templates')
STATIC_DIR = os.path.abspath('src/')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://checkers_su:123456@db:5432/checkers'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

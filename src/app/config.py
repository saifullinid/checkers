import os


TEMPLATE_DIR = os.path.abspath('src/html/templates')
STATIC_DIR = os.path.abspath('./src')

DATABASE_NAME = 'checkers'
DATABASE_USERNAME = 'checkers_su'
DATABASE_PASSWORD = '123456'
DATABASE_HOST = os.environ.get('DATABASE_HOST') or 'localhost'
DATABASE_PORT = '5432'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = f'postgresql://' \
                              f'{DATABASE_USERNAME}:' \
                              f'{DATABASE_PASSWORD}@' \
                              f'{DATABASE_HOST}:' \
                              f'{DATABASE_PORT}/' \
                              f'{DATABASE_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

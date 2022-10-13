from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.app import db, login_manager
# классы-таблицы SQLAlchemy


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))

    def __repr__(self):
        return f'USER - {self.username}'

    def set_password(self, psw):
        self.password_hash = generate_password_hash(psw)

    def check_password(self, psw):
        return check_password_hash(self.password_hash, psw)


class Rooms(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomname = db.Column(db.String(64), index=True, unique=True, nullable=False)
    amount_players = db.Column(db.Integer, index=True)
    users = db.relationship('Users', backref='room', lazy=True)

    @staticmethod
    def get_roomnames():
        output_roomnames = []
        rooms = Rooms.query.all()
        for room in rooms:
            output_roomnames.append((room.roomname, room.roomname))
        return output_roomnames


class Colors(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(64), index=True, unique=True, nullable=False)
    users = db.relationship('Users', backref='color', lazy=True)


# Пользовательский загрузчик, связь flask-login с SQLAlchemy
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

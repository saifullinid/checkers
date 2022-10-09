from src.app.dbmodel.dbmodel import Users, Rooms, Colors


# класс для работы с БД через SQLAlchemy
class dbService:
    @classmethod
    def add_new_user(cls, db, username, email, psw):
        user = Users.query.filter_by(username=username).first()
        user_by_email = Users.query.filter_by(email=email).first()
        if not user and not user_by_email:
            user = Users(username=username, email=email)  # type: ignore
            user.set_password(psw)
            db.session.add(user)
            db.session.commit()
            return user

    @staticmethod
    def login_current_user(username, psw):
        user = Users.query.filter_by(username=username).first()
        if user:
            if user.check_password(psw):
                return user

    @staticmethod
    def add_new_room(roomname, db):
        room = Rooms.query.filter_by(roomname=roomname).first()
        if not room:
            room = Rooms(roomname=roomname, amount_players=0)  # type: ignore
            db.session.add(room)
            db.session.commit()

    @staticmethod
    def add_player_to_room(user, roomname, db):
        room = Rooms.query.filter_by(roomname=roomname).first()
        user.room_id = room.id
        room.amount_players += 1
        db.session.add(user)
        db.session.add(room)
        db.session.commit()

    @staticmethod
    def get_roomname_by_user(user):
        sql_row_room = Rooms.query.filter(Rooms.id == user.room_id).first()
        if sql_row_room:
            return sql_row_room.roomname

    @staticmethod
    def set_color(username, color, db):
        sql_row_color = Colors.query.filter_by(color=color).first()
        user = Users.query.filter_by(username=username).first()
        user.color_id = sql_row_color.id
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def logout_user_from_room(user, db):
        room_id = user.room_id
        if room_id:
            room = Rooms.query.filter_by(id=room_id).first()
            room_id = None
            db.session.delete(room)
            db.session.commit()
            db.session.add(user)
            db.session.commit()

    @staticmethod
    def delete_all_rooms(db):
        rooms = Rooms.query.all()
        for room in rooms:
            db.session.delete(room)
        db.session.commit()
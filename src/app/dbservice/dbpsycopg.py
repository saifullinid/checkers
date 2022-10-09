import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

psycopg_config = {'host': '127.0.0.1',
                  'user': 'sid',
                  'password': '12345',
                  'db_name': 'checkers'}


# класс для работы с БД через psycopg2
class dbPsycopg():
    def set_connection(self):
        try:
            connection = psycopg2.connect(
                host=psycopg_config['host'],
                user=psycopg_config['user'],
                password=psycopg_config['password'],
                database=psycopg_config['db_name'],
            )
            connection.autocommit =True
            return connection
        except psycopg2.InterfaceError as e:
            print('[INFO] Error while working with PostgreSQL', e)

    def set_password(self, psw):
        return generate_password_hash(psw)

    @staticmethod
    def check_password(password_hash, psw):
        return check_password_hash(password_hash, psw)

    def add_new_user(self, username, email, psw):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM users 
                    WHERE users.username = (%s);
                    """,
                    (username,)
                )
                user_by_username = cursor.fetchone()
                cursor.execute(
                    """
                    SELECT * FROM users 
                    WHERE users.email = (%s);
                    """,
                    (email,)
                )
                user_by_email = cursor.fetchone()

                if not user_by_username and not user_by_email:
                    cursor.execute(
                        '''
                        INSERT INTO users (username, email, password_hash) 
                        VALUES (%s, %s, %s);
                        ''',
                        (username, email, self.set_password(psw))
                    )
                    print('[INFO] PostgreSQL: New user registered')
                    return True
                else:
                    print('[INFO] PostgreSQL: This name or email is already taken')
                    return False
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

    def login_current_user(self, username, psw):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT password_hash FROM users 
                    WHERE users.username = (%s);
                    """,
                    (username,)
                )
                password_hash = cursor.fetchone()[0]
                if password_hash:
                    if self.check_password(password_hash, psw):
                        print('[INFO] PostgreSQL: User login')
                        return True
                    else:
                        print('[INFO] PostgreSQL: Invalid password')
                        return False
                else:
                    print('[INFO] PostgreSQL: User not found')
                    return False
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

    def add_new_room(self, roomname):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM rooms 
                    WHERE rooms.roomname = (%s);
                    """,
                    (roomname,)
                )
                room_by_roomname = cursor.fetchone()

                if not room_by_roomname:
                    cursor.execute(
                        '''
                        INSERT INTO rooms (roomname, amount_players) 
                        VALUES (%s, %s);
                        ''',
                        (roomname, 0,)
                    )
                    print('[INFO] PostgreSQL: New room created')
                    return True
                else:
                    print('[INFO] PostgreSQL: This roomname is already taken')
                    return False
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

    def add_player_to_room(self, username, roomname):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM rooms 
                    WHERE rooms.roomname = (%s);
                    """,
                    (roomname,)
                )
                room_by_roomname = cursor.fetchone()

                if room_by_roomname:
                    cursor.execute(
                        '''
                        UPDATE users
                        SET room_id = rooms.id 
                        FROM rooms
                        WHERE users.username = (%s) AND rooms.roomname = (%s);
                        ''',
                        (username, roomname,)
                    )
                    cursor.execute(
                        '''
                        UPDATE rooms
                        SET amount_players = amount_players + 1 
                        WHERE rooms.roomname = (%s);
                        ''',
                        (roomname,)
                    )
                    print('[INFO] PostgreSQL: Room and User updated')
                    return True
                else:
                    print('[INFO] PostgreSQL: Roomname not found')
                    return False
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

    def logout_user_from_room(self, username):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    SELECT room_id 
                    FROM users 
                    WHERE users.username = (%s);
                    ''',
                    (username,)
                )
                room_id = cursor.fetchone()[0]
                cursor.execute(
                    '''
                    UPDATE users
                    SET room_id = NULL 
                    WHERE users.username = (%s);
                    ''',
                    (username, )
                )
                cursor.execute(
                    '''
                    DELETE FROM rooms 
                    WHERE id = (%s);
                    ''',
                    (room_id,)
                )
                print('[INFO] PostgreSQL: User logout, ROOM deleted')
                return True
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

    def get_roomname_by_user(self, username):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    SELECT roomname 
                    FROM rooms 
                    JOIN users 
                    ON users.room_id = rooms.id 
                    WHERE users.username = (%s);
                    ''',
                    (username,)
                )
                roomname = cursor.fetchone()[0]
                print('[INFO] PostgreSQL: Room name received', roomname)
                return roomname
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

    def set_color(self, username, color):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    UPDATE users 
                    SET color_id = colors.id 
                    FROM colors 
                    WHERE users.username = (%s) AND colors.color = (%s);
                    ''',
                    (username, color,)
                )
                print('[INFO] PostgreSQL: Choice Color:', color)
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

    def delete_all_rooms(self):
        connection = self.set_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    DELETE FROM rooms;
                    '''
                )
                print('[INFO] PostgreSQL: Rooms removed:')
        except Exception as e:
            print('[INFO] Error while working with PostgreSQL', e)
        finally:
            if connection:
                connection.close()
            print('[INFO] PostgreSQL connection closed')

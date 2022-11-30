import psycopg2
from werkzeug.security import generate_password_hash


def set_connection():
    connection = psycopg2.connect(
        host='db',
        user='checkers_su',
        password='123456',
        database='checkers',
    )
    connection.autocommit = True
    return connection


def add_colors_and_test_users():
    connection = set_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO colors (color) VALUES (%s), (%s)
                ON CONFLICT (color) DO NOTHING;
                ''',
                ('black', 'white')
            )
            cursor.execute(
                '''
                INSERT INTO users (username, email, password_hash) 
                VALUES (%s, %s, %s), (%s, %s, %s)
                ON CONFLICT (email) DO NOTHING;
                ''',
                ('user_1', 'user_1@example.com', generate_password_hash('123456'),
                 'user_2', 'user_2@example.com', generate_password_hash('123456'))
            )
    except Exception as e:
        print('[INFO] Error while working with PostgreSQL', e)
    finally:
        if connection:
            connection.close()


add_colors_and_test_users()

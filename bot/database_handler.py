import sqlite3

user_conn = sqlite3.connect('users.db')
user_cursor = user_conn.cursor()
user_cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE)")

meeting_conn = sqlite3.connect('meetings.db')

def add_user(tag=str, id=int):
    cursor = user_conn.cursor()


import sqlite3


connect = sqlite3.connect("products.db")
cursor = connect.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')
    connect.commit()

def get_all_products():
    initiate_db()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connect.commit()
    return all_products


def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"{username}", f"{email}", f"{age}", "1000"))
    connect.commit()

def is_included(username):
    cursor.execute("SELECT username From Users")
    users = cursor.fetchall()
    for user in users:
        if username == user or username == user[0]:
            return True
    return False

initiate_db()
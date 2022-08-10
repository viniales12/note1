import sqlite3


def connect_db():
    conn = sqlite3.connect('my_db.db')
    return conn


def create_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE users ( user_id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL,
                    country TEXT NOT NULL)
                ''')
    conn.commit()
    conn.close()


def add_user(user):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO users (name, email, phone, address,       
                    country) VALUES (?, ?, ?, ?, ?)
    ''', (user['name'],
          user['email'], user['phone'], user['address'],
          user['country']))

    conn.commit()
    conn.close()

    return f"New User {user['name']} Successfully added"


def show_db():
    users = []

    conn = connect_db()
    conn.row_factory = sqlite3.Row
    #  ^^^^^  umożliwia dostęp do kolumn za pomocą nazw, podczas gdy zwykła krotka wymagałaby użycia indeksów numerowanych
    cur = conn.cursor()

    for i in cur.execute('''SELECT * FROM users'''):
        user = {}
        user["user_id"] = i["user_id"]
        user["name"] = i["name"]
        user["email"] = i["email"]
        user["phone"] = i["phone"]
        user["address"] = i["address"]
        user["country"] = i["country"]
        users.append(user)

    return users


def show_db_id(id):
    users = []

    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    for i in cur.execute('''SELECT * FROM users WHERE user_id == ?''', (id,)):
        # przecinek w (id ,) bardzo ważny, inaczej błąd przy wprowadzeniu liczby dwucyfrowej
        user = {}
        user["user_id"] = i["user_id"]
        user["name"] = i["name"]
        user["email"] = i["email"]
        user["phone"] = i["phone"]
        user["address"] = i["address"]
        user["country"] = i["country"]
        users.append(user)

    return users


def delete(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''DELETE FROM users WHERE user_id == ?''', (id,))

    conn.commit()
    conn.close()

    return f'User id:{id} Successfully deleted'


def update(user, id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?",
                (user["name"], user["email"], user["phone"], user["address"], user["country"], id))

    conn.commit()
    conn.close()

    return f"User {user['name']} Successfully updated"

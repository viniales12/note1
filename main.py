import json
import sqlite3

from flask import Flask, jsonify

user = {
    "name": "Charles Effiong",
    "email": "charles@gamil.com",
    "phone": "067765665656",
    "address": "Lui Str, Innsbruck",
    "country": "Italy"
}


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

    return "ok"


def show_db():
    users = []

    conn = connect_db()
    conn.row_factory = sqlite3.Row
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

    json_string = json.dumps(users)
    return json_string


def show_db_id(id):
    users = []

    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    for i in cur.execute('''SELECT * FROM users WHERE user_id == ?''', (id)):
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
    cur.execute('''DELETE FROM users WHERE user_id == ?''', (id))

    conn.commit()
    conn.close()

    return 'delete ok'


def update(user, id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?",
                (user["name"], user["email"], user["phone"], user["address"], user["country"], id))

    conn.commit()
    conn.close()

    return "ok is update"


app = Flask(__name__)


@app.route("/add", methods=['GET', 'POST'])
def add():
    return add_user(user)


@app.route("/show", methods=['GET'])
def show():
    return jsonify(show_db())


@app.route("/show/<user_id>", methods=['GET'])
def show_id(user_id):
    return jsonify(show_db_id(user_id))


@app.route("/delete/<user_id>", methods=['GET', 'DELETE'])
def delete_user(user_id):
    return delete(user_id)


@app.route("/update/<user_id>", methods=['GET', 'PUT'])
def update_user(user_id):
    return update(user, user_id)


app.run()

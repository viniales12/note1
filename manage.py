from flask import Flask, jsonify
from db.db_management import Database
from user import *

app = Flask(__name__)
data = Database(user_2)


@app.route("/add", methods=['GET', 'POST'])
def add():
    return data.add_user()


@app.route("/show", methods=['GET'])
def show():
    return jsonify(data.show_db())


@app.route("/show/<user_id>", methods=['GET'])
def show_id(user_id):
    return jsonify(data.show_db_id(user_id))


@app.route("/delete/<user_id>", methods=['GET', 'DELETE'])
def delete_user(user_id):
    return data.delete(user_id)


@app.route("/update/<user_id>", methods=['GET', 'PUT'])
def update_user(user_id):
    return data.update(user_id)


@app.route("/", methods=['GET'])
def hello():
    return 'Hello'
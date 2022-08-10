from flask import Flask, jsonify
from db.db_management import *
from user import *

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

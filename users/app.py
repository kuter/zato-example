import uuid

from flask import Flask, abort, jsonify, request

app = Flask(__name__)


USERS = {"foo": "bar"}


@app.route("/")
def index():
    return "Users service!"


@app.route("/login", methods=["GET", "POST"])
def login():
    login = request.form["login"]
    password = request.form["password"]

    valid = login in USERS and password == USERS[login]
    if not valid:
        app.logger.info("Login failed.")
        abort(401)

    app.logger.info("Login successful.")

    return jsonify(
        {"first_name": "foo", "last_name": "bar", "token": uuid.uuid4().hex}
    )

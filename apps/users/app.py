from datetime import datetime, timedelta

from flask import Flask, abort, jsonify, request
from jose import jwt

app = Flask(__name__)


USERS = {"foo": "bar"}
JWT_KEY = "secret"


@app.route("/")
def index():
    return "Users service!"


@app.route("/login", methods=["POST"])
def login():
    login = request.form["login"]
    password = request.form["password"]

    valid = login in USERS and password == USERS[login]
    if not valid:
        app.logger.info("Login failed.")
        abort(401)

    app.logger.info("Login successful.")

    claims = {
        "login": login,
        "scopes": ["photos:view"],
        "exp": datetime.utcnow() + timedelta(minutes=5),
    }
    token = jwt.encode(claims, JWT_KEY, algorithm="HS256")

    return jsonify({"token": token})

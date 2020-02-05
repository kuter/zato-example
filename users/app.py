from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return "Users service!"


@app.route("/login", methods=["GET", "POST"])
def login():
    return jsonify({
        "first_name": "foo",
        "last_name": "bar"
    })


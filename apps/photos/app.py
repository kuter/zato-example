from flask import Flask, abort, jsonify, request
from jose import jwt

app = Flask(__name__)

JWT_KEY = "secret"


class Photo:
    def __init__(self, photo_id, src, login_required):
        self.photo_id = photo_id
        self.src = src
        self.login_required = login_required


PHOTOS = [
    Photo(1, "https://via.placeholder.com/150/0000FF/808080", False),
    Photo(2, "https://via.placeholder.com/150/FF0000/FFFFFF", True),
    Photo(3, "https://via.placeholder.com/150/FFFF00/000000", False),
]


def has_perm(perm):
    try:
        token = request.headers.get("Authorization").split()[1]
        claims = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
    except:
        return False
    else:
        return perm in claims["scopes"]


@app.route("/")
def index():
    return "Photos service!"


@app.route("/photo/<int:photo_id>")
def show_photo(photo_id):
    obj = next((x for x in PHOTOS if x.photo_id == photo_id), None)
    if not obj:
        abort(404)
    if obj.login_required and not has_perm("photos:view"):
        abort(403)
    return jsonify({"src": obj.src})

from flask import Flask, abort, jsonify, request

app = Flask(__name__)


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


def is_authenticated():
    return request.headers.get("X-Token")


@app.route("/")
def index():
    return "Photos service!"


@app.route("/photo/<int:photo_id>")
def show_photo(photo_id):
    obj = next((x for x in PHOTOS if x.photo_id == photo_id), None)
    if not obj:
        abort(404)
    if obj.login_required and not is_authenticated():
        abort(403)
    return jsonify({"src": obj.src})

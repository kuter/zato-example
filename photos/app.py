from flask import Flask, jsonify, request

app = Flask(__name__)


class Photo:
    def __init__(self, photo_id, src, login_required):
        self.photo_id = photo_id
        self.src = src
        self.login_required = login_required


PHOTOS = [
    Photo(1, "https://via.placeholder.com/150/0000FF/808080", False),
    Photo(2, "https://via.placeholder.com/150/FF0000/FFFFFF", True),
    Photo(3, "https://via.placeholder.com/150/FFFF00/000000", False)
]

def is_authenticated():
    app.logger.info("is_authenticated called !")
    return True


@app.route("/")
def index():
    return "Photos service!"


@app.route("/photo/<int:photo_id>")
def show_photo(photo_id):
    app.logger.info("show_photo {}".format(photo_id))
    obj = next((x for x in PHOTOS if x.photo_id == photo_id), None)
    return jsonify({
        "src": obj.src
    })

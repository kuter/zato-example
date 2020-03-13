from flask import Flask, request
from flask_babel import Babel, lazy_gettext

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(["pl", "en"])


@app.route("/", methods=["POST"])
def index():
    text = request.form["text"]
    translated = lazy_gettext(text)
    return str(translated)

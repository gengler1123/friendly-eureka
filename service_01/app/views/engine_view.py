from app import flask_app as app
import flask
from engine import Engine


engine = Engine()


@app.route("/engine_call", methods=["POST"])
def engine_call():
    """

    """
    return engine(flask.request)

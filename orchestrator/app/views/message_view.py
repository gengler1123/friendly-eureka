from app import flask_app as app
from ferry import Ferry
import json
from flask import request

ferry = Ferry()


@app.route("/message", methods=["POST"])
def message_view():
    """


    """
    ferry(request)

    return json.dumps(
        {
            "Status": "Called Ferry"
        }
    )
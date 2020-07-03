from app import flask_app as app
from carburetor import Carburetor
import json
from flask import request


carburetor = Carburetor()


@app.route("/message", methods=["POST"])
def message_view():
    """


    """
    try:
        carburetor(request)
        carburetor_message = "Success"
    except Exception as e:
        carburetor_message = f"carburetor Exception: {e}"

    return json.dumps(
        {
            "Status": carburetor_message
        }
    )

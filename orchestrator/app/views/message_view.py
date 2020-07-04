from app import flask_app as app
from carburetor import Carburetor
import json
from flask import request
from os import environ


carburetor = Carburetor()


@app.route("/message", methods=["POST"])
def message_view():
    """


    """
    service_01_endpoint = environ.get("SERVICE_01_ENDPOINT", "http://engine:8000")
    service_02_endpoint = environ.get("SERVICE_02_ENDPOINT", "http://service-02:8000")
    rabbitmq_endpoint = environ.get("RABBITMQ_ENDPOINT", "http://rabbitmq:5672")
    redis_endpoint = environ.get("REDIS_ENDPOINT")
    psql_host = environ.get("PSQL_HOST")
    psql_port = environ.get("PSQL_PORT")
    psql_user = environ.get("PSQL_USER")
    psql_pass = environ.get("PSQL_PASS")

    parameters = {
        "engine_endpoint": service_01_endpoint,
        "rabbitmq_endpoint": rabbitmq_endpoint,
        "redis_endpoint": redis_endpoint
    }
    try:
        carburetor(
            _request=request,
            parameters=parameters
        )
        carburetor_message = "Success"
    except Exception as e:
        carburetor_message = f"carburetor Exception: {e}"

    return json.dumps(
        {
            "Status": carburetor_message
        }
    )

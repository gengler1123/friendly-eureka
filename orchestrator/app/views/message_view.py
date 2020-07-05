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
        initial_request = request.form.to_dict(flat=False)
        initial_json = request.get_json()
        initial_data = request.data.decode('utf-8')
    except Exception as e:
        initial_request = {}
        initial_json = {}
        initial_data = ""
    resp = {"First REsponse": "Hello"}
    try:
        resp = carburetor(
            _request=request,
            parameters=parameters
        )
        carburetor_message = "Success"
    except Exception as e:
        carburetor_message = f"carburetor Exception: {e}"

    try:
        response = {
            "Status": carburetor_message,
            "request_form": initial_request,
            "initial_data": initial_data,
            "initial_json": initial_json,
            "carb_response": resp,
            "response_text": resp.get("response_text", "None"),
            "response_metadata": resp.get("response_metadata", {})
        }
    except Exception as e:
        response = {
            "exception": f"{e}"
        }

    try:
        resp_to_send = json.dumps(response)
    except Exception as e:
        resp_to_send = json.dumps({
            "Exception": f"{e}"
        })

    return resp_to_send

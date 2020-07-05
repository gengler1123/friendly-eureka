import flask
from requests import post


class Carburetor:
    """

    """

    def __init__(self):
        """

        """

    def _send_to_engine(
        self,
        post_json: dict=None,
        _parameters: dict=None,
        *args, **kwargs
    ):
        """

        """
        try:
            resp = post(
                url="http://engine:8000/engine_call",
                json=post_json).json()
        except Exception as e:
            resp = {"Engine Exception": f"{e}"}

        return resp

    def __call__(
        self,
        _request: flask.request,
        parameters: dict = None,
        *args, **kwargs
    ):
        """

        """
        if parameters is None:
            # Fetch Parameters
            # TODO Create Abstraction to Pull Remote Parameters
            pass
        print("Calling Ferry")

        request = _request.form.to_dict(flat=False)

        resp = self._send_to_engine(
            post_json=request,
            _parameters=parameters
        )

        return {
            "engine_response": resp,
            "engine_request": request
        }

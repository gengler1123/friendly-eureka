import flask
from requests import post


class Carburetor:
    """

    """

    def __init__(
            self,
            engine_endpoint: str = None,
            *args, **kwargs
    ):
        """

        """
        if engine_endpoint is None:
            self.engine_endpoint = "http://engine:8000/engine_call"
        else:
            self.engine_endpoint = engine_endpoint

    def _send_to_engine(
        self,
        post_json: dict = None,
        _parameters: dict = None,
        *args, **kwargs
    ):
        """

        """
        try:
            resp = post(
                url=self.engine_endpoint,
                json=post_json
            ).json()
        except Exception as e:
            resp = {"Engine Exception": f"{e}"}
        return resp

    def __call__(
        self,
        _request: flask.request,
        parameters: dict = None,
        *args, **kwargs
    ) -> dict:
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

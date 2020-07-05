import flask


class Engine:
    """

    """
    def __init__(self):
        """

        """

    def __call__(
        self,
        _request: flask.request,
        *args, **kwargs
    ) -> dict:
        """

        """
        incoming_json = _request.get_json()
        return {
            "engine_incoming_json": incoming_json,
            "response_text": "Generic Response Text"
        }

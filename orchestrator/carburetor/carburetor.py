import flask


class Carburetor:
    """

    """

    def __init__(self):
        """

        """

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

        return request

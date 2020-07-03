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
        *args, **kwargs
    ):
        """

        """
        print("Calling Ferry")

        request = _request.form.to_dict(flat=False)

        return request

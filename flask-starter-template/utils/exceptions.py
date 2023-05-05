from http.client import HTTPException


class BaseAPIError(HTTPException):
    """
    API Errors are used when a json response should be returned to the client
    """
    def __init__(self, message='Unknown Error'):
        self.message = message
        self.code = None
        self.args = (self.code, message)


class BadRequestAPIException(BaseAPIError):
    def __init__(self, message='Bad Request'):
        self.message = message
        self.code = 400
        self.args = (self.code, self.message)


class UnauthorizedAPIException(BaseAPIError):
    def __init__(self, message='Unauthorized'):
        self.message = message
        self.code = 401
        self.args = (self.code, self.message)


class InternalServerAPIException(BaseAPIError):
    def __init__(self, message='Internal Server Error'):
        self.message = message
        self.code = 500
        self.args = (self.code, self.message)

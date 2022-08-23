class APIException(Exception):

    def __init__(self, message, status_code, payload):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = 'error'
        return rv


class NotFoundException(APIException):

    def __init__(self, message='Not Found.', payload=None):
        super().__init__(message=message, status_code=404, payload=payload)


class InvalidPayload(APIException):

    def __init__(self, message='Not Found.', payload=None):
        super().__init__(message=message, status_code=404, payload=payload)

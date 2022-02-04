
class SelfHostBadRequestException(Exception):
    def __init__(self, message='Bad Request'):
        self.message = message


class SelfHostUnauthorizedException(Exception):
    def __init__(self, message='Unauthorized'):
        self.message = message


class SelfHostForbiddenException(Exception):
    def __init__(self, message='Forbidden'):
        self.message = message


class SelfHostNotFoundException(Exception):
    def __init__(self, message='Not Found'):
        self.message = message


class SelfHostMethodNotAllowedException(Exception):
    def __init__(self, message='Method Not Allowed'):
        self.message = message


class SelfHostConflictException(Exception):
    def __init__(self, message='Conflict'):
        self.message = message


class SelfHostTooManyRequestsException(Exception):
    def __init__(self, message='Too Many Requests'):
        self.message = message


class SelfHostInternalServerException(Exception):
    def __init__(self, message='Internal Server Error'):
        self.message = message


class SelfHostFatalErrorException(Exception):
    def __init__(self, message='A fatal error occurred'):
        self.message = message

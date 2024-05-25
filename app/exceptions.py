from fastapi import HTTPException, status


class Exceptions(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExists(Exceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class IncorrectLogin(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect username or password"


class TokenExpired(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired"


class TokenAbsent(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token absent"


class IncorrectToken(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Token"


class IncorrectUser(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED

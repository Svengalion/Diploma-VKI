from fastapi import HTTPException, status


class BookingException(HTTPException):
    status = 500
    detail = ""

    def __init__(self):
        super.__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExists(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class IncorrectLogin(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect username or password"


class TokenExpired(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired"


class TokenAbsent(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token absent"


class IncorrectToken(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Token"


class IncorrectUser(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED

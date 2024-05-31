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


class IncorrectLection(Exceptions):
    status_code = status.HTTP_204_NO_CONTENT
    detail = "Lection does not exist"


class IncorrectTest(Exceptions):
    status_code = status.HTTP_204_NO_CONTENT
    detail = "Test does not exist"


class AvatarNotFound(Exceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Avatar not found"


class QuestionNotFound(Exceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Question not found"


class AnswerNotFound(Exceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Answer not found"


class TestNotFound(Exceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Test not found"


class ResultsNotFound(Exceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Result not found"

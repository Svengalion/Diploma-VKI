from app.models import Lection, Test

from app.dao.base import BaseDAO


class TestDAO(BaseDAO):
    model = Test


class LectionDAO(BaseDAO):
    model = Lection
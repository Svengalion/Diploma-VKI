from app.src.models import Lection

from app.src.dao.base import BaseDAO


class LectionDAO(BaseDAO):
    model = Lection
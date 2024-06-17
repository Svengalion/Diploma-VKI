from app.src.models import Feedback

from app.src.dao.base import BaseDAO


class FeedbackDAO(BaseDAO):
    model = Feedback

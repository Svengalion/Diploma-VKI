from app.src.models import Course

from app.src.dao.base import BaseDAO


class CourseDAO(BaseDAO):
    model = Course

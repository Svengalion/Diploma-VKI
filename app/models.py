from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    number = Column(Integer)
    group = Column(String)

    # Relationships
    courses = relationship('Student_in_course', backref='student')

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationships
    lections = relationship('Lection', backref='course')
    students = relationship('Student_in_course', backref='course')
    tests = relationship('Test', backref='course')
    questions = relationship('Question', backref='course')

class Lection(Base):
    __tablename__ = 'lection'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))

class Student_in_course(Base):
    __tablename__ = 'student_in_course'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('user.id'))
    course_id = Column(Integer, ForeignKey('course.id'))

    # Relationships
    tasks = relationship('Task', backref='student_in_course')

class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    student_in_course_id = Column(Integer, ForeignKey('student_in_course.id'))
    result = Column(Integer)

class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    title = Column(String)

    # Relationships
    answers = relationship('Answer_to_question', backref='question')

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    answer = Column(String)

    # Relationships
    answers_to_question = relationship('Answer_to_question', backref='answer')

class Answer_to_question(Base):
    __tablename__ = 'answer_to_question'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    answer_id = Column(Integer, ForeignKey('answer.id'))
    right_answer_id = Column(Integer)


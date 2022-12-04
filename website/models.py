from . import db
from flask_login import UserMixin

# create database model here

# models the courses model


class Course(db.Model, UserMixin):
    idcourses = db.Column(db.Integer, primary_key=True)
    courseTitle = db.Column(db.String(25))
    courseDes = db.Column(db.String(150))
    courseLink = db.Column(db.String(150))
    courseFeedback = db.Column(db.String(150))
    courseTime = db.Column(db.String(30))
    startDate = db.Column(db.String(15))
    endDate = db.Column(db.String(15))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user'))
    employees = db.relationship('employeeCourse')
    questions = db.relationship('Question')
    answers = db.relationship('Answer')

# models the junction-table for employees and courses


class employeeCourse(db.Model, UserMixin):
    employee_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', name='fk_employee'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.idcourses', name='fk_course'), primary_key=True)
    manager_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', name='fk_course1'), primary_key=True)
    answer = db.Column(db.String(150))
    feedback = db.Column(db.String(150))
    progress = db.Column(db.Float(11))
# models the quesions table


class Question(db.Model, UserMixin):
    questionId = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(150))
    maxPoints = db.Column(db.Integer)
    link = db.Column(db.String(150))
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.idcourses', name='fk_course2'), primary_key=True)
    answers = db.relationship('Answer')

# models the junction-table for employee courses and questions


class Answer(db.Model, UserMixin):
    answer = db.Column(db.String(150))
    points = db.Column(db.Integer)
    feedback = db.Column(db.String(150))
    employee_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', name='fk_employee1'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.idcourses', name='fk_course1'), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.questionId', name='fk_question'), primary_key=True)


# models the users table

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    isManager = db.Column(db.String(1))
    isSupManager = db.Column(db.String(1))
    manager_id = db.Column(
        db.Integer, db.ForeignKey('user.id', name='fk_mngr'))
    employees = db.relationship('User')
    courses = db.relationship('Course')
    manager_courses = db.relationship(
        'employeeCourse', foreign_keys='employeeCourse.manager_id')
    employee_courses = db.relationship(
        'employeeCourse', foreign_keys='employeeCourse.employee_id')
    eAnswer = db.relationship('Answer')

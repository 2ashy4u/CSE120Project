from . import db
from flask_login import UserMixin

# create database model here

# models the courses model


class Course(db.Model, UserMixin):
    idcourses = db.Column(db.Integer, primary_key=True)
    courseTitle = db.Column(db.String(25))
    courseQues = db.Column(db.String(150))
    courseLink = db.Column(db.String(150))
    courseFeedback = db.Column(db.String(150))
    courseTime = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user'))

# models the users table


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    employeeID = db.Column(db.String(12))
    isManager = db.Column(db.String(1))
    isSupManager = db.Column(db.String(1))
    courses = db.relationship('Course')

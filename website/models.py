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
    courseTime = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user'))
    employees = db.relationship('Employee_Course')

# models the manager

class Manager(db.Model, UserMixin):
    manager_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user1'))
    employees = db.relationship('Employee')

# models the employee table

class Employee(db.Model, UserMixin):
    employee_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user2'))
    manager_id = db.Column(db.Integer, db.ForeignKey('manager.manager_id', name='fk_manager'))
    courses = db.relationship('Employee_Course')

# models the junction-table for employees and courses

class Employee_Course(db.Model, UserMixin):
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id', name='fk_employee'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.idcourses', name='fk_course'), primary_key=True)
    courseAnswer = db.Column(db.String(150))

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
    manager = db.relationship('Manager')
    employee = db.relationship('Employee')

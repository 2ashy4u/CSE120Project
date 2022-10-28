from . import db
from flask_login import UserMixin

# create database model here


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    employeeID = db.Column(db.String(12))
    isManager = db.Column(db.String(1))
    isSupManager = db.Column(db.String(1))

    # additions: manager attribute

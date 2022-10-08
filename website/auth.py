from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)
#route to login page
@auth.route('/login')
def login():
    return render_template("login.html")
#route to logout page
@auth.route('/manager')
def logout():
    return render_template("manager.html")
@auth.route('/home')
def home():
    return render_template("home.html")


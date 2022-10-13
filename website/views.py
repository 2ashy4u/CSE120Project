from flask import Blueprint, render_template

views = Blueprint('views', __name__)
#route to home page
@views.route('/')
def home():
    return render_template("landingPage.html")
    
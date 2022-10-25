from flask import Blueprint, render_template
from flask_login import current_user

views = Blueprint('views', __name__)
#route to home page
@views.route('/')
def home():
    return render_template("landingPage.html", user=current_user)
    
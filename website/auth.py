from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)
#routes to different pages
@auth.route('/Welcome')
def land():
    return render_template("landingPage.html")

@auth.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password=request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in successfully', category = 'success')
                login_user(user, remember=True)
                return redirect(url_for('auth.manager'))
            else:
                flash('Wrong password', category = 'error')
        else:
            flash('Wrong email', category = 'error')
    return render_template("login.html", user=current_user)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/Home')
def home():
    return render_template("home.html", user=current_user)

@auth.route('/Manager')
@login_required
def manager():
    return render_template("manager.html", user=current_user)

@auth.route('/Quiz')
@login_required
def quiz():
    return render_template("quiz.html", user=current_user)


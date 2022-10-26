from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)
#routes to different pages
@auth.route('/Welcome')
def land():
    return render_template("landingPage.html")

@auth.route('/Login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/Home')
def home():
    return render_template("home.html")

@auth.route('/Manager')
def manager():
    return render_template("manager.html")

@auth.route('/Quiz')
def quiz():
    return render_template("quiz.html")

@auth.route('/AddQuiz')
def addQuiz():
    return render_template("addQuiz.html")
    
@auth.route('/SignUp', methods=['GET', 'POST'])
#This is the post method to store information to database
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        else:
            #add user to database
            flash('Account created', category='success')
    return render_template("sign_up.html")


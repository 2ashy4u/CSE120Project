from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Course, employeeCourse
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
#from flask_security import roles_required
now = datetime.now()


auth = Blueprint('auth', __name__)
# routes to different pages


@auth.route('/Welcome')
def land():
    return render_template("landingPage.html")


@auth.route('/Login', methods=['GET', 'POST'])
def login():
    # recieves GET and POST data
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user, remember=True)
                if user.isManager == 'N':
                    return redirect(url_for('auth.home'))
                else:
                    return redirect(url_for('auth.manager'))
            else:
                flash('Wrong password!', category='error')
                return render_template('login.html')
        else:
            flash('Wrong email!', category='error')
            return render_template('login.html')
    return render_template("login.html", user=current_user)


@auth.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/Home')
@login_required
def home():
    return render_template("home.html", user=current_user)


@auth.route('/Manager')
@login_required
# @roles_required("Manager")
def manager():
    return render_template("manager.html", user=current_user)


@auth.route('/CoursesOverview')
@login_required
def coursesOverview():
    return render_template("coursesOverview.html", user=current_user)


@auth.route('/AddCourses', methods=['GET', 'POST'])
@login_required
def addCourse():
    if request.method == 'POST':
        courseQues = request.form.get('courseQues')
        courseLink = request.form.get('courseLink')
        # First gets all the checkboxes for employees
        employeeAssigned = request.form.getlist('employee')
        # Converts the check boxes from string to integers with a for loop
        convertListToInt = [eval(i) for i in employeeAssigned]

        courseTitle = request.form.get('courseTitle')
        if len(courseTitle) < 1:
            flash("Course Title was not entered!", category='error')
        elif len(courseQues) < 1:
            flash("Course Question was not entered!", category='error')
        else:
            newcourse = Course(courseQues=courseQues, courseTime=now,
                               user_id=current_user.id, courseLink=courseLink, courseTitle=courseTitle)
            # adds the course and flush keeps the value
            db.session.add(newcourse)
            # retains newCourse.id
            db.session.flush()
            # for loop to add employee ids assigned
            for x in convertListToInt:
                newEC = employeeCourse(
                    employee_id=x, course_id=newcourse.idcourses, manager_id=current_user.id)
                db.session.add(newEC)
            db.session.commit()  # <---- commits to the database
            flash("Course was added successfully!", category="success")
    return render_template("addCourse.html", user=current_user)


@auth.route('/CourseTest')
@login_required
def courseTest():
    return render_template("courseTest.html", user=current_user)

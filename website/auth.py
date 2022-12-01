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
    return render_template("home.html", user=current_user, _course = Course)


@auth.route('/Manager')
@login_required
# @roles_required("Manager")
def manager():
    return render_template("manager.html", user=current_user,  _employee_course=employeeCourse)


@auth.route('/Employees')
@login_required
def coursesOverview():
    return render_template("employees.html", user=current_user, _course = Course)


@auth.route('/AddCourses', methods=['GET', 'POST'])
@login_required
def addCourse():
    if request.method == 'POST':
        courseQues = request.form.get('courseQues')
        courseLink = request.form.get('courseLink')
        # First gets all the checkboxes for employees
        employeeAssigned = request.form.getlist('employee')
        print(employeeAssigned)
        # Converts the check boxes from string to integers with a for loop
        convertListToInt = [eval(i) for i in employeeAssigned]
        print(convertListToInt)
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
                print("x",x)
                newEC = employeeCourse(
                    employee_id=x, course_id=newcourse.idcourses, manager_id=current_user.id)
                db.session.add(newEC)
            db.session.commit()  # <---- commits to the database
            flash("Course was added successfully!", category="success")
    return render_template("addCourse.html", user=current_user)


# the route has id parameter because will create a unique page to each employee by their id with the same courseTest.html 
@auth.route('/CourseTest/id=<id>', methods=['GET', 'POST'])
@login_required
def courseTest(id):
    if request.method == 'POST':
        answer = request.form.get("answerText")
        print(answer)
        if len(answer) < 1:
            flash("Answer was not entered!", category='error')
        else:
            # store the employee answer in the employeeCourse table of the database
            # put in the row that matches to the course_id, and employee_id
            EC = employeeCourse.query.filter_by(course_id=id, employee_id=current_user.id).first()
            # put the column answer in the EC table to the answer from the user input 
            EC.answer = answer
            #db.session.flush()
            db.session.commit() 
            flash("Answer was submited successfully!", category="success")  
    # _course in render_templete in order to use Course table in the courseTest.html 
    # we also need the id since we have to pass this id to each employee page 
    return render_template("courseTest.html", user=current_user, _course=Course, id=id)


@auth.route('/Feedback/e_id=<idForEmp>,c_id=<idForCourse>', methods=['GET', 'POST'])
@login_required
def feedback(idForEmp,idForCourse):
    EC = employeeCourse.query.filter_by(course_id=idForCourse, employee_id=idForEmp).first()
    if request.method == 'POST':
        feedback = request.form.get("feedbackText")
        print(feedback)
        grade = request.form.get("gradeNumber")
        print(grade)
        if len(feedback) < 1:
            flash("Feedback was not entered!", category='error')
        else:
            EC_feedback = employeeCourse.query.filter_by(course_id=idForCourse, employee_id=idForEmp).first()
            EC_feedback.feedback = feedback
            EC_feedback.grade = grade
            db.session.flush()
            db.session.commit() 
            flash("Feedback was submited successfully!", category="success")  
    return render_template("manager_feedback.html", user=current_user, idForCourse=idForCourse, idForEmp=idForEmp, EC=EC)

@auth.route('/ViewFeedback/c_id=<idForCourse>')
@login_required
def viewFeedback(idForCourse):
    EC = employeeCourse.query.filter_by(course_id=idForCourse).first()
    return render_template("viewFeedback.html", user=current_user, idForCourse=idForCourse, EC=EC)


@auth.route('/UpdateCourse/c_id=<idForCourse>', methods=['GET', 'POST'])
@login_required
def update(idForCourse):
    # assigned a var to the Course table in the database so that we can update or replace the old data
    course_update = Course.query.filter_by(user_id=current_user.id,idcourses=idForCourse).first()
    # assigned a var to the employeeCourse table in the database so that we can update the assigned employee 
    employee_update = employeeCourse.query.filter_by(course_id=idForCourse).first()
    if request.method == "POST":
        course_update.courseTitle = request.form.get("updateCourseTitle")
        course_update.courseQues = request.form.get("updateCourseQues")
        course_update.courseLink = request.form.get("updateCourseLink")
        employee_update.updateEmployeeAssigned = request.form.getlist('updateEmployee')
        # same as the AddCourse functionality, add additional employee to the employeeCourse with a interger list 
        convertListToInt = [eval(i) for i in employee_update.updateEmployeeAssigned]
        print(convertListToInt)
        for x in convertListToInt:
            print("x",x)
            newEC = employeeCourse(employee_id=x, course_id=idForCourse, manager_id=current_user.id)
            db.session.merge(newEC)
        db.session.commit()
        flash("Update was submited successfully!", category="success")          
    return render_template("update_course.html", eC=employeeCourse, user=current_user, idForCourse=idForCourse, _course_update=course_update)


@auth.route('/Delete/c_id=<idForCourse>', methods=['GET', 'POST'])
@login_required
def delete(idForCourse):
    # delete all the row that matches with the manager_id and course_id in the employeeCourse and Course table in the database 
    employeeCourse.query.filter_by(course_id=idForCourse).delete()
    Course.query.filter_by(user_id=current_user.id, idcourses=idForCourse).delete()
    db.session.commit()
    flash("Successfully delete course")
    return render_template("manager.html",user=current_user,idForCourse=idForCourse,_employee_course=employeeCourse)

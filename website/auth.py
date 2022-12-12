from flask import Blueprint, render_template, request, flash, redirect, url_for, Markup
from .models import User, Course, employeeCourse, Question, Answer
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime, date
#from flask_security import roles_required
now = datetime.now()
today = date.today()
td = today.strftime("%Y-%m-%d")
print(td)
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
    numOfAnswer = 0
    totalAnswer = 0
    for answers in Answer.query.all():
        totalAnswer +=1
        if answers.answer:
            numOfAnswer += 1
    print(numOfAnswer)
    print(totalAnswer)
    return render_template("home.html", user=current_user, _course=Course, _answer=Answer, todayDate=td, totalAnswer=totalAnswer,numOfAnswer=numOfAnswer)


@auth.route('/Manager')
@login_required
# @roles_required("Manager")
def manager():
    return render_template("manager.html", user=current_user,  _employee_course=employeeCourse)


@auth.route('/Employees')
@login_required
def coursesOverview():
    # employee = User.query.filter_by(manager_id=current_user.id).first()
    completed = 0  
    incompelete = 0
    totalCourse = 0
    totalManager = 0
    for e in current_user.employees:
        totalManager +=1
    # find all the course with that specific manager id 
    for course in current_user.courses:
        print(course)
        # access to the employeeCourse database with that manager id 
        for employee in current_user.employees:
            boo = 1
            # access the answer table with that employee id and manager id 
            for answer in Answer.query.filter_by(employee_id=employee.id,course_id=course.idcourses):
                totalCourse +=1
                if not answer.answer:
                    # print(answer.answer)
                    boo = 0
                    incompelete +=1
                    break
                completed += boo
    print("totalCourse", totalCourse)
    print("complete", completed)
    print("incomplete", incompelete)
    return render_template("employees.html", user=current_user, _course=Course, completed=completed, totalCourse=totalCourse, incompelete=incompelete, totalManager=totalManager)


@auth.route('/AddCourses', methods=['GET', 'POST'])
@login_required
def addCourse():
    if request.method == 'POST':
        courseDes = request.form.get('courseDes')
        courseLink = request.form.get('courseLink')
        startDate = request.form.get('start')
        endDate = request.form.get('end')
        # First gets all the checkboxes for employees
        employeeAssigned = request.form.getlist('employee')
        # Converts the check boxes from string to integers with a for loop
        convertListToInt = [eval(i) for i in employeeAssigned]

        courseTitle = request.form.get('courseTitle')
        if len(courseTitle) < 1:
            flash("Course Title was not entered!", category='error')
        elif len(courseDes) < 1:
            flash("Course Question was not entered!", category='error')
        elif (startDate > endDate):
            flash("Dates entered incorrectly!", category='error')
        else:
            newcourse = Course(courseDes=courseDes, courseTime=now,
                               user_id=current_user.id, courseLink=courseLink, courseTitle=courseTitle, startDate=startDate, endDate=endDate)
            # adds the course and flush keeps the value
            db.session.add(newcourse)
            # retains newCourse.id
            db.session.flush()
            # for loop to add employee ids assigned
            for x in convertListToInt:
                newEC = employeeCourse(
                    employee_id=x, course_id=newcourse.idcourses, manager_id=current_user.id, progress=0)
                db.session.add(newEC)
                db.session.commit()  # <---- commits to the database
            flash(Markup(
                'Course sucessfully made!, please click <a href="/Manager" class="alert-link">here</a> to add questions!'), category='success')
    return render_template("addCourse.html", user=current_user, todayDate=today)


# the route has id parameter because will create a unique page to each employee by their id with the same courseTest.html
@auth.route('/CourseTest/id=<id>', methods=['GET', 'POST'])
@login_required
def courseTest(id):
    mCourse = Course.query.filter_by(idcourses=id).first()
    if request.method == 'POST':
        see = 'see'
        boo = 1
        answer = request.form.getlist("answerText")
        qid = []
        x = 0
        for j in mCourse.questions:
            qid.append(j.questionId)
        if qid[0]:
            see = qid[0]
        for i in answer:
            if len(i) < 1:
                flash("Answer was not entered!", category='error')
                boo = 0
                break
            else:
                # store the employee answer in the employeeCourse table of the database
                # put in the row that matches to the course_id, question_id, and employee_id
                #EC = employeeCourse.query.filter_by(course_id=id, employee_id=current_user.id).first()
                ans = Answer.query.filter_by(
                    employee_id=current_user.id, course_id=id, question_id=qid[x]).first()
                if not ans:
                    # check to see if the answer row exists (it theoretically should always exist)
                    see = id
                    flash("Answer doesn't exist!", category='error')
                    boo = 0
                    break
                else:
                    # put the column answer in the EC table to the answer from the user input
                    #EC.answer = answer
                    ans.answer = i
                # db.session.flush()
            x += 1
        if boo == 1:
            db.session.commit()
            flash("Answer was submited successfully!", category="success")
    # _course in render_templete in order to use Course table in the courseTest.html
    # we also need the id since we have to pass this id to each employee page
    return render_template("courseTest.html", user=current_user, _course=Course, id=id, mCourse=mCourse, ans=Answer)


@auth.route('/Feedback/e_id=<idForEmp>,c_id=<idForCourse>', methods=['GET', 'POST'])
@login_required
def feedback(idForEmp, idForCourse):
    EC = employeeCourse.query.filter_by(
        course_id=idForCourse, employee_id=idForEmp).first()
    employee = User.query.filter_by(id=idForEmp).first()
    mCourse = Course.query.filter_by(idcourses=idForCourse).first()
    if request.method == 'POST':
        feedback = request.form.getlist("feedbackText")
        points = request.form.getlist("pointText")
        boo = 1
        qid = []
        x = 0
        isInt = 1
        for j in mCourse.questions:
            qid.append(j.questionId)
        for i in feedback:
            if len(points[x]) < 1:
                points[x] = 0
            try:
                points[x] = int(points[x])
            except ValueError:
                isInt = 0
            if len(i) < 1:
                boo = 0
                flash("Feedback was not entered!", category='error')
                break
            elif isInt == 0:
                boo = 0
                flash("Points have to be integers!", category='error')
                break
            elif int(points[x]) < 0:
                boo = 0
                flash("Points can't be negative!", category='error')
                break
            else:
                ans_feedback = Answer.query.filter_by(
                    question_id=qid[x], employee_id=idForEmp).first()
                ans_feedback.feedback = i
                ans_feedback.points = points[x]
                # db.session.flush()
            x += 1
        givenPoints = 0
        totalPoints = 0
        i = 0
        if boo == 1:
            db.session.commit()

            # calculate total course progress for employee
            for q in mCourse.questions:
                if not Answer.query.filter_by(question_id=q.questionId).first().points:
                    Answer.query.filter_by(question_id=q.questionId).first().points = 0
                totalPoints += int(q.maxPoints)
                givenPoints += int(Answer.query.filter_by(
                    question_id=q.questionId).first().points)
            if not totalPoints == 0:
                # max course progress should be 100%
                if givenPoints > totalPoints:
                    EC.progress = 100
                else:
                    EC.progress = (givenPoints/totalPoints)*100
            # if the max points are 0, progress is automatically 100%
            else:
                EC.progress = 100
            db.session.commit()
            flash("Feedback submitted!", category="success")
    return render_template("manager_feedback.html", user=current_user, idForCourse=idForCourse, idForEmp=idForEmp, EC=EC,
                           course=Course.query.filter_by(idcourses=idForCourse).first(), _answer=Answer, employee=employee)


@auth.route('/ViewFeedback/c_id=<idForCourse>')
@login_required
def viewFeedback(idForCourse):
    EC = employeeCourse.query.filter_by(course_id=idForCourse).first()
    course = Course.query.filter_by(idcourses=idForCourse).first()
    return render_template("viewFeedback.html", user=current_user, idForCourse=idForCourse, EC=EC, course=course, _answer=Answer)


@auth.route('/UpdateCourse/c_id=<idForCourse>', methods=['GET', 'POST'])
@login_required
def update(idForCourse):
    # assigned a var to the Course table in the database so that we can update or replace the old data
    course_update = Course.query.filter_by(
        user_id=current_user.id, idcourses=idForCourse).first()
    # assigned a var to the employeeCourse table in the database so that we can update the assigned employee
    employee_update = employeeCourse.query.filter_by(
        course_id=idForCourse).first()
    if request.method == "POST":
        course_update.courseTitle = request.form.get("updateCourseTitle")
        course_update.courseDes = request.form.get("updateCourseDes")
        course_update.courseLink = request.form.get("updateCourseLink")
        course_update.startDate = request.form.get('start')
        course_update.endDate = request.form.get('end')
        updateEmployeeAssigned = request.form.getlist('updateEmployee')
        # print( employee_update.updateEmployeeAssigned )
        # same as the AddCourse functionality, add additional employee to the employeeCourse with a interger list
        convertListToInt = [eval(i) for i in updateEmployeeAssigned]
        # if the manager does not add anyone flash the error alert
        if convertListToInt == []:
            print("error is here")
            flash("Add the employee in the course!", category="error")
            return render_template("update_course.html", eC=employeeCourse, user=current_user, idForCourse=idForCourse, _course_update=course_update, progress=0)
        for x in convertListToInt:
            newEC = employeeCourse(
                employee_id=x, course_id=idForCourse, manager_id=current_user.id)
            # merge is use to add the same employee again without any error
            db.session.merge(newEC)
        # current_user.employees is access the employee in that manager
        for employee in current_user.employees:
            # initialize to set user does not exist
            y = 0
            for x in convertListToInt:
                # if the employee exist in the list
                if employee.id == x:
                    # then user is set to 1
                    y = 1
            # this will not run if the employee is in the list
            # and statement is to make sure it delete the row that exist in the database
            # and Answer.query.filter_by(course_id=idForCourse, employee_id=employee.id).first()
            if y == 0 and employeeCourse.query.filter_by(course_id=idForCourse, employee_id=employee.id).first():
                Answer.query.filter_by(
                    course_id=idForCourse, employee_id=employee.id).delete()
                employeeCourse.query.filter_by(
                    course_id=idForCourse, employee_id=employee.id).delete()
        # for each question in the course database that related to the questions database
        # we can call .questions because we set the relation in the models.py
        for question in Course.query.filter_by(idcourses=idForCourse).first().questions:
            for employee in current_user.employees:
                # if the answer is not in that employee yet
                if not Answer.query.filter_by(course_id=idForCourse, employee_id=employee.id, question_id=question.questionId).first() and employeeCourse.query.filter_by(employee_id=employee.id, course_id=idForCourse).first():
                    # add the new row of that answer
                    initAnswer = Answer(
                        employee_id=employee.id, course_id=idForCourse, question_id=question.questionId)
                    db.session.add(initAnswer)
        db.session.commit()
        flash("Update was submited successfully!", category="success")
    return render_template("update_course.html", eC=employeeCourse, user=current_user, idForCourse=idForCourse, _course_update=course_update)


@auth.route('/Delete/c_id=<idForCourse>', methods=['GET', 'POST'])
@login_required
def delete(idForCourse):
    # delete all the row that matches with the manager_id and course_id in the employeeCourse and Course table in the database
    Answer.query.filter_by(course_id=idForCourse).delete()
    Question.query.filter_by(course_id=idForCourse).delete()
    employeeCourse.query.filter_by(
        manager_id=current_user.id, course_id=idForCourse).delete()
    Course.query.filter_by(user_id=current_user.id,
                           idcourses=idForCourse).delete()
    db.session.commit()
    flash("Successfully delete course")
    return render_template("manager.html", user=current_user, idForCourse=idForCourse, _employee_course=employeeCourse)


@auth.route('/ProgressPieChart/c_id=<cid>', methods=['GET', 'POST'])
def progressPieChart(cid):
    course = Course.query.filter_by(idcourses=cid).first()
    completed = 0
    incompleted = 0
    totalCourse = 0
    print("cid",cid)

    # access the answer table with that employee id and manager id 
    for answer in Answer.query.filter_by(course_id=cid):
        print(answer.answer)
        totalCourse+=1
        if answer.answer:
            # print(answer.answer)
            completed +=1
        else:
            incompleted +=1
        # completed += boo
    print("totalCourse", totalCourse)
    print("complete", completed)
    print("incomplete",incompleted)
    return render_template("progressPieChart.html", cid=cid, user=current_user,course=course, totalCourse=totalCourse, completed=completed)


@auth.route('/EmployeeList/m_id=<mid>', methods=['GET', 'POST'])
def employeeList(mid):
    print(mid)
    manager = User.query.filter_by(id=mid).first()
    totalEmployee = 0
    for e in manager.employees:
        totalEmployee +=1
    return render_template("employeeList.html", user=current_user, mid=mid, manager=manager, totalEmployee=totalEmployee)
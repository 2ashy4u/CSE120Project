from flask_login import current_user, login_required
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User, Course, employeeCourse, Question, Answer
from . import db
import json

views = Blueprint('views', __name__)
# route to home page


@views.route('/')
def home():
    return render_template("landingPage.html", user=current_user)


@views.route('/UpdateCourse/id=<cid>/Questions', methods=['GET', 'POST'])
def addQuestions(cid):
    course = Course.query.filter_by(
        user_id=current_user.id, idcourses=cid).first()
    see = 0
    if request.method == "POST":
        question = request.form.get('question')
        points = request.form.get('points')
        link = request.form.get('link')
        isInt = 1
        try:
            points = int(points)
        except ValueError:
            isInt = 0
        if len(question) < 1:
            flash("Question was not entered!", category='error')
        elif not isInt == 1:
            flash("Maximum points has to be an integer!", category='error')
        elif int(points) < 0:
            flash("Maximum points can't be negative!", category='error')
        else:
            newquestion = Question(
                data=question, maxPoints=points, link=link, course_id=course.idcourses)  
            db.session.add(newquestion)
            db.session.commit()

            # flush wasn't working, so this line finds the last committed question to the course
            obj = db.session.query(Question).order_by(
                Question.questionId.desc()).filter_by(course_id=cid).first()
            for employee in current_user.employees:
                if employeeCourse.query.filter_by(employee_id=employee.id, course_id=cid).first():
                    initAnswer = Answer(
                        employee_id=employee.id, course_id=cid, question_id=obj.questionId)
                    db.session.add(initAnswer)
            db.session.commit()
            flash("Question added successfully!", category='success')
    return render_template("addQuestions.html", user=current_user, course=course)


@views.route('/Delete/q_id=<qid>', methods=['GET', 'POST'])
@login_required
def deleteQ(qid):
    # delete row with the question id
    quest = Question.query.filter_by(questionId=qid).first()
    cid = quest.course_id

    Answer.query.filter_by(question_id=qid).delete()
    Question.query.filter_by(questionId=qid).delete()
    db.session.commit()
    flash("Question deleted", category="success")
    return redirect(url_for("views.addQuestions", cid=cid))


@views.route('/Progress/e_id=<eid>', methods=['GET', 'POST'])
def progress(eid):
    employee = User.query.filter_by(id=eid).first()
    print(employee)
    completed = 0
    incompeleted = 0
    totalCourse = 0

    # access to the employeeCourse database with that employee id 
    # for e in current_user.employees:
    #     # print(employee)
    #     boo = 1
        # access the answer table with that employee id and manager id 
    for answer in Answer.query.filter_by(employee_id=eid):
        print(answer.answer)
        totalCourse +=1
        if answer.answer:
            # print(answer.answer)
            completed +=1
        else:
            incompeleted+=1

    print("totalCourse", totalCourse)
    print("complete", completed)
    print("incomplete",incompeleted)

    return render_template("progress.html", eid=eid, user=current_user, employee=employee, _employee_course=employeeCourse, completed=completed, totalCourse=totalCourse, incompeleted=incompeleted)

from flask import request, Blueprint, session
from flask import render_template, redirect, url_for, flash
from sqlalchemy import select

from app.models.base import db
from app.models.program import Program
from app.models.university import University

provideKnlgPointBP = Blueprint('provideKnlgPoint',__name__)
@provideKnlgPointBP.route("/provideKnlgPointInfo", methods=["GET","POST"])

def provideKnlgPointInfo():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('ProvideCourseNameList.html', name = name)
    if request.method == 'POST':
        knlg_universityName = request.form.get("universityName")
        knlg_programName = request.form.get("programName")
        knlg_courseList = request.form.get("courseList")

        # Finding university in the University database
        universities = University.query.filter(University.university_name == knlg_universityName).all()
        print(universities)
        if not universities:
            return '<script> alert("University not found.");window.location.replace("/provideKnlgPointInfo")</script>'

        # Finding program in the Program database
        programs = Program.query.filter(Program.program_name == knlg_programName).all()
        if not programs:
            return '<script> alert("Program not found.");window.location.replace("/provideKnlgPointInfo")</script>'

        # Correlation the program with University
        for program in programs:
            university = University.query.filter_by(university_id=program.provider_id).first()
            if university.university_name != knlg_universityName:
                return '<script> alert("The program is not provided in this university! ");window.location.replace("/provideKnlgPointInfo")</script>'
            else:
                if not knlg_courseList:
                    return '<script> alert("Courses Required should not be empty...");window.location.replace("/provideKnlgPointInfo")</script>'
                else:
                    program.courseList = knlg_courseList
                    print(program.courseList)
                    db.session.commit()
                    return '<script> alert("Success provide knowledge point.");window.location.replace("/provideKnlgPointInfo")</script>'
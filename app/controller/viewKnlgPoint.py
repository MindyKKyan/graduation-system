from flask import request, Blueprint, render_template, session
from app.models.university import University
from app.models.program import Program

viewKnlgPointBP = Blueprint('viewKnlgPoint', __name__)

@viewKnlgPointBP.route("/knlgPoint", methods=['GET', 'POST'])
def knlgPoint():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('KnowledgePointPage.html', name=name)
    else:
        program_name = request.form['program_name']
        print(program_name)

        # Search through the Program database
        program_knlg = Program.query.filter(Program.program_name.contains(program_name)).all()
        if not program_knlg:
            return '<script> alert("There is no information found! ");window.location.replace("/knlgPoint")</script>'
        else:
            knlgPs = []
            # Getting program information from taught offers
            for knlg in program_knlg:
                universities = University.query.filter_by(university_id=knlg.provider_id).all()
                for university in universities:
                    print(university)
                    knlgPs.append((university.university_name, knlg.program_name, knlg.courseList))

            print(knlgPs)

            return render_template('ProgramDisplay.html', knlgPs=knlgPs)


from flask import request, Blueprint, render_template, session
from app.models.program import Program
from app.models.university import University

searchAdmReqBP = Blueprint('searchAdmReq', __name__)

@searchAdmReqBP.route("/searchAdmReq", methods=['GET', 'POST'])
def searchAdmReq():
    if request.method == 'GET':
        name = session.get('name')


        return render_template('Search Admission Requirements.html', name = name)

@searchAdmReqBP.route("/searchThrGPA", methods=['GET', 'POST'])
def searchThrGPA():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('Search GPA.html', name=name)
    else:
        gpa_min = float(request.form['gpa_min'])
        gpa_max = float(request.form['gpa_max'])
        print(gpa_min, gpa_max)
        difference = gpa_max - gpa_min
        print(difference)
        if gpa_min < 0 or gpa_max < 0 or gpa_min > 3.8 or gpa_max > 4.0:
            return '<script> alert("In valid GPA range: GPA should be inside [0, 4.0]");window.location.replace("/searchThrGPA")</script>'
        if gpa_min >= gpa_max:
            return '<script> alert("The minimum GPA should not larger than the maximum GPA! ");window.location.replace("/searchThrGPA")</script>'

        elif difference < 0.1666:
            return '<script> alert("The differences between maximum GPA and minimum GPA should be larger than 0.2! ");window.location.replace("/searchThrGPA")</script>'

        else:
            programs = Program.query.filter(Program.gpa_low >= gpa_min, Program.gpa_up <= gpa_max).all()
            print(programs)
            if not programs:
                return '<script> alert("There is no information found! ");window.location.replace("/searchThrGPA")</script>'
            else:
                results = []
                for program in programs:
                    university = University.query.filter_by(university_id=program.provider_id).first()
                    results.append((program.program_name, university.university_name, program.gpa_low, program.gpa_up))
                print(results)
                return render_template('ProgramDisplay.html', results=results)

@searchAdmReqBP.route("/searchThrUName", methods=['GET', 'POST'])
def searchThrUName():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('Search by College or University.html', name=name)
    else:
        c_name = request.form.get('college_program')
        print(c_name)
        programs = Program.query.filter(Program.program_name.contains(c_name)).all()
        print(programs)
        if not programs:
            return '<script> alert("No information found"); window.location.replace("/searchThrUName")</script>'
        else:
            program_info = []
            for program in programs:
                university = University.query.filter_by(university_id=program.provider_id).first()
                program_info.append((university.university_name, program.program_name, program.gpa_low, program.gpa_up))
            print(program_info)
            return render_template("ProgramDisplay.html", program_info=program_info)

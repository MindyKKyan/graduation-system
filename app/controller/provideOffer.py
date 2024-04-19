from flask import request, Blueprint, session
from flask import render_template

from app.models.base import db
from app.models.program import Program
from app.models.researchOffer import ResearchOffer
from app.models.taughtOffer import TaughtOffer
from app.models.uicer import UICer
from app.models.university import University

provideOfferBP = Blueprint('provideOffer', __name__)


@provideOfferBP.route("/provideInfo", methods=["GET", "POST"])
def provideInfo():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('ProvideOfferInformation.html', name = name)
    else:
        name = session.get('name')
        select_value = request.form.get('Rtype')
        print(select_value)
        if select_value == '0':
            tdate = request.form.get("tdate")
            tgpa = request.form.get("tgpa")
            tuniversityName = request.form.get("tuniversityName")
            tprogramName = request.form.get("tprogramName")

            if (float(tgpa) < 0.0) or (float(tgpa) > 4.0):
                print("Invalid gpa input!")
                return '<script> alert("Invalid gpa input.");window.location.href("/provideInfo")</script>'
            print(tdate, tgpa, tuniversityName, tprogramName)

            # Finding university in the University database and allocate corresponding program
            university = University.query.filter(University.university_name == tuniversityName).first()
            if not university:
                return '<script> alert("The University is not exists!");window.location.replace("/provideInfo")</script>'

            program = Program.query.filter(Program.provider_id == university.university_id, Program.program_name == tprogramName).first()
            if not program:
                return '<script> alert("The University did not provide this program!");window.location.replace("/provideInfo")</script>'

            else:
                print(university)
                print(program)
                uicer = UICer.query.filter_by(name=name).first()
                print(uicer.role)
                if(uicer.role == 1):
                    taught = TaughtOffer(date=tdate, gpa=tgpa, universityName=tuniversityName, programName=tprogramName, towner=uicer)
                if(uicer.role == 2):
                    taught = TaughtOffer(date=tdate, gpa=tgpa, universityName=tuniversityName, programName=tprogramName, towner=uicer)

                # update the gpa range to the Program
                pg_min = min(float(program.gpa_low), float(tgpa))
                pg_max = max(float(program.gpa_up), float(tgpa))
                print(pg_min, pg_max)
                program.gpa_low = pg_min
                program.gpa_up = pg_max

                db.session.add(taught)
                db.session.commit()
                print("GPA updated!")
                print("Provide success.")
                return '<script> alert("Sucessfully provide taught offer.");window.location.replace("/provideInfo")</script>'

        else:
            # research offer providing
            rdate = request.form.get("rdate")
            rgpa = request.form.get("rgpa")
            runiversityName = request.form.get("runiversityName")
            rprogramName = request.form.get("rprogramName")
            supervisor = request.form.get("rsupervisor")
            researchTopic = request.form.get("researchTopic")
            noPapers = request.form.get("noPapers")
            noResearch = request.form.get("noResearch")
            ralumniName = request.form.get("ralumniName")

            if float(rgpa) < 0 or float(rgpa) > 4:
                print("Invalid gpa input!")
                return '<script> alert("Invalid gpa input!");window.location.replace("/provideInfo")</script>'
            print(rdate, rgpa, runiversityName, rprogramName, ralumniName, supervisor, researchTopic, noPapers,
                  noResearch, ralumniName)

            # Finding university in the University database
            university = University.query.filter(University.university_name == runiversityName).first()
            print(university)
            if not university:
                return '<script> alert("University not found.");window.location.replace("/provideInfo")</script>'

            # Finding program in the Program database
            programs = Program.query.filter(Program.program_name == rprogramName).all()
            if not programs:
                return '<script> alert("Program not found.");window.location.replace("/provideInfo")</script>'

            # Correlation the program with University
            for program in programs:
                university = University.query.filter_by(university_id=program.provider_id).first()
                if university.university_name != runiversityName:
                    return '<script> alert("The program is not provided in this university! ");window.location.replace("/provideInfo")</script>'


            if float(noPapers) < 0:
                print("Invalid noPapers input!")
                return '<script> alert("Invalid noPapers input!");window.location.replace("/provideInfo")</script>'
            if float(noResearch) < 0:
                print("Invalid noResearch input!")
                return '<script> alert("Invalid noResearch input!");window.location.replace("/provideInfo")</script>'
            else:
                uicer = UICer.query.filter_by(name=name).first()
                if (uicer.role == 1):
                    research = ResearchOffer(date=rdate, gpa=rgpa, reUniversityName=runiversityName,
                                         reProgramName=rprogramName, supervisor=supervisor, researchTopic=researchTopic,
                                         noPapers=noPapers, noResearch=noResearch, rowner=uicer)

                elif (uicer.role == 2):
                    research = ResearchOffer(date=rdate, gpa=rgpa, reUniversityName=runiversityName,
                                             reProgramName=rprogramName, supervisor=supervisor,
                                             researchTopic=researchTopic,
                                             noPapers=noPapers, noResearch=noResearch, rowner=uicer)
                else:
                    return '<script> alert("Invalid role! ");window.location.replace("/provideInfo")</script>'

                # update the gpa range to the Program
                pto_update = Program.query.filter(Program.program_name == rprogramName).first()
                pg_min = min(float(pto_update.gpa_low), float(rgpa))
                pg_max = max(float(pto_update.gpa_up), float(rgpa))
                print(pg_min, pg_max)
                pto_update.gpa_low = pg_min
                pto_update.gpa_up = pg_max

                db.session.add(research)
                db.session.commit()
                print("success.")
                return '<script> alert("Successfully provide research offer.");window.location.replace("/provideInfo")</script>'
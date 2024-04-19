from flask import request, Blueprint, render_template, session

from app.models.base import db
from app.models.companyOffer import CompanyOffer
from app.models.employmentExperience import EmploymentExperience
from app.models.uicer import UICer

shareEmpExpBP = Blueprint('shareEmpExp', __name__)


@shareEmpExpBP.route("/shareEmpExpInfo", methods=['GET', 'POST'])
def shareExperience():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('ShareEmpExp.html', name = name)
    else:
        date = request.form.get("EmpDate")
        emlpCompanyName = request.form.get("cpnName")
        emlpgpa = request.form.get("EmpGPA")
        title = request.form.get("EmpTitle")
        experience = request.form.get("Exp")
        name = session.get('name')

        if (float(emlpgpa) < 0.0) or (float(emlpgpa) > 4.0):
            print("Invalid gpa.")
            return '<script> alert("Invalid gpa.");window.location.replace("/shareEmpExpInfo")</script>'
        else:
            print(date, emlpCompanyName, emlpgpa, title, experience)

            company = CompanyOffer.query.filter_by(companyName=emlpCompanyName).first()
            if not company:
                print("Company not found.")
                return '<script> alert("Company not found.");window.location.replace("/shareEmpExpInfo")</script>'
            else:
                print(company)
                owner = UICer.query.filter(UICer.name == name).first()
                print(owner)
                company_offer = CompanyOffer(date=date, title=title, gpa=emlpgpa, companyName=emlpCompanyName, cowner=owner)
                emplExperience = EmploymentExperience(companyName=emlpCompanyName, experience=experience, holder=company)

                db.session.add(company_offer)
                db.session.add(emplExperience)
                db.session.commit()
                print("Sucessfully add the info to the database.")
                return '<script> alert("Success share employment experience.");window.location.replace("/shareEmpExpInfo")</script>'
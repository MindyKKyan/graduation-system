
import numpy as np


from flask import request, Blueprint, render_template, session, send_from_directory
from datetime import datetime

from matplotlib import pyplot as plt

from app.models.researchOffer import ResearchOffer
from app.models.taughtOffer import TaughtOffer

viewYearlyRepBP = Blueprint('viewYearlyRep', __name__)

@viewYearlyRepBP.route("/viewYrlRep", methods=['GET', 'POST'])
def viewYrlRep():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('ViewYearlyReport.html', name=name)
    else:
        year = request.form['year']
        print(year)
        start_date = datetime(int(year), 1, 1).date()
        end_date = datetime(int(year), 12, 31).date()
        print(start_date, end_date)

        research_offers = ResearchOffer.query.filter(ResearchOffer.date.between(start_date, end_date)).all()
        taught_offers = TaughtOffer.query.filter(TaughtOffer.date.between(start_date, end_date)).all()

        yearlRs = []
        for offer in research_offers:
            yearlR = {
                'university': offer.reUniversityName,
                'program': offer.reProgramName,
                'gpa': offer.gpa,
                'year': offer.date,
            }
            yearlRs.append(yearlR)

        for offer in taught_offers:
            yearlR = {
                'university': offer.universityName,
                'program': offer.programName,
                'gpa': offer.gpa,
                'year': offer.date,
            }
            yearlRs.append(yearlR)

        if yearlRs == []:
            return '<script> alert("No information found");window.location.replace("/viewYrlRep")</script>'
        else:
            # Extract university names and GPAs
            universities = [yr['university'] for yr in yearlRs]
            gpas = [yr['gpa'] for yr in yearlRs]

            # Set up the bar chart
            fig, ax = plt.subplots()
            x_pos = np.arange(len(universities))

            # Create the bar chart
            bars = ax.bar(x_pos, gpas, color='lightblue')

            # Customize the chart
            ax.set_xticks(x_pos)
            ax.set_xticklabels(universities, rotation='vertical')
            ax.set_xlabel('University')
            ax.set_ylabel('GPA')
            ax.set_title('Yearly Report - GPA by University')

            # Save the chart as an image file
            image_name = f"app/static/{year}.png"
            plt.savefig(image_name)
            image = f'{year}.png'
            return render_template('ProgramDisplay.html', yearlRs=yearlRs, image_name=image)


@viewYearlyRepBP.route('/download_chart/<filename>', methods=['GET'])
def download_chart(filename):
    return send_from_directory('static', filename, as_attachment=True)
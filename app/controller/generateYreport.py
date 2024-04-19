
from flask import request, Blueprint, render_template, session
from sqlalchemy import extract
from app.models.researchOffer import ResearchOffer
from app.models.taughtOffer import TaughtOffer

generateYreportBP = Blueprint('generateYreport', __name__)


@generateYreportBP.route("/generateYreport", methods=['GET', 'POST'])
def generateYreport():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('GenerateYearReport.html', name = name)
    else:
        year = request.form.get('year')
        if year is None:
            return '<script> alert("please input the year");window.location.replace("/generateYreport")</script>'

        research_offers = ResearchOffer.query.filter(extract('year', ResearchOffer.date) == year).all()
        # Get taught offers for the specified year
        taught_offers = TaughtOffer.query.filter(extract('year', TaughtOffer.date) == year).all()
        # Initialize an empty list to store the results
        results = []
        for research_offer in research_offers:
            result = {}
            result['university_name'] = research_offer.reUniversityName
            result['program_name'] = research_offer.reProgramName
            result['gpa'] = research_offer.gpa
            result['offer_type'] = 'Research'
            results.append(result)
        # Loop through the taught offers and add the relevant information to the results list
        for taught_offer in taught_offers:
            result = {}
            result['university_name'] = taught_offer.universityName
            result['program_name'] = taught_offer.programName
            result['gpa'] = taught_offer.gpa
            result['offer_type'] = 'Taught'
            results.append(result)
        # Render the template with the results
        print(results)

        import matplotlib.pyplot as plt

        # Extract university names and corresponding GPAs from the results
        universities = [result['university_name'] for result in results]
        gpas = [result['gpa'] for result in results]

        # Calculate the average GPA for each university
        university_avg_gpa = {}
        for university, gpa in zip(universities, gpas):
            if university not in university_avg_gpa:
                university_avg_gpa[university] = []
            university_avg_gpa[university].append(gpa)

        # Calculate the average GPA for each university
        avg_gpas = []
        for university in university_avg_gpa:
            avg_gpa = sum(university_avg_gpa[university]) / len(university_avg_gpa[university])
            avg_gpas.append(avg_gpa)

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(university_avg_gpa.keys(), avg_gpas)
        plt.xlabel('Universities')
        plt.ylabel('Average GPA')
        plt.title('Average GPA of Accepted Students by University')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot as an image file
        save_name = year + 'report.png'
        plt.savefig(save_name)

        # Display the plot
        return '<script> alert("yearly report generate success");window.location.replace("/generateYreport")</script>'
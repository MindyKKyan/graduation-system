from flask import request, Blueprint, render_template, session
from app.models.researchOffer import ResearchOffer
from app.models.taughtOffer import TaughtOffer
from app.models.university import University

viewOffertimeBP = Blueprint('viewOffertime', __name__)



@viewOffertimeBP.route("/viewOffertime", methods=['GET', 'POST'])
def viewOffertime():
    if request.method == 'GET':
        name = session.get('name')
        return render_template('ViewOfferTime.html', name=name)
    else:
        c_name = request.form.get('searchOffer')
        print(c_name)
        university = University.query.filter(University.university_name.contains(c_name)).all()
        print(university)
        if university is None:
            return '<script> alert("University not found!");window.location.replace("/viewOffertime")</script>'

        else:
            researchOffers = ResearchOffer.query.filter(ResearchOffer.reUniversityName.contains(c_name)).all()
            taughtOffers = TaughtOffer.query.filter(TaughtOffer.universityName.contains(c_name)).all()
            print(researchOffers)
            print(taughtOffers)
            if not researchOffers and not taughtOffers:
                return '<script> alert("No offer found!");window.location.replace("/viewOffertime")</script>'
            else:
                results = []
                if researchOffers:
                    offerType = 'Research Offer'
                    for offer in researchOffers:
                        results.append((offer.reUniversityName, offer.reProgramName, offer.date, offerType))

                if taughtOffers:
                    offerType = 'Taught Offer'
                    for offer in taughtOffers:
                        results.append((offer.universityName, offer.programName, offer.date, offerType))
                print(results)
                return render_template('OfferTimeDisplay.html', results=results)

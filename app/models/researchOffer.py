from sqlalchemy import Column, String, Integer

from app.models.base import db
from app.models.offer import Offer

class ResearchOffer(Offer):

    reUniversityName = Column(String(50))
    reProgramName = Column(String(50))
    supervisor = Column(String(50))
    researchTopic = Column(String(50))
    noPapers = Column(Integer)
    noResearch = Column(Integer)
    rowner_id = Column(Integer, db.ForeignKey('uicer.id'))

    def __init__(self, date, gpa, reUniversityName, reProgramName, supervisor, researchTopic, noPapers, noResearch, rowner):
        super(ResearchOffer, self).__init__(date, gpa)
        self.reUniversityName = reUniversityName
        self.reProgramName = reProgramName
        self.supervisor = supervisor
        self.researchTopic = researchTopic
        self.noPapers = noPapers
        self.noResearch = noResearch
        self.rowner = rowner

    def jsonstr(self):

        jsondata = {
            'date':self.date,
            'photocopy': self.photocopy,
            'gpa': self.gpa,
            'offer_type': self.offer_type,
            'supervisor': self.supervisor,
            'researchOfferName': self.researchOfferName,
            'researchTopic': self.researchTopic,
            'noPapers': self.noPapers,
            'noResearch': self.noResearch

        }

        return jsondata


from sqlalchemy import Column, String, Integer

from app.models.base import db
from app.models.offer import Offer

class TaughtOffer(Offer):

    universityName = Column(String(50))
    programName = Column(String(50))
    towner_id = Column(Integer, db.ForeignKey('uicer.id'))


    def __init__(self, date, gpa, universityName, programName, towner):
        super(TaughtOffer, self).__init__(date, gpa)
        self.universityName = universityName
        self.programName = programName
        self.towner = towner

    def jsonstr(self):

        jsondata = {
            'date':self.date,
            'photocopy': self.photocopy,
            'gpa': self.gpa,
            'offer_type': self.offer_type,
            'universityName': self.universityName,
            'programName': self.programName

        }

        return jsondata

from sqlalchemy import Column, String, Integer

from app.models.base import db
from app.models.offer import Offer

class CompanyOffer(Offer):
    __tablename__ = 'companyOffer'

    title = Column(String(50))
    companyName = Column(String(50))
    cowner_id = Column(Integer,db.ForeignKey('uicer.id'))
    experience = db.relationship('EmploymentExperience', backref='holder')

    def __init__(self, date, gpa, title, companyName, cowner):
        super(CompanyOffer, self).__init__(date, gpa)
        self.title = title
        self.companyName = companyName
        self.cowner = cowner

    def jsonstr(self):

        jsondata = {
            'date':self.date,
            'photocopy': self.photocopy,
            'gpa': self.gpa,
            'offer_type': self.offer_type,
            'title': self.title,
            'companyName': self.companyName

        }

        return jsondata



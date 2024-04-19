from sqlalchemy import Column, Boolean

from app.models.base import db
from app.models.companyOffer import CompanyOffer
from app.models.uicer import UICer

class Alumni(UICer):

    anonymousName = Column(Boolean)
    coffers = db.relationship('CompanyOffer', backref='cowner', foreign_keys=[CompanyOffer.cowner_id])

    def __init__(self, name, email, GPA, _password, role, anonymousName):
        super(Alumni,self).__init__(name, email, GPA, _password, role)
        self.anonymousName = anonymousName

    def jsonstr(self):
    #for testing in the login func of original user
        jsondata = {
            'name':self.name,
            'email': self.email,
            'GPA': self.GPA,
            'password': self.password,
            'status': self.status,
            'anonymousName': self.anonymousName

        }

        return jsondata

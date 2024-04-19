from sqlalchemy import Column, String, Integer, DATE, Float
from app.models.base import Base


class Offer(Base):
    __abstract__ = True

    offer_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DATE)
    photocopy = Column(String(200), default='https://tse3-mm.cn.bing.net/th/id/OIP-C.X11R7arVSvahR0oQpaoYkAHaFS?pid=ImgDet&rs=1')
    gpa = Column(Float)



    def __init__(self, date, gpa):
        self.date = date
        self.gpa = gpa

    def verifyOffer(self):
        return True

    def update(self, date, offer_type):
        if date.year.isna() == True:
            return False
        if date.month.isna() == True and date.day.isna() == False:
            return False
        if offer_type.isna() == True:
            return False
        if offer_type < 1 or offer_type > 3:
            return False
        else:
            self.date = date
            self.photocopy = date
            self.offer_type = offer_type
            return True

    def updateGPA(self, gpa):
        if gpa < 0 or gpa > 4.0:
            return False
        else:
            self.gpa = gpa
            return 'Update GPA successfully.'

    def jsonstr(self):

        jsondata = {
            'date':self.date,
            'photocopy': self.photocopy,
            'gpa': self.gpa,
            'offer_type': self.offer_type

        }

        return jsondata

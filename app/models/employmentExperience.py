from sqlalchemy import Column, String, Integer
from app.models.base import Base, db


class EmploymentExperience(Base):

    experience_id = Column(Integer, primary_key=True, autoincrement=True)
    companyName = Column(String(50))
    experience = Column(String(99))
    holder_id = Column(Integer,db.ForeignKey('companyOffer.offer_id'))



    def __init__(self,companyName, experience,holder):
        self.companyName = companyName
        self.experience = experience
        self.holder = holder

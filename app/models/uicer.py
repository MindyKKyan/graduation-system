from sqlalchemy import Column, Integer, String, Float
from app.models.base import Base, db
from app.models.companyOffer import CompanyOffer
from app.models.researchOffer import ResearchOffer
from app.models.taughtOffer import TaughtOffer


class UICer(Base):
    __tablename__ = 'uicer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(120))
    GPA = Column(Float(precision=2))
    _password = Column(String(128))
    role = Column(Integer)

    toffers = db.relationship('TaughtOffer', backref='towner', foreign_keys=[TaughtOffer.towner_id])
    roffers = db.relationship('ResearchOffer', backref='rowner', foreign_keys=[ResearchOffer.rowner_id])


    def __init__(self, name, email, GPA, password, role):
        self.name = name
        self.email = email
        self.GPA = GPA
        self._password = password
        self.role = role
from sqlalchemy import Column, Integer, String
from app.models.base import Base, db


class University(Base):
    university_id = Column(Integer, primary_key=True, autoincrement=True)
    university_name = Column(String(50))
    university_rank = Column(Integer)
    programs = db.relationship('Program', backref='provider')

    def __init__(self, university_name, university_rank):
        super().__init__()
        self.university_name = university_name
        self.university_rank = university_rank

    def addProgram(self, program):
        if program not in self.p_list:
            self.program_list.append(program)
            return True
        else:
            return False

    def updateName(self, newName):
        self.university_name = newName
        return True

    def updateu_rank(self, university_rank):
        if university_rank > 0:
            self.university_rank = university_rank
            return True
        else:
            return False


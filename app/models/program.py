from sqlalchemy import Column, Integer, String, Float
from app.models.base import Base, db


class Program(Base):
    program_id = Column(Integer, primary_key=True, autoincrement=True)
    program_name = Column(String(50))
    gpa_low = Column(Float)
    gpa_up = Column(Float)
    program_rank = Column(Integer)
    courseList = Column(String(99))
    provider_id = Column(Integer, db.ForeignKey('university.university_id'))

    def __init__(self, program_name, gpa_range, program_rank, courseList, provider):
        super().__init__()
        self.program_name = program_name
        self.gpa_low = gpa_range[0]
        self.gpa_up = gpa_range[1]
        self.program_rank = program_rank
        self.provider = provider
        self.courseList = courseList

    def updateName(self, new_name):
        self.program_name = new_name
        return True

    def updateProgram(self, new_gpa_range, new_p_rank):
        if new_gpa_range[1] - new_gpa_range[0] > 0.2:
            return False
        elif new_gpa_range[0] < 0 or new_gpa_range[1] > 4.0:
            return False
        elif new_gpa_range[1] < new_gpa_range[0]:
            return False
        else:
            self.gpa_low = new_gpa_range[0]
            self.gpa_up = new_gpa_range[1]
            self.program_rank = new_p_rank
            return True




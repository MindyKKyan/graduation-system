from sqlalchemy import Column, Integer, String

from app.models.base import Base

class Admin(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    _password = Column(String(128))
    role = Column(Integer)


    def __init__(self, name, password, role):
        self.name = name
        self._password = password
        self.role = role
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))
    def __init__(self, name, email, password):
    	self.name = name
    	self.email = email
    	self.password = password
    def __repr__(self):
    	return "<User('%s', '%s', '%s')>" % (self.name, self.email, self.password)



from sqlalchemy import Column, Integer, String, Boolean, Table, Sequence
from app.database import metadata, db_session, Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_sq'), primary_key=True)
    name = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))

    def __init__(self, name, email, password):
    	self.name = name
    	self.email = email
    	self.password = password
    
    def __repr__(self):
    	return "<User('%s', '%s', '%s')>" % (self.name, self.email, self.password)

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, Sequence('user_id_sq'), primary_key=True)
    todo = Column(String(64))
    check = Column(Boolean)

    def __init__(self, todo, check=False):
    	self.todo = todo
    	self.check = check

    def __repr__(self):
    	return "<Todo('%s', '%s')>" % (self.todo, self.check)


import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True,echo=True)
metadata = MetaData()
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)


from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Code/Data/rpg.db', echo=True) # set echo to False after testing
session = Session(bind=engine)
Base = declarative_base()

with engine.connect() as connection:
    rs = connection.execute(text('select "Hello World"' ))
    print(rs.all())
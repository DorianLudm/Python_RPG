from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import sys
sys.path.append("..")
from ORM_connector import session, Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

    characters = relationship('Character', back_populates='user')
    
    def __init__(self):
        self.id = None
        self.username = None
        self.password = None
        
    def load(self, username):
        from Character import Character
        user = session.query(User).filter_by(username=username).first()
        if user:
            self.id = user.id
            self.username = user.username
            self.password = user.password
            self.characters = user.characters
        else:
            raise ValueError(f"No user found with username {username}")
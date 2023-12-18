from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from Character import Character
from typing import List

Base = DeclarativeBase()

class User(Base):
    __tablename__ = "users"
    idU: Mapped[int] = mapped_column(int, primary_key=True)
    username: Mapped[str] = mapped_column(str)
    salt: Mapped[str] = mapped_column(str)
    hashed_password: Mapped[str] = mapped_column(str)
    # Might be Mapped[List["Character"]]
    characters: Mapped[List[Character]] = relationship("Character", back_populates="user")
    
    def __init__(self, username, salt, hashed_password):
        self.logined = False
        self.username = username
        self.salt = salt
        self.hashed_password = hashed_password
    
    # To update
    def login(self, username):
        self.logined = True
        self.username = username
    
    def logout(self):
        self.logined = False
        self.username = None

    def __repr__(self) -> str:
        return f'User({self.username}, {self.logined})'
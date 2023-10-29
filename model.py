from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from DataBase.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String,unique=True, index=True)
    password = Column(String)
    results = relationship("Result", back_populates="owner", cascade="all, delete-orphan")

class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True)
    result = Column(String, index=True)
    coding_lang = Column(String, index=True)
    grammer = Column(String, index=True)
    filler_words = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="results")

Base.metadata.create_all(bind=engine)

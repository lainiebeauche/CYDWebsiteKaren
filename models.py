from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """Represents a user in the database."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    age = Column(Integer)
    language = Column(String)

class Message(Base):
    """Represents a simple textual message from a user."""
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    text = Column(String)


class Comment(Base):
    """Represents a simple textual message from a user."""
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    text = Column(String)

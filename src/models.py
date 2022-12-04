import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    mail = Column(String(50))
    password = Column(String(50))
    first_name = Column(String(20))
    last_name = Column(String(20))
    date_of_birth = Column(String(20))
    photo_profile = Column(String(50))

class Publications(Base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    comments = Column(Text)
    file = Column(String(50))
    create_at = Column(String(50))
    update_at = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))

class Stories(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    file = Column(String(50))
    create_at = Column(String(50))
    update_at = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))

class Reaction(Base):
    __tablename__ = 'reaction'
    id = Column(Integer, primary_key=True)
    publications_id = Column(Integer, ForeignKey('publication.id'))
    create_at = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))

class ReactionStories(Base):
    __tablename__ = 'reaction_stories'
    id = Column(Integer, primary_key=True)
    create_at = Column(String(50))
    stories_id = Column(Integer, ForeignKey('stories.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

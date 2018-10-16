import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Sailors(Base):
    __tablename__ = 'sailors'
    sid = Column(Integer, primary_key=True)
    sname = Column(String(30), nullable=False)
    rating = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)

class Reserves(Base):
    __tablename__ = 'reserves'
    sid = Column(Integer, primary_key=True)
    bid = Column(Integer, primary_key=True)
    day = Column(String(10), primary_key=True)

class Boats(Base):
    __tablename__ = 'boats'
    bid = Column(Integer, primary_key=True)
    bname = Column(String(20), nullable=False)
    color = Column(String(10), nullable=False)
    length = Column(Integer, nullable=False)

engine = create_engine('sqlite:///sailors-mysql.db')
Base.metadata.create_all(engine)
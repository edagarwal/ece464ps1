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
    avgrating = Column(Integer, nullable=False)
    dob = Column(String(10), nullable=False)

class Reserves(Base):
    __tablename__ = 'reserves'
    sid = Column(Integer, primary_key=True)
    bid = Column(Integer, primary_key=True)
    day = Column(String(10), primary_key=True)
    eid = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=True)
    condition = Column(String(30), nullable=True)

class Boats(Base):
    __tablename__ = 'boats'
    bid = Column(Integer, primary_key=True)
    bname = Column(String(20), nullable=False)
    color = Column(String(10), nullable=False)
    length = Column(Integer, nullable=False)
    rent = Column(Integer, nullable=False)
    noofrents = Column(Integer, nullable=False)
    lastmaintenance = Column(String(10), nullable=False)

class Employee(Base):
    __tablename__ = 'employee'
    eid = Column(Integer, primary_key=True)
    ename = Column(String(30), nullable=False)
    job = Column(String(30), nullable=False)
    salary = Column(Integer, nullable=False)
    hours = Column(Integer, nullable=False)

class Sells(Base):
    __tablename__ = 'sells'
    sid = Column(Integer, primary_key=True)
    iid = Column(Integer, primary_key=True)
    day = Column(String(10), primary_key=True)
    eid = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    iid = Column(Integer, primary_key=True)
    iname = Column(String(30), nullable=False)
    cost = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

class Maintenance(Base):
    __tablename__ = 'maintenance'
    bid = Column(Integer, primary_key=True)
    eid = Column(Integer, primary_key=True)
    day = Column(String(10), primary_key=True)
    cost = Column(Integer, nullable=False)

engine = create_engine('sqlite:///sailors2-mysql.db')
Base.metadata.create_all(engine)
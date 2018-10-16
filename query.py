from dec import Base, Sailors, Reserves, Boats
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sailors-mysql.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

sailor = session.query(Sailors).first()
reserve = session.query(Reserves).filter(Reserves.sid == sailor.sid).first()
boat = session.query(Boats).filter(Boats.bid == reserve.bid).first()
print(sailor.sname)
print(boat.bname)
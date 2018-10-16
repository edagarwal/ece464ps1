from dec2 import Base, Sailors, Reserves, Boats, Employee, Sells, Inventory, Maintenance
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sailors2-mysql.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

sailor = session.query(Sailors).first()
reserve = session.query(Reserves).filter(Reserves.sid == sailor.sid).first()
boat = session.query(Boats).filter(Boats.bid == reserve.bid).first()
maintenance = session.query(Maintenance).filter(Maintenance.bid == reserve.bid).first()
employee = session.query(Employee).filter(Employee.eid == reserve.eid).first()
sells = session.query(Sells).filter(Sells.sid == sailor.sid).first()
item = session.query(Inventory).filter(Inventory.iid == sells.iid).first()

print('Sailor: ', sailor.sname)
print('Boat: ', boat.bname)
print('Last Maintenance: ', maintenance.day)
print('Date: ', reserve.day)
print('Rented by: ', employee.ename)
print('Items purchased: ', item.iname)
print('Quantity: ', sells.quantity)
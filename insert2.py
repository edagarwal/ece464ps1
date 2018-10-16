from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dec2 import Base, Sailors, Reserves, Boats, Employee, Sells, Inventory, Maintenance

engine = create_engine('sqlite:///sailors2-mysql.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

sailor = Sailors(sid=90,sname='vin',avgrating=3,dob='1960/01/01')
session.add(sailor)

boat = Boats(bid=101,bname='Interlake',color='blue',length=45,rent=1000,noofrents=20,lastmaintenance='2017/10/10')
session.add(boat)

employee = Employee(eid=500,ename='John',job='Clerk',salary=15,hours=100)
session.add(employee)

reserve = Reserves(sid=90,bid=101,day='1998/8/10',eid=500)
session.add(reserve)

inventory = Inventory(iid=600,iname='Sail',cost=100,stock=50)
session.add(inventory)

sells = Sells(sid=90,iid=600,day='1998/8/10',eid=500,quantity=2)
session.add(sells)

maintenance = Maintenance(bid=101,eid=500,day='2017/10/10',cost=1000)
session.add(maintenance)

session.commit()
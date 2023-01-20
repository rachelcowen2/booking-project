import sqlite3
import random
import datetime

from counter import *
from customer import *
from booking import *

con = sqlite3.connect("Booking.db")
cur = con.cursor()

ret = createTableTable(cur)

res = cur.execute("Select name from sqlite_master")
print(res.fetchone())

# add tables
for i in range(1,10):
    addTable(cur,i, random.randint(1,6))
    
print(cur.execute("select * from counter").fetchall())

createCustomerTable(cur)

for i in range(1,10):
    addCustomer(cur, i,str("customer"+str(i)),i)
    
print(cur.execute("select * from customer").fetchall())

createBookingTable(cur)

for i in range(1,10):
    addBooking(cur, i, 
    random.randint(1,10),random.randint(1,10),
    datetime.datetime.now()+datetime.timedelta(hours = random.randint(1,100)))

print(cur.execute("Select * from booking").fetchall())

con.close()
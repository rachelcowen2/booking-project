import sqlite3
import random
import datetime
con = sqlite3.connect("Booking.db")
cur = con.cursor()
cur.execute("drop table if exists counter")
query = """Create table if not exists counter(
TableNumber integer not null unique,
NumSeats integer not null);"""
cur.execute(query)
res = cur.execute("Select name from sqlite_master")
print(res.fetchone())
for i in range(1,10):
    query = f"""insert into counter values
({i},{random.randint(1,6)})"""
    #print(query)
    cur.execute(query)
print(cur.execute("select * from counter").fetchall())
#delquery = "delete from counter;"
#cur.execute(delquery)
#print(cur.execute("select * from counter order by NumSeats"),fetchall())
#print(cur.execute("select * from counter where NumbSeats =2"),fetchall())
#cur.commit()

cur.execute("drop table if exists customer")
query = """create table if not exists customer(
CustomerID integer not null unique,
Name varchar(50) not null,
PhoneNum integer not null);
"""
cur.execute(query)
res = cur.execute("Select name from sqlite_master")
print(res.fetchone())



def addCustomer(CustomerID,Name,PhoneNum,cur):
    query = f"""insert into customer values
({CustomerID},"{Name}",{PhoneNum});"""
    #print (query)
    cur.execute(query)
    
print(cur.execute("Select * from customer").fetchall())
for i in range(1,10):
    #print(i)
    addCustomer(i,str("customer"+str(i)),i,cur)
    
print(cur.execute("select * from customer").fetchall())


cur.execute("drop table if exists booking")
query = """create table if not exists booking(
BookingID integer not null unique,
CustomerID integer not null,
TableNum interger not null,
BookingTime integer not null);
"""
cur.execute(query)

def addBooking(BookingId, CustomerId, TableNum, BookingTime):
    query = f"""insert into booking values
(?,?,?,?);"""
    cur.execute(query,(BookingId,CustomerId,TableNum,BookingTime))

for i in range(1,10):
    addBooking(i, random.randint(1,10),random.randint(1,10),datetime.datetime.now()+datetime.timedelta(hours = random.randint(1,100)))
print(cur.execute("Select * from booking").fetchall())

print(cur.execute("Select * from booking join customer on booking.CustomerID = customer.CustomerId").fetchall())
print(cur.execute("Select date(BookingTime) from booking join customer on booking.CustomerID = customer.CustomerId where date(BookingTime) = date('16/01/2023')").fetchall())
con.close()
        

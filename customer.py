import sqlite3
import random
import datetime

def createCustomerTable(cur):
    cur.execute("drop table if exists customer")
    query = """create table if not exists customer(
CustomerID integer not null unique,
Name varchar(50) not null,
PhoneNum integer not null);
"""
    cur.execute(query)



def addCustomer(cur, CustomerID,Name,PhoneNum):
    query = f"""insert into customer values
({CustomerID},"{Name}",{PhoneNum});"""
    #print (query)
    cur.execute(query)
    
import sqlite3
import random
import datetime

def createBookingTable(cur):
    cur.execute("drop table if exists booking")
    query = """create table if not exists booking(
    BookingID integer not null unique,
    CustomerID integer not null,
    TableNum interger not null,
    BookingTime integer not null);
    """
    cur.execute(query)

def addBooking(cur, BookingId, CustomerId, TableNum, BookingTime):
    query = f"""insert into booking values
(?,?,?,?);"""
    cur.execute(query,(BookingId,CustomerId,TableNum,BookingTime))

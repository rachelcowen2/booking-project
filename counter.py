import sqlite3
import random
import datetime

def createTableTable(cur):
    cur.execute("drop table if exists counter")
    query = """Create table if not exists counter(
TableNumber integer not null unique,
NumSeats integer not null);"""
    cur.execute(query)

def addTable(cur, tableNumber, numSeats):
    query = f"""insert into counter values ({tableNumber},"{numSeats}");"""
    cur.execute(query) 
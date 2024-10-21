'''
  Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  K19 - Working with SQL and CSV files
  2024-10-20
  time spent: 1 hour
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
c.execute("DELETE FROM courses")
c.execute("DELETE FROM students")

with open("courses.csv", mode = 'r') as file:
    command = "CREATE TABLE IF NOT EXISTS courses (code TEXT, mark NUMBER, id NUMBER)"          # test SQL stmt in sqlite3 shell, save as string
    c.execute(command)
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    for row in reader: 
        str = "('"
        str += row.get(headers[0]) + "', "
        str += row.get(headers[1]) + ", "
        str += row.get(headers[2]) + ")"
        query = f"INSERT INTO courses VALUES {str}" 
        c.execute(query)

with open("students.csv", mode = 'r') as file:
    command = "CREATE TABLE IF NOT EXISTS students (name TEXT, age NUMBER, id NUMBER)"          # test SQL stmt in sqlite3 shell, save as string
    c.execute(command)
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    for row in reader: 
        str = "('"
        str += row.get(headers[0]) + "', "
        str += row.get(headers[1]) + ", "
        str += row.get(headers[2]) + ")"
        query = f"INSERT INTO students VALUES {str}" 
        c.execute(query)


#==========================================================

db.commit() #save changes

res = c.execute("SELECT code, mark, id FROM courses")
print(res.fetchall())

rest = c.execute("SELECT name, age, id FROM students")
print(rest.fetchall())

db.close()  #close database

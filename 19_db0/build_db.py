#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

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
fields = []
rows = []

with open('courses.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        print(row)

command = "CREATE TABLE IF NOT EXISTS courses(code, mark, id)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

c.execute("""
INSERT INTO courses VALUES
    ('systems', '75', '1'),
    ('softdev', '65', '1')
""")
db.commit()

res = c.execute("SELECT code FROM courses")
print(res.fetchall())
#==========================================================

db.commit() #save changes
db.close()  #close database

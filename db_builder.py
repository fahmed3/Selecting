import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#peeps
peeps = csv.DictReader(open("peeps.csv"))
headers = peeps.fieldnames
command = "CREATE TABLE peeps (%s);" % (str(headers)[1:-1])
c.execute(command)

for row in peeps:
    command = "INSERT INTO peeps VALUES ('%s',%s,%s)" % (
        row['name'], row['age'], row['id'])
    #print command
    c.execute(command)

#courses
courses = csv.DictReader(open("courses.csv"))
headers = courses.fieldnames
command = "CREATE TABLE courses (%s);" % (str(headers)[1:-1])
c.execute(command)

for row in courses:
    command = "INSERT INTO courses VALUES ('%s',%s,%s)" % (
        row['code'], row['mark'], row['id'])
    #print command
    c.execute(command)


#command = ""          #put SQL statement in this string
#c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database


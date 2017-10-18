# Fabiha Ahmed, Kristin Lin
# SoftDev pd09
# Work 10: Selecting Success
# 2017-10-18

import csv, sqlite3, db_builder

f = "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

#=========================================================
#PARTE UNO - interacting with peeps and courses


# to print the list of tuples that fetchall returns from SELECT FROM WHERE 
def printer(data):
    for r in data: #for each row
        s = "" #update the name, code, and mark
        for c in r: 
            s+= str(c) + " | "
        print s

# collect the <name>'s grades. take the name, code, mark from the db
def myGrades(name):
    command = "SELECT name, code, mark FROM peeps, courses WHERE courses.id = peeps.id AND '%s' = name;" % (name)
    c.execute(command)
    data = c.fetchall() #get the info that SELECT displays in a list of tuples
    #print data
    return data

# find average of person requested, using data that myGrades(name) returns
def myAverage(name):
    sum = 0
    data = myGrades(name)
    for each in data:
        sum += int(each[2]) #mark was 2nd
    return sum/len(data)

#~~~~~~~~~TESTING~~~~~~~~~~
print
print "PRINTING GRADES OF KRUDER:"
printer(myGrades('kruder'))
print "AVERAGE OF KRUDER:"
print myAverage('kruder')

print
print "PRINTING GRADES OF DORFMEISTER:"
printer(myGrades('dorfmeister'))
print "AVERAGE OF DORFMEISTER:"
print myAverage('dorfmeister')
#~~~~~~~~~TESTING~~~~~~~~~~


#=========================================================
#PARTE DOS - creating new table


#create averages
command = "CREATE TABLE averages (id INTEGER PRIMARY KEY, name TEXT, mean INTEGER NOT NULL)"
c.execute(command)
#take data from peeps, find myAverage for each peep, and put it into averages
command = "SELECT name, id FROM peeps;"
c.execute(command)
data = c.fetchall()
for each in data:
    command = "INSERT INTO averages VALUES (%s, '%s', %s)" % (each[1], each[0], myAverage(each[0]))
    c.execute(command)

db.commit()#saves everything


#=========================================================
#PARTE TRES - interacting with averages


# return id, name, mean of the entire table
def display():
    command = "SELECT * FROM averages;"
    c.execute(command)
    data = c.fetchall()
    return data

# insert new rows into courses table
def updateCourses(course, mark, pid):
    command = "INSERT INTO courses VALUES ('%s', %d, %d)" %(course, mark, pid)
    print command
    c.execute(command)

# update the averages table with new averages
def updateAverages():
    data = display()
    for each in data:
        command = "UPDATE averages SET mean = %d WHERE name = '%s';" % (myAverage(each[1]), each[1])
        c.execute(command)

#~~~~~~~~~TESTING~~~~~~~~~~
print
print "ID, NAME, AVERAGES"
printer(display())

print
print "ADDING POETRY CLASSES"
updateCourses('poetry', 45, 5)
updateCourses('poetry', 75, 7)
updateCourses('poetry', 65, 9)

updateAverages()
print
print "UPDATED AVERAGES FOR TIESTO, TOKIMONSTA, TINI"
printer(display())
#~~~~~~~~~TESTING~~~~~~~~~~


#=========================================================
db.commit()
db.close()

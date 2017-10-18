import csv, sqlite3, db_builder

f = "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()
#=========================================================
def printer(data):
    for r in data:
        s = ""
        for c in r:
            s+= str(c) + " | "
        print s

def myGrades(name):
    command = "SELECT name, code, mark FROM peeps, courses WHERE courses.id = peeps.id AND '%s' = name;" % (name)
    c.execute(command)
    data = c.fetchall()
    #print data
    return data

def myAverage(n):
    sum = 0
    data = myGrades(n)
    for each in data:
        sum += int(each[2])
    return sum/len(data)

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


command = "CREATE TABLE averages (id INTEGER PRIMARY KEY, name TEXT, mean INTEGER NOT NULL)"
c.execute(command)
command = "SELECT name, id FROM peeps;"
c.execute(command)
data = c.fetchall()
for each in data:
    command = "INSERT INTO averages VALUES (%s, '%s', %s)" % (each[1], each[0], myAverage(each[0]))
    c.execute(command)

db.commit()#saves everything

def display():
    command = "SELECT * FROM averages;"
    c.execute(command)
    data = c.fetchall()
    return data

print
print "ID, NAME, AVERAGES"
printer(display())

print
print "ADDING POETRY CLASSES"
command = "INSERT INTO courses VALUES ('poetry', 45, 5)"
print command
c.execute(command)

command = "INSERT INTO courses VALUES ('poetry', 75, 7)"
print command
c.execute(command)

command = "INSERT INTO courses VALUES ('poetry', 65, 9)"
print command
c.execute(command)

def updateAverages():
    data = display()
    for each in data:
        command = "UPDATE averages SET mean = %d WHERE name = '%s';" % (myAverage(each[1]), each[1])
        c.execute(command)

updateAverages()
print
print "UPDATED AVERAGES FOR TIESTO, TOKIMONSTA, TINI"
printer(display())
    
#=========================================================
db.commit()
db.close()

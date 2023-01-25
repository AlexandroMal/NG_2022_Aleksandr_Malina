import sqlite3
from sqlite3 import Error


def connectDatabase():
    try:
        connect = sqlite3.connect("componentsPC.db")
        print("Connected")
    except Error as e:
        print(e)
        print("Error")
    return connect


def createTable():
    connect =  connectDatabase()
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS componentsPC(Name text NOT NULL, status text)")


def inputDataBase(Name,status):
    connect = connectDatabase()
    cursor = connect.cursor()
    createTable()
    cursor.execute("INSERT INTO componentsPC('Name', 'status') VALUES ('{}','{}' )".format(Name,status))
    connect.commit()
    connect.close()
    
    
def returnDataBase():
    connect = connectDatabase()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM componentsPC")
    rows = cursor.fetchall()
    usersTable = "<table border='1'>"
    for row in rows:
        usersTable += "<tr>"
        for cell in row:
            usersTable += "<td>" + str(cell) + "</td>"
        usersTable += "</tr>"
    usersTable += "</table>"
    
    cursor.execute("DROP TABLE IF EXISTS componentsPC")
    
    return(usersTable)
    
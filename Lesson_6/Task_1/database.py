import sqlite3
from sqlite3 import Error
    
def connectDatabase():
    try:
        connect = sqlite3.connect("chat.db")
        print("Connected")
    except Error as e:
        print(e)
        print("Error")
    return connect

def createTable():
    connect =  connectDatabase()
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS chat(login text NOT NULL, message text NOT NULL);")
    
def addToDataBase(login,message):
    connect =  connectDatabase()
    cursor = connect.cursor()
    createTable()
    cursor.execute ("INSERT INTO chat('login', 'message') VALUES ('{}','{}' )".format(login,message))
    connect.commit()
    connect.close()
   
    
def returnDataBase():
    connect =  connectDatabase()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM chat")
    rows = cursor.fetchall()
    
    usersTable = "<table border='1'>"
    for row in rows:
        usersTable += "<tr>"
        for cell in row:
            usersTable += "<td>" + str(cell) + "</td>"
        usersTable += "</tr>"
    usersTable += "</table>"
    return usersTable
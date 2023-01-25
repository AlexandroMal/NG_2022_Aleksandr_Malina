import sqlite3
from sqlite3 import Error

login = input("Enter login:" )
message = input("enter mesage:")

connect = sqlite3.connect("chat.db")
cursor = connect.cursor()   
cursor.execute ("CREATE TABLE IF NOT EXISTS chat(login text NOT NULL, message text NOT NULL)")
connect.commit()
cursor.execute ("INSERT INTO chat('login', 'message') VALUES ('{}','{}' )".format(login,message))
connect.commit()


cursor = connect.cursor()
cursor.execute("SELECT * FROM chat")
rows = cursor.fetchall()
user = ""
usersTable = ""
for row in rows:
    user += str(row)
    for cell in row:
        usersTable += "<label>" + str(cell) + " " + "</label>"


print(usersTable)
print(user)
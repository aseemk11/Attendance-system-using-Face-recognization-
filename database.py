import sys

import mysql.connector



db = mysql.connector.connect(user='root', password='1966', host='localhost', port=3306 , database= 'face_recognization' )

user= sys.argv[1]
scholarid=sys.argv[2]
mycursor = db.cursor()
mycursor.execute("SELECT scholasid FROM studentrecord")
a=mycursor.fetchall()

sql = "INSERT INTO studentrecord(name, Scholasid) VALUES (%s, %s)"
val = ( user, scholarid)
mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")
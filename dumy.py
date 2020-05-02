import mysql.connector
import sys
import datetime
import json
import os

db = mysql.connector.connect(user='root', password='1966', host='localhost', port=3306 , database= 'face_recognization' )
mycursor = db.cursor()




mycursor.execute("SELECT * from studentrecord ")
data1=mycursor.fetchall()



with open('data.json', 'w') as f:
    json.dump(data1, f)


os.system('jsontoexcel.py')

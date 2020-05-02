import pandas as pd
import mysql.connector
import os.path
import shutil
import datetime

path = desktop = os.path.normpath(os.path.expanduser("~/Desktop"))

try:
    os.mkdir(path)
except OSError:
    print ("Already exist" )
else:
    print ("Successfully created the directory %s " % path)

now=datetime.datetime.now()
month=now.month
savepath= 'C:/user'
db = mysql.connector.connect(user='root', password='1966', host='localhost', port=3306 , database= 'face_recognization' )
mycursor = db.cursor()
mycursor.execute("SELECT  COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'studentrecord' ")
data=mycursor.fetchall()

df=pd.read_json('data.json')



df1=pd.DataFrame(data)

a= df1.values.tolist()

header=[]
for sublist in a:
    for val in sublist:
        header.append(val)


df.columns = header
df.to_json('forgui.json')
df.to_excel('data.xlsx',sheet_name='sheet1')
shutil.move('data.xlsx', 'C:/Users/adity/Desktop/{0}.xlsx'.format(month))
print("excel is complete")

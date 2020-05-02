import datetime

import cv2
import mysql.connector
import numpy as np
import os
import sys

#database start


db = mysql.connector.connect(user='root', password='1966', host='localhost', port=3306 , database= "face_recognization")
mycursor = db.cursor()
mycursor.execute("SELECT scholasid FROM studentrecord ")

data = mycursor.fetchall()
mycursor.execute("SELECT id FROM studentrecord ")
ids= mycursor.fetchall()


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/02.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = [0]

# names related to ids: example ==> Marcelo: id=1,  etc
names = data

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
# Create a woorksheet


now= datetime.datetime.now()
today=now.day
month=now.month
timestampStr = str(now.strftime("%d-%m-%Y"))

mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'studentrecord'")
data1 = mycursor.fetchall()
a=data1[-1][0]
#
print(names)
if (a==timestampStr):
    print("")

else:
    mycursor.execute("Alter table studentrecord  ADD COLUMN `{0}` VARCHAR(45) DEFAULT 'Absent' ".format(timestampStr))

while True:

    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.3,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            print (id)
            id1 = names[id-1][0]
            print(id1)

            confidence = "  {0}%".format(round(100 - confidence))

            # Assign attendance


            mycursor.execute("UPDATE `face_recognization`.`studentrecord` SET `{0}` = 'present' WHERE (`scholasid` = '{1}')".format(a,id1))
            #sheet.cell(row=str(id1), column=int(today)).value = "Present"
            db.commit()
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id1), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
os.system('python dumy.py')
cam.release()
cv2.destroyAllWindows()

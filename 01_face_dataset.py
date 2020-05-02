''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc                       

Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18    

'''
import sys

import cv2
import os
import mysql.connector

#database start
db = mysql.connector.connect(user='root', password='1966', host='localhost', port=3306 , database= 'face_recognization' )
mycursor = db.cursor()
scholarid= sys.argv[1]
#camerano=sys.argv[2]
sql = "SELECT * FROM studentrecord WHERE scholasid = '{0}'".format(scholarid)

mycursor.execute(sql)
id = mycursor.fetchall()

#//////////////////////////////////////////////////////////


size = 4
cam = cv2.VideoCapture(0)
cam.set(3, 1240)  # set video width
cam.set(4, 720)  # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = id[0][0]

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while (True):

    ret, img = cam.read()
    im = cv2.flip(img, 1)  # flip video image vertically
    # mini = cv2.resize(im, (im.shape[1] // size, im.shape[0] // size))
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('video', img)

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30:  # Take 30 face sample and stop video
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
os.system('python training.py ')
cam.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
#import RPi.GPIO as GPIO
import time
import mysql.connector


def check_user(users, ch):
    a = ch.split(",")
    check = False
    for i in range(len(users)):
        if (str(users[i][1]) == a[0] and str(users[i][2]) == a[1]):
            check = True
    return check

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dangcap07',
    port='3306',
    database='test2'
)

mycursor = mydb.cursor()

mycursor.execute('select * from users')

users = mycursor.fetchall()
# setup opencv
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

# setup GPIO for lock
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(16,GPIO.OUT)

#GPIO.output(16,GPIO.LOW)

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        ch = str(obj.data,'utf-8')
        # set up open door with qr code = 1
        if check_user(users, ch):
            print("code is: ", ch)
            print("open the door")
            #GPIO.output(16, GPIO.HIGH)
            time.sleep(3)
        # setup door not open for code not equal 1
        else:
            print("code is: ", ch)
            print("can't open the door")
            time.sleep(3)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
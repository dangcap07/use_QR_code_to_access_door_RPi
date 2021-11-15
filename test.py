import qrcode
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dangcap07',
    port='3306',
    database='test2'
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, pass) VALUES (%s, %s)"
val = input('name and password: ').split(" ")
mycursor.execute(sql, val)

mydb.commit()
str = str(val[0]) + ',' + str(val[1])
gen_img = qrcode.make(str)
gen_img.save("QR.png")

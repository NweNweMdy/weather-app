import mysql.connector 
from mysql.connector import Error
import base64
import io
import time
from PIL import Image

idd=input("Enter the id of the image=")

try:
    connection = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="N671234#@!b",
                                 database="testdb",
                                 charset="utf8")
                                
    cursor = connection.cursor()
    query= "SELECT name, file FROM myImage WHERE idd="+idd
    cursor.execute(query)
    data=cursor.fetchall()
    print(data[0][0])
    time.sleep(2)
    image1= data[0][1]

    bdata=base64.b64decode(image1)
    photo=Image.open(io.BytesIO(bdata))
    photo.show()

    imgPath="./images/"+str(data[0][0])+ ".jpg"
    file=open(imgPath,'wb')
    file.write(bdata)
    file.close()
    print("Image is stored in Photos folders")
except Error as e:
    print("Error in mysql connection=",e)
finally:
    print("My Sql connection closed")
    connection.close()

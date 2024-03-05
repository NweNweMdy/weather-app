import mysql.connector 
from mysql.connector import Error
import base64

idd= input("Enter the id of the image =")
namee= input("Enter the name=")
photou=input("Enter the path of the image with name=")

file=open(photou,'rb').read()
file= base64.b64encode(file)
try:
    connection = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="N671234#@!b",
                                 database="testdb",
                                 charset="utf8")
                                
    cursor = connection.cursor()
    query= "INSERT INTO myImage values(%s, %s, %s)"
    tuple=(idd, namee, file)
    cursor.execute(query, tuple)
    connection.commit()
    print("Image is stored at id=", idd)
except Error as e:
    print("Error in mysql connection=",e)
finally:
    print("My Sql connection closed")
    connection.close()

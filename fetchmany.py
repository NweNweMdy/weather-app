import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    mySql_select_Query = "select * from laptop"
    cursor = connection.cursor()
    cursor.execute(mySql_select_Query)
    row_count = 2
    records = cursor.fetchmany(row_count)

    print("Total number of rows is: ", cursor.rowcount)
    print("Printing ", row_count, " Laptop record using cursor.fetchmany")
    for row in records:
        print(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("connection is closed")

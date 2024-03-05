import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    mySql_Create_Table_Query = """CREATE TABLE Python_Employee1 ( 
                             id INT NOT NULL,
                             name TEXT NOT NULL,
                             photo LONGBLOB NOT NULL,
                             biodata LONGBLOB NOT NULL,
                             PRIMARY KEY (id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Python_Employee1 Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

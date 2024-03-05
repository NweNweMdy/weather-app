import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    mySql_Create_Table_Query = """CREATE TABLE myImage ( 
                            idd INT NOT NULL,
                            name TEXT NOT NULL,
                            file LONGBLOB NOT NULL,
                            PRIMARY KEY (idd)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("myImage Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

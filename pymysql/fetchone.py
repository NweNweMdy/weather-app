import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    mySql_select_Query = "select * from laptop"
    cursor = connection.cursor(buffered=True)
    cursor.execute(mySql_select_Query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

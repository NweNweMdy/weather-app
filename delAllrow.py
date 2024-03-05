import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')
    cursor = connection.cursor()
    Delete_all_rows = """truncate table Laptop """
    cursor.execute(Delete_all_rows)
    connection.commit()
    print("All Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete all records from database table: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

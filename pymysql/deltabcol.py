import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')
    cursor = connection.cursor()
    alter_column = """ALTER TABLE Laptop DROP COLUMN Purchase_date"""
    cursor.execute(alter_column)
    connection.commit()
    print("Column Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete column: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

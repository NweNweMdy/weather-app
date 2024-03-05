import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')
    cursor = connection.cursor()
    delete_table_query = """DROP TABLE Laptop"""
    cursor.execute(delete_table_query)

    delete_database_query = """DROP DATABASE Electronics"""
    cursor.execute(delete_database_query)
    connection.commit()
    print("Table and Database Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete table and database: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

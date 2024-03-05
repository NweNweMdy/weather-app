import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop SET Price = %s WHERE id = %s"""

    # multiple records to be updated in tuple format
    records_to_update = [(3000, 3), (4000, 4)]
    cursor.executemany(sql_update_query, records_to_update)
    connection.commit()

    print(cursor.rowcount, "Records of a laptop table updated successfully")

except mysql.connector.Error as error:
    print("Failed to update records to database: {}".format(error))
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

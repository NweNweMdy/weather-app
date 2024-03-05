from datetime import datetime

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Purchase_date = %s where id = %s"""

    current_Date = datetime.now()
    formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
    id = 2
    input = (formatted_date, id)
    cursor.execute(sql_update_query, input)
    connection.commit()
    print("Purchased Date Updated successfully ")

except mysql.connector.Error as error:
    print("Failed to update purchased date {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("connection is closed")

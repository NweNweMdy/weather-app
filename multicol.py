import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Name = %s, Price = %s where id = %s"""

    name = "HP Pavilion"
    price = 2200
    id = 4
    input = (name, price, id)

    cursor.execute(sql_update_query, input)
    connection.commit()
    print("Multiple columns updated successfully ")

except mysql.connector.Error as error:
    print("Failed to update columns of table: {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

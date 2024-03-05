import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop SET Name = %s, Price = %s WHERE id = %s"""

    input_id = int(input("What is the ID to be changed:"))
    input_name = input(f"What is the name to be change of {input_id}:")
    input_price = int(input(f"What is the Price to be changed of {input_id}:"))
    
    input = (input_name, input_price, input_id)

    cursor.execute(sql_update_query, input)
    connection.commit()
    print("Multiple columns updated successfully ")

except mysql.connector.Error as error:
    print("Failed to update columns of table: {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

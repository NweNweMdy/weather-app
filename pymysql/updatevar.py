import mysql.connector

def update_laptop_price(id, price):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='testdb',
                                             user='root',
                                             password='N671234#@!b')

        cursor = connection.cursor()
        sql_update_query = """Update Laptop SET price = %s WHERE id = %s"""
        input_data = (price, id)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print("Record Updated successfully ")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

update_laptop_price(3, 7500)
update_laptop_price(4, 5000)

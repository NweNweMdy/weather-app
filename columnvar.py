import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    sql_Query = "select price from laptop where id =%s"
    id = (2,)
    cursor = connection.cursor()
    cursor.execute(sql_Query, id)
    record = cursor.fetchone()

    #cursor.execute("SELECT Price FROM Laptop WHERE id = 21")
    #print (cursor.fetchone() )

    # selecting column value into variable
    price = record
    print("Laptop price is : ", price)

except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

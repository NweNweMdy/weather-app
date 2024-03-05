from datetime import datetime

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    mySql_insert_query = """INSERT INTO Laptop2 (Id, Name, Price, Purchase_date) 
                            VALUES (%s, %s, %s, %s) """

    cursor = connection.cursor()
    current_Date = datetime.now()
    print(datetime.now())
    print(current_Date)
    # convert date in the format you want
    #formatted_date = datetime.now().strftime("%y-%m-%d-%H-%M")
    insert_tuple = (18, 'Acer Predator Triton', 2435, current_Date)
    print(insert_tuple)
    result = cursor.execute(mySql_insert_query, insert_tuple)
    connection.commit()
    print("Date Record inserted successfully")

except mysql.connector.Error as error:
    connection.rollback()
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


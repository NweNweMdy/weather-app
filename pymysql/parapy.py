import mysql.connector

def get_laptop_detail(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='testdb',
                                             user='root',
                                             password='N671234#@!b')

        cursor = connection.cursor()
        sql_select_query = """select * from laptop where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()

        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Salary  = ", row[3], "\n")

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

get_laptop_detail(1)
get_laptop_detail(2)

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='N671234#@!b')

    cursor = connection.cursor(prepared=True)
    sql_Delete_query = """Delete from employee where id = %s"""
    empId = 2

    cursor.execute(sql_Delete_query, (empId,))
    connection.commit()
    print("Record Deleted successfully using Parameterized query")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

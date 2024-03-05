import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into Python_Employee1 table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='testdb',
                                             user='root',
                                             password='N671234#@!b')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO Python_Employee1
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into Python_Employee1 table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Eric", "C:\\Users\\PNE\\Desktop\\pymysql\\images\\eric.jpg",
           "C:\\Users\\PNE\\Desktop\\pymysql\\images\\eric_bioData.txt")
insertBLOB(2, "George", "C:\\Users\\PNE\\Desktop\\pymysql\\images\\george.jpg",
           "C:\\Users\\PNE\\Desktop\\pymysql\\images\\george_bioData.txt")

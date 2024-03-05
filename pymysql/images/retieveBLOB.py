import mysql.connector


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(emp_id, photo, bioData):
    print("Reading BLOB data from Python_Employee1 table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='testdb',
                                             user='root',
                                             password='N671234#@!b')

        
        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from Python_Employee1 where id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[2]
            file = row[3]
            print("Storing employee image and bio-data on disk \n")
            write_file(image, photo)
            write_file(file, bioData)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


readBLOB(1, "C:\\Users\\PNE\\Desktop\\pymysql\\images\\b coder-1.png",
         "C:\\Users\\PNE\\Desktop\\pymysql\\images\\eric_bioData.txt")
readBLOB(2, "C:\\Users\\PNE\\Desktop\\pymysql\\images\\b coder-2.png",
         "C:\\Users\\PNE\\Desktop\\pymysql\\george_bioData.txt")

	



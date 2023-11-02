import mysql.connector
import csv

host = "127.0.0.1"
user = "root"
password = "3103"
database = "sakila"
csv_filename = "output.csv"

try:
    mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    mycursor = mydb.cursor()

    query = "SELECT * FROM customer"
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    with open(csv_filename, 'w') as csv_file:
        my_csv_writer = csv.writer(csv_file)
        my_csv_writer.writerow([i[0] for i in mycursor.description])
        my_csv_writer.writerows(myresult)




except Exception as e:
    print(f"Error: {str(e)}")

finally:
    mycursor.close()
    mydb.close()
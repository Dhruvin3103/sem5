import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="3103",
 database="electronics"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE LAPTOPS")
print('\nTable Dropped\n')
mydb.commit()

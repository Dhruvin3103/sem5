import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3103",
    database="electronics"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE Laptop ADD Rating int(10)")
mydb.commit()
mycursor.execute("SELECT * FROM Laptop")
res = mycursor.fetchall()
for x in res:
    print(x)
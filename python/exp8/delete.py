import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3103",
    database="electronics"
)

mycursor = mydb.cursor()
mycursor.execute("DELETE FROM Laptop WHERE Id = 17")
mydb.commit()
res = mycursor.fetchall()
for x in res:
    print(x)
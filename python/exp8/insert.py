import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3103",
    database="electronics"
)

mycursor = mydb.cursor()
sql = """ 
        INSERT INTO LAPTOP(Id, Name, Price, Purchase_date) VALUES(%s, %s, %s, %s)
                 """
val = [(17,'Macbook M1','114000','2019-08-22'),(21,'Macbook M2 pro','240000','2019-08-27')]
mycursor.executemany(sql,val)
mydb.commit()

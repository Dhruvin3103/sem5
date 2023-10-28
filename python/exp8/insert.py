import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3103",
    database="electronics"
)

mycursor = mydb.cursor()
sql = """ 
        INSERT INTO LAPTOP(Id, Name, Price, Purchase_date, Rating) VALUES(%s, %s, %s, %s, %s)
                 """
val = [(31,'Microsoft Go','120000','2019-08-22',4.1),(29,'Macbook M2 pro','2370000','2019-08-27',4.7)]
mycursor.executemany(sql,val)
mydb.commit()

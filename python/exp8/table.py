import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3103",
    database="electronics"
)

mycursor = mydb.cursor()
# mycursor.execute("""
#                  CREATE TABLE LAPTOP(
#                     Id int(11) NOT NULL,
#                     Name varchar(250) NOT NULL,
#                     Price float NOT NULL,
#                     Purchase_date Date NOT NULL,
#                     PRIMARY KEY(Id)
#                  )
#                  """)
mydb.commit()
mycursor.execute(""" 
                 INSERT INTO LAPTOP(Id, Name, Price, Purchase_date) VALUES(16,'Acer aspire 8','53000','2019-08-17')
                 """)
mydb.commit()


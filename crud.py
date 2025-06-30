# import mysql.connector

# #---------connection creation with sql--------------
# try:
#     conn=mysql.connector.connect(host='127.0.0.1',user='root',passwd='root',database='indigo')
#     mycursor=conn.cursor()

# # -----------create a database on the db server----------------
#     # mycursor.execute('CREATE DATABASE indigo')
#     # conn.commit()
#     # print("Database Created Successfully!")
# except mysql.connector.DatabaseError as db:
#     print("Error in Database",db)

# ----------create a table----------------
# --------airport --> airport_id | code | name | city----------

# mycursor.execute(""" CREATE TABLE airport(
#                  airport_id INTEGER PRIMARY KEY,
#                  code VARCHAR(10) NOT NULL,
#                  city VARCHAR(50) NOT NULL,
#                  name VARCHAR(255) NOT NULL)""")   
# conn.commit() 
# print('Table created successfully!')

# ----------insert data to the table----------
# mycursor.execute("""INSERT INTO airport VALUES
# (1,'DEL','New Delhi','IGIA'),
# (2,'CCU','Kolkata','NSCA'),
# (3,'BOM','Mumbai','CSMA')""")
# conn.commit()
# print("Data inserted successfully!")

# -----------Search/Retrieve---------------     
# mycursor.execute("""SELECT * FROM airport 
#                  WHERE airport_id > 1""") 
# -------------use fetchall method for fetching data from database--------
# data=mycursor.fetchall()
# print(data)

# for i in data:
#     print(i[3])

# -------------update---------------
# mycursor.execute("""UPDATE airport 
#                  SET city='Bombay' 
#                  WHERE city='Mumbai' """)
# conn.commit()
# print("Updated Successfully!")

# --------------search/retrieve---------------
# mycursor.execute("SELECT * FROM airport")
# data=mycursor.fetchall()
# print(data)

# --------------Delete-------------

# mycursor.execute("""DELETE FROM airport WHERE airport_id = 3""")
# conn.commit()
# print("Deleted Successfully!")

# mycursor.execute("SELECT * FROM airport")
# data=mycursor.fetchall()
# print(data)
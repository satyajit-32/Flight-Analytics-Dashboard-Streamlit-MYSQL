import mysql.connector
try:
    con=mysql.connector.connect(host='127.0.0.1',user='root',passwd='root')
    cur=con.cursor()
    query='CREATE DATABASE indigo'
    cur.execute(query)
    print("Database Created Successful!")
except mysql.connector.DatabaseError as db:
    print("Error in Database",db)
    
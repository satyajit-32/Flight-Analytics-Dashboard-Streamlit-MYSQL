import mysql.connector

# connect to the database server

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='root',
                database='flights'
            )
            self.mycursor=self.conn.cursor()
            print("Connection Established !!")
        except mysql.connector.DatabaseError as db:
            print("MySQL error",db)

    def fetch_city_names(self):
        city=[]
        self.mycursor.execute(""" SELECT DISTINCT(source) FROM flights
                                UNION
                                SELECT DISTINCT(destination) FROM flights; 
                            """)
        data=self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city
    
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute(""" SELECT Airline,Route,Dep_Time,Duration,Price FROM flights
                                  WHERE Source='{}' AND Destination='{}' """.format(source,destination))
        data=self.mycursor.fetchall()
        return data
    
    def fetch_airline_frequency(self):

        airline=[]
        frequency=[]

        self.mycursor.execute("""SELECT Airline,COUNT(*) FROM flights
                                 GROUP BY Airline """)
        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency

    def busy_airport(self):
        
        city=[]
        frequency=[]
        self.mycursor.execute("""SELECT source,COUNT(*) FROM (SELECT source FROM flights
							                                  UNION ALL
							                                  SELECT destination FROM flights) t
                                GROUP BY t.source
                                ORDER BY COUNT(*) DESC """)
        data=self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city,frequency

    def daily_frequency(self):
        date=[]
        frequency=[]
        self.mycursor.execute(""" SELECT Date_of_journey, COUNT(*) 
                                  FROM flights 
                                  GROUP BY Date_of_journey  """)
        data=self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date,frequency   
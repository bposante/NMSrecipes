import mysql.connector
import db_settings as dbs

class NMSDatabase:
    def __init__(self):
        self.mydb = None
        self.mycursor = None
        try:
            print("Attempting to connect to database")
            self.mydb = mysql.connector.connect(
                host=dbs.host,
                user=dbs.username,
                password=dbs.password,
                database="NMS_data"
            )
        except mysql.connector.errors.ProgrammingError:
            print("Database not found, creating database")
            self.mydb = mysql.connector.connect(
                host=dbs.host,
                user=dbs.username,
                password=dbs.password
            )
            mycursor = self.mydb.cursor()
            mycursor.execute("CREATE DATABASE NMS_data")
        print("Successfully connected to database.")

if __name__ == "__main__":
    test = NMSDatabase()
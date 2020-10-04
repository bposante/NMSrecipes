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
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("CREATE DATABASE NMS_data")
        print("Successfully connected to database.")
        return

    def create_table(self, name, columns):
        command = "CREATE TABLE "
        command = command + str(name) + " ("
        for item in range(0, len(columns)):
            if item != len(columns) - 1:
                command = command + columns[item] + " VARCHAR(255), "
            else:
                command = command + columns[item] + " VARCHAR(255))"
        print(name, columns, command)

if __name__ == "__main__":
    test = NMSDatabase()
    test.create_table("refiner_recipes",["recipe_output", "recipe_qty", "recipe_val", "input_1", "input_1_qty", "input_2", "input_2_qty", "input_3", "input_3_qty"])
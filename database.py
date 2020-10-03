import mysql.connector
import db_settings as dbs

mydb = mysql.connector.connect(
  host=dbs.host,
  user=dbs.username,
  password=dbs.password
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mydatabase")
mycursor.execute("CREATE DATABASE mydatabase")
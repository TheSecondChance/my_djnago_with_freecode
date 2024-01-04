import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'wontoPNA2383LS@#f*!FL',
)

cursoreObject = dataBase.cursor()
cursoreObject.execute("CREATE DATABASE alpha")
print("All Done!")
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = banco.cursor()

cursor.execute("CREATE DATABASE exmysql")

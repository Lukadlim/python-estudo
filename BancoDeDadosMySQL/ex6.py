import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="exmysql"
)

cursor = banco.cursor()

cursor.execute("DROP DATABASE exmysql")

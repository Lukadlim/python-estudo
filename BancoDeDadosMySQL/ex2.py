import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="exmysql"
)

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas(nome VARCHAR(255), idade INT(3), email VARCHAR(255))")

banco.commit()

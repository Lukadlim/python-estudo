import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="exmysql"
)

cursor = banco.cursor()

comando_sql = "SELECT * FROM pessoas"

cursor.execute(comando_sql)

valores_lidos = cursor.fetchall()

print(valores_lidos)

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_youtube"
)

cursor = banco.cursor()

comando_SQL = "SELECT * FROM pessoas WHERE idade > 40"

cursor.execute(comando_SQL)

valores_lidos = cursor.fetchall()

print(valores_lidos)


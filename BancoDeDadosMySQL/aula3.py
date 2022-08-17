import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_youtube"
)

cursor = banco.cursor()

comando_SQL = "INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)"
dados = ("João", "65", "joao_123@gmail.com")
cursor.execute(comando_SQL, dados)

banco.commit()

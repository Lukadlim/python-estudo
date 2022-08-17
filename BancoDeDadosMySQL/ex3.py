import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="exmysql"
)

cursor = banco.cursor()

nome = str(input('Nome: '))

comand = "INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)"
dados = (f"{nome}", "58", "pedreiro45@hotmail.com")

cursor.execute(comand, dados)

banco.commit()

# from * select pessoas; = mostrar os dados da tabelas

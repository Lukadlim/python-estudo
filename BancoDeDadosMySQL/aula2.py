import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_youtube"
)

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome VARCHAR (255), idade INT(3), email VARCHAR(255))")  # Criar tabela

# show databases; = mostrar as bases de dados
# use "nome da database"; = selecionar a database
# show tables; = mostrar as tabelas criadas

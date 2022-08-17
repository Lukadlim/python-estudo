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

dados = cursor.fetchall()

for c in dados:
    print(f'Nome: {c[0]:<12} idade: {c[1]:<3} email: {c[2]}')

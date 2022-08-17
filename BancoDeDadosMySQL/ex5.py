import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="exmysql"
)

cursor = banco.cursor()

comando_sql = "DELETE FROM pessoas WHERE nome = 'pedro'"

cursor.execute(comando_sql)

banco.commit()

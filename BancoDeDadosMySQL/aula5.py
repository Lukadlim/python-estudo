import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_youtube"
)

cursor = banco.cursor()

comando_SQL = "DELETE FROM pessoas WHERE nome = 'Pedro'"

cursor.execute(comando_SQL)

banco.commit()




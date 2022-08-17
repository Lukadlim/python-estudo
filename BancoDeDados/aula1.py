import sqlite3

banco = sqlite3.connect('Arquivos.db') # Como criar banco de dados

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)") # Como criar tabela

#cursor.execute("INSERT INTO pessoas VALUES('Felipe', 30, 'felipe_123@gmail.com')")  # Como inserir dados

#banco.commit()
cursor.execute('SELECT * FROM pessoas') # Como ver dados no banco de dados
print(cursor.fetchall())

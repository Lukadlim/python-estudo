import sqlite3

nome = 'Juliana'
idade = 28
email = 'juliana@gmail.com'
banco = sqlite3.connect('primeiro_banco.db') # Como criar banco de dados

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)") # Como criar tabela

#cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"', "+str(idade)+", '"+email+"')")  # Como inserir dados

cursor.execute("UPDATE pessoas SET nome = 'Fábio' WHERE idade = 28")

banco.commit()
'''cursor.execute('SELECT * FROM pessoas') # Como ver dados no banco de dados
print(cursor.fetchall())'''
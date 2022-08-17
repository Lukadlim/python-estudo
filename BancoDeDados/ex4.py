import sqlite3

nome = 'Juliana'
idade = 23
email = 'novinhasedutora@gmail.com'

banco = sqlite3.connect('Arquivos.db')

cursor = banco.cursor()

# cursor.execute(f"INSERT INTO Pessoas VALUES('{nome}', {idade}, '{email}')")

banco.commit()

cursor.execute('SELECT * FROM Pessoas')
print(cursor.fetchall())


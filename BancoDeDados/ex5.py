import sqlite3

banco = sqlite3.connect('Arquivos.db')

cursor = banco.cursor()

cursor.execute("UPDATE Pessoas SET Nome = 'Gabriel' WHERE Nome = 'Carlos'")

banco.commit()

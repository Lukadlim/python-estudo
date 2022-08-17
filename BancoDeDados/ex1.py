import sqlite3

banco = sqlite3.connect('Arquivos.db')

cursor = banco.cursor()

# cursor.execute('CREATE TABLE Pessoas("Nome" text, "Idade" integer, "Email" text)')
# nome = str(input('Digite o nome: '))
#
# cursor.execute(f'INSERT INTO Pessoas VALUES("Carlos", 58, "guerrasempre@hotmail.com")')
#
# banco.commit()

cursor.execute('SELECT Email FROM Pessoas')
print(cursor.fetchall())


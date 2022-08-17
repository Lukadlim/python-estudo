import sqlite3

try:
    banco = sqlite3.connect('Arquivos.db')

    cursor = banco.cursor()

    cursor.execute("DELETE FROM Pessoas WHERE Idade = 47")

    banco.commit()
    banco.close()
    print('Deletado com sucesso')
except:
    print('Deu ruim')


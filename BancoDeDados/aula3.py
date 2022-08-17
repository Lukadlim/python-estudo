import sqlite3

try:
    banco = sqlite3.connect('primeiro_banco.db')  # Como criar banco de dados

    cursor = banco.cursor()

    cursor.execute('DELETE from pessoas WHERE idade')

    banco.commit()
    banco.close()
    print('Os dados foram deletados com sucesso')

except sqlite3.Error as erro:
    print('Erro ao excluir os dados', erro)


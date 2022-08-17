import sqlite3
import os

print('-' * 30)
print(f'{"Banco de dados":^30}')
print('-' * 30)
print('''[1] - Criar Banco de dados
[2] - Acessar banco de dados''')
while True:
    try:
        ope = int(input('O que deseja? '))
    except:
        ope = ' '
    if ope not in range(1, 3):
        print('''------ERRO------
Digite "1" ou "2"''')
    print('-' * 30)
    if ope == 1 or ope == 2:
        break
if ope == 1:
    nbank = str(input('Nome do Banco de dados: '))
    banco = sqlite3.connect(f'{nbank}.db')
elif ope == 2:
    while True:
        nbank = str(input('Nome do Banco de dados: '))
        print('-' * 30)
        try:
            arquivo = open(f'{nbank}.db')
            sinal = True
        except:
            print('Este banco de dados não existe')
            sinal = False
        if sinal:
            break
        print('-' * 30)
    print('')

    # banco = sqlite3.connect(f'{nbank}.db')
    # print('Conectado')





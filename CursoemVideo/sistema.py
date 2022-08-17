from time import sleep
from ex115 import *

while True:
    print('-' * 50)
    print(f'{"MENU PRINCIPAL":^50}')
    print('-' * 50)
    print(f'''{co[1]}1{co[0]} - {co[2]}Ver pessoas cadastradas{co[0]}
{co[1]}2{co[0]} - {co[2]}Cadastrar nova pessoa{co[0]}
{co[1]}3{co[0]} - {co[2]}Sair do Sistema{co[0]}''')
    print('-' * 50)
    resp = leropcao(f'{co[1]}Sua opção: {co[0]}')
    if resp == 1:
        print('-' * 50)
        print(f'{"PESSOAS CADASTRADAS":^50}')
        print('-' * 50)
        try:
            arquivo = open('dados.txt', 'r', -1, "utf-8")
        except:
            print(f'{"Não há pessoas cadastradas":^50}')
        else:
            print(arquivo.read(), end='')
            arquivo.close()
    if resp == 2:
        print('-' * 50)
        print(f'{"NOVO CADASTRO":^50}')
        print('-' * 50)
        arquivo = open('dados.txt', 'a', -1, "utf-8")
        dado = []
        nome = lerinput('Nome: ')
        idade = idadeinput('Idade: ')
        dado.append(nome[0:40])
        dado.append(idade)
        arquivo.writelines(dado)
        arquivo.close()
        print(f'Novo registro de {nome.strip()} adicionado')
    if resp == 3:
        print('-' * 50)
        print(f'{"Saindo do sistema... Até logo!":^50}')
        print('-' * 50)
        sleep(2)
        break
    sleep(3)

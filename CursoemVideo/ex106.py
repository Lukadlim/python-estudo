from time import sleep


def simb(frase, cor):
    global normal
    qnt = len(frase)+4
    if cor == 'verde':
        cor = '\033[0:29:42m'
    elif cor == 'azul':
        cor = '\033[0:29:46m'
    elif cor == 'vermelho':
        cor = '\033[0:29:41m'
    normal = '\033[m'
    print(f'{cor}~'*qnt)
    print(f'{frase:^{qnt}}')
    print(f'~' * qnt)
    print(normal, end='')


while True:
    simb('SISTEMA DE AJUDA PyHELP', 'verde')
    comando = input('Função ou biblioteca > ')
    if comando == 'fim':
        break
    simb(f'Acessando manual do comando {comando}', 'azul')
    sleep(2)
    print('\033[1:30:107m', end='')
    help(comando)
    print(normal, end='')
    sleep(1)
sleep(1)
simb('ATÉ LOGO', 'vermelho')

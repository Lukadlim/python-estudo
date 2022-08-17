from random import randint
from time import sleep
jogos = []
cartela = []
print('-'*30)
print('{:^30}'.format('MEGA SENA'))
print('-'*30)
jogo = int(input('Quantos jogos deseja? '))
print('{:=^32}'.format(f' SORTEANDO {jogo} JOGOS '))
for c in range(0, jogo):
    cont = 0
    while cont < 6:
        n = randint(1, 60)
        if n not in cartela:
            cartela.append(n)
            cont += 1
    cartela.sort()
    jogos.append(cartela[:])
    cartela.clear()
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)

from random import randint
from time import sleep
jogadores = {}
pos = 1
print('Valores sorteados:')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'    O jogador{c} tirou {jogadores[f"jogador{c}"]}')
    sleep(1)
print('Ranking dos jogadores:')
for j in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    {pos}° Lugar: {j} com {jogadores[j]}')
    sleep(1)
    pos += 1

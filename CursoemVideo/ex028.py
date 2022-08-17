import random
from time import sleep
n1 = int(input('Escolha um número de 0 a 5: '))
ne = random.randint(0, 5)
print('PROCESSANDO...')
sleep(3)
print(f'Você venceu, o número escolhido foi {ne}' if ne == n1 else f'Você perdeu, número escolhido foi {ne}')

import random
from time import sleep
print(f'Jokenpô vs computador')
jogador = input('Escolha pedra, papel ou tesoura: ')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
if jogador == 'pedra' and pc == 'papel' or jogador == 'papel' and pc == 'tesoura' or jogador == 'tesoura' and pc == 'pedra':
    print(f'O computador venceu, ele escolheu {pc}')
elif jogador == pc:
    print(f'Empate, o computador também escolheu {pc}')
elif jogador == 'pedra' or jogador == 'tesoura' or jogador == 'papel':
    print(f'Você venceu, o computador escolheu {pc}')
else:
    print('Talvez tenha escrito errado, tente novamente')

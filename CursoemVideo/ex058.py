from random import randint
pc = randint(0, 10)
jogador = 11
tentativa = 0
print('O computador pensou em um número de 0 a 10')
while jogador != pc:
    jogador = int(input('Qual é esse numero? '))
    tentativa += 1
    if jogador != pc:
        print('Errou, tente mais uma vez')
print(f'Parabens, voce acertou na {tentativa}ª tentativa')
from random import randint
print('Ímpar ou par')
ganho = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    jogada = str(input('Ímpar ou par? [I/P]: '))[0]
    while jogada not in 'PpIi':
        jogada = str(input('Ímpar ou par? [I/P]: '))[0]
    total = pc + jogador
    if total % 2 == 0:
        print(f'Você jogou {jogador} e o computador {pc}. Total deu {total}. DEU PAR')
        if jogada in 'Pp':
            print('Você venceu')
            print('Jogue novamente')
            ganho += 1
        else:
            print('Voce perdeu')
            break
    else:
        print(f'Você jogou {jogador} e o computador {pc}. Total deu {total}. DEU ÍMPAR')
        if jogada in 'Ii':
            print('Voce venceu')
            print('Jogue novamente')
            ganho += 1
        else:
            print('Voce perdeu')
            break
print(f'FIM DE JOGO. Você ganhou {ganho} vezes')

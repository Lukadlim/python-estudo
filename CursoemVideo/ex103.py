def ficha(nome, gols):
    if not nome:
        nome = '<desconhecido>'
    if not gols or not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
gols = input('Quantidade de gols: ')
ficha(jogador, gols)

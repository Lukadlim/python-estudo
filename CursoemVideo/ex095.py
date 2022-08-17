futebol = dict()
qnt = list()
jogadores = list()
while True:
    total = 0
    futebol['nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
    for c in range(0, part):
        n = int(input(f'Quantos gols na partida {c+1}? '))
        qnt.append(n)
        total += n
    futebol['gols'] = qnt[:]
    futebol['total'] = total
    jogadores.append(futebol.copy())
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N]: '))[0]
    if resp in 'Nn':
        break
    qnt.clear()
print('='*53)
print('{} {:<20}{:<22}{:<20}'.format('cod', 'nome', 'gols', 'total'))
print('-'*53)
for c, i in enumerate(jogadores):
    print(f'{c:>3} {i["nome"]:<20}{i["gols"]!s:<22}{i["total"]:<20}')
print('='*53)
while True:
    jog = -1
    while jog not in range(0, len(jogadores)):
        jog = int(input('Mostrar dados de qual jogador? [999] interrompe: '))
        if jog == 999:
            break
        if jog not in range(0, len(jogadores)):
            print(f'ERRO! Não existe jogador com código {jog}! Tente novamente')
    if jog == 999:
        break
    print('-' * 53)
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[jog]["nome"]}:')
    for c in range(0, len(jogadores[jog]['gols'])):
        print(f'   => Na partida {c+1}, fez {jogadores[jog]["gols"][c]} gols.')
    print('-' * 53)
print('-' * 53)
print('FIM DO PROGRAMA')

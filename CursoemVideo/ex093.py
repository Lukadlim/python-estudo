futebol = dict()
qnt = list()
total = 0
futebol['nome'] = str(input('Nome: '))
part = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
for c in range(0, part):
    n = int(input(f'Quantos gols na partida {c}? '))
    qnt.append(n)
    total += n
futebol['gols'] = qnt
futebol['total'] = total
print('='*50)
print(futebol)
print('='*50)
for c, i in futebol.items():
    print(f'O campo {c} tem o valor {i}.')
print('='*50)
print(f'O jogador {futebol["nome"]} jogou {part} partidas')
for c in range(0, part):
    print(f'   => Na partida {c}, fez {futebol["gols"][c]} gols.')
print(f'Foi um total de {total} gols.')

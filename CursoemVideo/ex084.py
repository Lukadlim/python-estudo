pessoas = list()
dado = list()
cont = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    cont += 1
    if cont == 1 or dado[1] > pesado:
        pesado = dado[1]
    if cont == 1 or dado[1] < leve:
        leve = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N]: '))[0]
    if resp in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso é {pesado:.2f}kg. Que são: ', end='')
for p, c in enumerate(pessoas):
    if pessoas[p][1] >= pesado:
        print(f'{pessoas[p][0]}', end=' ')
print(f'\nO menor peso foi de {leve:.2f}kg. Que são: ', end='')
for p, c in enumerate(pessoas):
    if pessoas[p][1] <= leve:
        print(f'{pessoas[p][0]}', end=' ')

boletim = []
aluno = []
nota = []
media = []
cont = 0
espaco = ''
while True:
    aluno.append(str(input('Nome: '))[:10])
    for c in range(1, 3):
        nota.append(float(input(f'Nota {c}: ')))
    media.append((nota[0]+nota[1]) / 2)
    aluno.append(nota[:])
    aluno.append(media[:])
    boletim.append(aluno[:])
    aluno.clear()
    nota.clear()
    media.clear()
    resp = ' '
    cont += 1
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N]: '))[0]
    if resp in 'nN':
        break
print('{:<3}{:>5}{:>20}'.format('N°', 'NOME', 'MÉDIA'))
print('-'*30)
for c in range(0, cont):
    print(f'{c:<3} {boletim[c][0]:<10}{boletim[c][2][0]:>13.1f}')
print('-'*30)
while True:
    vernota = int(input('De qual aluno deseja ver as notas? (999 interrompe): '))
    if vernota == 999:
        break
    print(f'Notas de {boletim[vernota][0]} são: {boletim[vernota][1]}')

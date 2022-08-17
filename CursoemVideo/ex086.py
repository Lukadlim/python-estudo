lista = [[[], [], []], [[], [], []], [[], [], []]]
for c in range(0, 3):
    for p, n in enumerate(lista):
        num = int(input(f'Digite um valor para [{c}, {p}]: '))
        lista[c][p].append(num)
for c in range(0, 3):
    for pos in range(0, 3):
        print(f'[{lista[c][pos][0]:^5}]', end=' ')
    print()

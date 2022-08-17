lista = [[[], [], []], [[], [], []], [[], [], []]]
par = terceira = maiord = 0
for c in range(0, 3):
    for p, n in enumerate(lista):
        num = int(input(f'Digite um valor para [{c}, {p}]: ')[:5])
        lista[c][p].append(num)
        if num % 2 == 0:
            par += num
        if p == 2:
            terceira += num
        if c == 1 and num > maiord:
            maiord = num
for c in range(0, 3):
    for pos in range(0, 3):
        print(f'[{lista[c][pos][0]:^5}]', end=' ')
    print('\n', end='')
print('-'*30)
print(f'A soma dos valores pares é de: {par}')
print(f'A soma dos valores da terceira coluna é: {terceira}')
print(f'O maior valor da segunda linha é o {maiord}')

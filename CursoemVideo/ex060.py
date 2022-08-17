f = 1
n = int(input('Digite um numero para ver a fatoracao: '))
print(f'{n}! = ', end='')
for c in range(n, 1, -1):
    f *= c
    print(f'{c}', end=' x ')
print(f'1 = {f}')
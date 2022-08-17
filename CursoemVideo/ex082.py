numeros = []
pares = []
impares = []
resp = ' '
while resp not in 'Nn':
    numeros.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'NnSs':
        resp = str(input('Deseja continuar? [S/N]: '))[0]
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

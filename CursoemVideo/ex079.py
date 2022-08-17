numeros = []
resp = ' '
while resp not in 'Nn':
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('\033[:32mValor adicionado com sucesso\033[:m')
    else:
        print('\033[:31mValor repetido, não será adicionado\033[:m')
    resp = ' '
    while resp not in 'NnSs':
        resp = str(input('Deseja adicionar mais um número? [S/N]: '))[0]
print('='*42)
numeros.sort()
print(f'Você digitou os valores: {numeros}')

numeros = []
cont = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'nNSs':
        resp = str(input('Deseja continuar? [S/N]: '))[0]
    cont += 1
    if resp in 'Nn':
        break
numeros.sort(reverse=True)
print(f'''Quantidade de números digitados: {cont}
lista dos valores em ordem decrescente: {numeros}''')
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')

numeros = list()
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))
copy = numeros[:]
maior = max(numeros)
menor = min(numeros)
contma = numeros.count(maior)
contme = numeros.count(menor)
print(f'Você digitou os valores {numeros}')
print(f'O maior número é {maior} nas posições', end=' ')
for c in range(0, contma):
    posma = numeros.index(maior)
    print(f'{posma}...', end=' ')
    del numeros[posma]
    numeros.insert(posma, 'a')
numeros = copy
print(f'\nO menor número é {menor} nas posições', end=' ')
for c in range(0, contme):
    posme = numeros.index(menor)
    print(f'{posme}...', end=' ')
    del numeros[posme]
    numeros.insert(posme, 'a')

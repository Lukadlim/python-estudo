numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite mais um outro número: ')))
print(numeros)
nove = numeros.count(9)
if 3 in numeros:
    tres = numeros.index(3)+1
else:
    tres = '3 não apereceu em nenhuma posição'
print(f'''O valor 9 apareceu: {nove} vezes
O valor 3 apareceu na posição: {tres}
Os valores pares são o''', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

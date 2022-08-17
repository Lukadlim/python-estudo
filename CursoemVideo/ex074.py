from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(numeros)
menor = numeros[0]
maior = numeros[0]
for c in range(0, 5):
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print(f'''O menor número é: {menor}
O maior número é: {maior}''')

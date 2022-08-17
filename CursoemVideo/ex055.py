maior = 0
menor = 0
print('Quem é o mais magro e o mais gordo?')
for p in range(1, 6):
    peso = float(input(f'Digite o {p}ª peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é de {maior}kg')
print(f'O menor peso é de {menor}kg')
print('A soma de todos os multiplos de 3 impares de 1 a 500')
nada = input('Aperte enter para comecar ')
soma = 0
cont = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        cont = cont + 1
        soma = soma + c
print(f'A soma de {cont} valores é igual a {soma}')

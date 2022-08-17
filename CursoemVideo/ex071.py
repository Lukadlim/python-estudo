from math import floor
print('Banco pobrezil')
valor = int(input('Valor a ser sacado: R$'))
cinquenta = floor(valor/50)
total = cinquenta * 50
falta = valor - total
vinte = floor(falta/20)
total = total + vinte * 20
falta = valor - total
dez = floor(falta/10)
total = total + dez * 10
falta = valor - total
um = floor(falta/1)
total = total + um
if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de R$50')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez > 0:
    print(f'Total de {dez} cédulas de R$10')
if um > 0:
    print(f'Total de {um} cédulas de R$1')

n = 0
ndigitado = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    ndigitado += 1
    soma += n
if n == 999:
    soma = soma - 999
    ndigitado -= 1
print(f'A soma de {ndigitado} números digitado é de {soma}')
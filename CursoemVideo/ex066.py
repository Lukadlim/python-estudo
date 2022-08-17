digitado = soma = 0
while True:
    n = int(input('Digite um valor ("999" para parar): '))
    if n == 999:
        break
    digitado += 1
    soma += n
print(f'A soma de {digitado} números digitados é {soma}')

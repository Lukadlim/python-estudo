resp = ''
divisao = soma = maior = 0
menor = 9999999999999999999
while resp != 'N':
    n = int(input('Digite um valor: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    divisao += 1
    soma += n
    resp = str(input('Quer continuar? ("S" para sim, "N" para não): ')).upper()
    if resp != 'N' and resp != 'S':
        while resp != 'N' and resp != 'S':
            print('Resposta inválida, digite novamente')
            resp = str(input('Quer continuar? ("S" para sim, "N" para não): ')).upper()
media = round(soma/divisao, 1)
print(f'''A média dos valores digitados é {media}
O maior número digitado foi {maior}
O menor número digitado foi {menor}''')
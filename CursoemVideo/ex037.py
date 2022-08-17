n = int(input('Digite um valor: '))
print('Digite: \n1 para binario \n2 para octal \n3 para hexadecimal')
c = int(input('Qual conversao voce deseja: '))
if c == 1:
    print(f'O valor {n} em binario é {bin(n)[2:]}')
elif c == 2:
    print(f'O valor de {n} em octal é {oct(n)[2:]}')
elif c == 3:
    print(f'O valor {n} em hexadecimal é {hex(n)[2:].upper()}')
else:
    print('Comando invalido, tente novamente')
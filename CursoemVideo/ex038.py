print('Comparador de numeros')
n1 = int(input('1º valor: '))
n2 = int(input('2° valor: '))
if n1 > n2:
    print(f'O primeiro valor {n1}, é maior que {n2} ')
elif n2 > n1:
    print(f'o segundo valor {n2}, é maior que {n1}')
else:
    print(f'Os valores {n1} e {n2} sao iguais')
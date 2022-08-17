sal = int(input('Salario: R$'))
if sal >= 1250:
    ns = sal*10/100
    print(f'Com 10% de aumento seu salário será R${ns+sal:.2f}')
else:
    ns = sal*15/100
    print(f'com 15% de aumento seu salário será R${ns+sal:.2f}')
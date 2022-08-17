casa = float(input('Valor da casa: R$'))
salario = float(input('Seu salário: R$'))
ano = int(input('Anos de prestação: '))
salario1 = salario*30/100
mes = casa/(ano*12)
if salario1 >= mes:
    print(f'Emprestimo aprovado, 30% do seu salário(R${salario1:.2f}) séra possivel pagar a prestação de R${mes:.2f}')
else:
    print(f'Emprestimo negado, 30% do seu salário(R${salario1:.2f}) não séra possivel pagar a prestação de R${mes:.2f}')

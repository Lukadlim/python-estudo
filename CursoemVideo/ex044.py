preco = float(input('Preço: R$'))
print('''Digite o número para escolher a forma de pagamento
[1] à vista dinheiro/cheque (10% de desconto)
[2] à vista no cartão (5% de desconto)
[3] 2x no cartão
[4] 3x ou mais no cartão (20% de juros)''')
forma = int(input('Forma de pagamento: '))
if forma == 1:
    desconto = preco*10/100
    print(f'O valor do produto será de R${preco-desconto:.2f}')
elif forma == 2:
    desconto = preco*5/100
    print(f'O valor do produto será de R${preco-desconto:.2f}')
elif forma == 3:
    parcela = preco/2
    print(f'O valor do produto será de R${preco:.2f} com 2 parcelas de R${parcela:.2f}')
elif forma == 4:
    parcela = int(input('Em quantas vezes deseja parcela: '))
    juros = preco*20/100
    parcela1 = (preco + juros) / parcela
    print(f'O valor do produto será de R${preco+juros:.2f} com {parcela} parcelas de R${parcela1:.2f}')
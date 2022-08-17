preco = float(input('Preço: '))
desc = preco*5/100
np = preco-desc #preco-(preco*5/100)
print('Com o desconto de 5% o preço é de {:.2f} Reais'.format(np))
resp = 's'
total = caro = barato = 0
sinal = False
nomebarato = ''
print('{:^30}'.format('Loja super caro'))
while resp not in 'Nn':
    print('-'*30)
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    resp = str(input('Quer continuar? [S/N]: '))[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]: '))[0]
    total += preco
    if preco > 1000:
        caro += 1
    if sinal == False or preco < barato:
        barato = preco
        nomebarato = produto
        sinal = True
print('-'*30)
print(f'''O total gasto é de R${total:.2f}
{caro} produtos custam mais de R$1000.00
O produto mais barato: {nomebarato} que custa R${barato:.2f}''')

listagem = ('lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Trasferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*37)
print('{:^36}'.format('Listagem de preços'))
print('-'*37)
for c in range(0, 18, 2):
    print(f'{listagem[c]:.<30}', end='')
    print(f'R${listagem[c+1]:>7.2f}')
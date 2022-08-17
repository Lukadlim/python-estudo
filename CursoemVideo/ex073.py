times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino',
         'Fortaleza', 'Corinthians', 'Internacional', 'Fluminense',
         'Cuiabá', 'América-MG', 'Atlético-GO', 'São Paulo', 'Ceará',
         'Athletico-PR', 'Santos', 'Bahia', 'Sport Recife', 'Juventude', 'Grêmio', 'Chapecoense')
print('-'*156)
print(f'Os times do brasileirão: \n{times}')
print('-'*156)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-'*156)
print(f'Os 4 times que estão na zona de rabaixamento são: {times[-4:]}')
print('-'*156)
print(f'''Em ordem alfabética:
{sorted(times)}''')
print('-'*156)
pos = times.index("Chapecoense")+1
print(f'O time da Chapecoense esta na {pos}ª posição')
nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome normal')
print(f'Tenha um bom dia, {nome}.')

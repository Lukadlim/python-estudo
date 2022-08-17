from datetime import date
print('Categoria de natacao com base na idade')
ano = int(input('Ano de nascimento: '))
idade = date.today().year-ano
if idade <= 9:
    print(f'Com {idade} anos de idade você é um nadador mirim')
elif idade <= 14:
    print(f'Com {idade} anos de idade você é um nadador infatil')
elif idade <= 19:
    print(f'Com {idade} anos de idade você é um nadador junior')
elif idade <= 25:
    print(f'Com {idade} anos de idade você é um nadador sênior')
else:
    print(f'Com {idade} anos de idade você é um nadador master')

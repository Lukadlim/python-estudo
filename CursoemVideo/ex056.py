from math import ceil
media = 0
velho = 0
menor = 0
nome1 = ''
for c in range(1, 5):
    print('-'*18)
    nome = str(input(f'Nome da {c}ª pessoa: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo "masculino ou feminino": ')).lower()
    media = media+idade
    if sexo == 'masculino' and c == 1:
        velho = idade
    if idade > velho and sexo == 'masculino':
        velho = idade
        nome1 = nome.title()
    if sexo == 'feminino' and idade < 21:
        menor += 1
media1 = ceil(media/4)
print(f'''A média de idade é de {media1}
O homem mais velho é o {nome1}
Entre as mulheres {menor} tem menos de 21 anos''')

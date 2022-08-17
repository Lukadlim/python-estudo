frase = 'Próxima pessoa'
maior = homem = mjovem = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [F/M]: ')).strip()[0]
    while sexo not in 'Ff' and sexo not in 'Mm':
        sexo = str(input('Digite seu sexo [F/M]: ')).strip()[0]
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mjovem += 1
    resp = str(input('Deseja cadastrar mais alguém? [S/N]: ')).strip()[0]
    while resp not in 'Ss' and resp not in 'Nn':
        resp = str(input('Deseja cadastrar mais alguém? [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
    print(f'{frase:-^20}')
print(f'''{maior} pessoas tem mais de 18 anos
{homem} homens foram cadastrados
{mjovem} mulheres tem menos de 20 anos''')

from datetime import date
ano = date.today().year
menor = 0
maior = 0
frase = 'pessoas são menores'
frase2 = 'pessoas são maiores'
for c in range(1, 8):
    nasc = int(input(f'Data de nascimento da {c}ª pessoa: '))
    idade = ano - nasc
    if idade < 21:
        menor += 1
maior = 7 - menor
if menor == 1:
    frase = frase.replace('pessoas são menores', 'pessoa é menor')
elif maior == 1:
    frase2 = frase2.replace('pessoas são maiores', 'pessoa é maior')
print(f'''Entre 7 pessoas
{menor} {frase} de idade
{maior} {frase2} de idade.''')

from datetime import date
data = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - data
if idade == 18:
    print(f'Este ano ({ano}) voce tera que se alistar')
elif idade < 18:
    print(f'Voce tera que se alistar daqui {18-idade} ano(s) em {ano+(18-idade)}')
else:
    print(f'O tempo de se alistar ja se passou {idade-18} ano(s) que foi em {ano-(idade-18)}')

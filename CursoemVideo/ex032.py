from datetime import date
ano = int(input('(Coloque "0" para analisar o ano atual) Escolha um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'o ano {ano} não é bissexto')
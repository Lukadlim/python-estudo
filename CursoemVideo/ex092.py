from datetime import date
ano = date.today().year
dados = {}
dados['nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = ano - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['contratacao']+35 - nasc
for c, i in dados.items():
    print(f'{c}: {i}')
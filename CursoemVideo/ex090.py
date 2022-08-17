dados = {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
print(f'O nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
if dados["media"] >= 7.0:
    print('Situação é igual a Aprovado')
elif 5.0 <= dados["media"] < 7.0:
    print('Situação é igual a RECUPERÇÃO')
else:
    print('Situação é igual a Reprovado')

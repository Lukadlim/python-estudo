dados = list()
pessoas = {}
totid = 0
mulher = []
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = ' '
    while pessoas['sexo'] not in 'MmFf':
        pessoas['sexo'] = str(input('Sexo [M/F]: '))[0]
        if pessoas['sexo'] not in 'MmfF':
            print('Erro! Por favor, digite apenas M ou F')
    if pessoas['sexo'] in 'Ff':
        mulher.append(pessoas['nome'][:])
    pessoas['idade'] = int(input('Idade: '))
    totid += pessoas['idade']
    dados.append(pessoas.copy())
    resp = ' '
    while resp not in 'SsnN':
        resp = str(input('Deseja continuar? [S/N]: '))[0]
        if resp not in 'SsnN':
            print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(dados)}.')
print(f'A média de idade do grupo: {totid/len(dados)} anos.')
print(f'Nome das mulheres cadastradas: {mulher}')
print('Lista de pessoas que estão acima da média de idade:')
for c, p in enumerate(dados):
    if p['idade'] > totid/len(dados):
        print(p)

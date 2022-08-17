print('10 termos de uma PA')
p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
soma = p
print(p, end=', ')
for c in range(1, 10):
        soma = soma + r
        print(soma, end=', ')
print('Etc...')


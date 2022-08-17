print('Sequência Fibonacci')
termo = int(input('Quantos termos deseja ver? '))
comeco = 1
n1 = 0
n2 = 1
while comeco <= termo/2:
    print(n1, end=', ')
    print(n2, end=', ')
    n1 = n1 + n2
    n2 = n1 + n2
    comeco += 1
if termo % 2 != 0:
    print(n1, end=', ')
print('FIM')

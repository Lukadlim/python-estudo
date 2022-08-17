n = int(input('Digite um número para saber se é primo: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        total += 1
if total == 2:
    print(f'O número {n} é um número primo')
else:
    print(f'O número {n} não é um número primo')
print(f'Porque ele é divisivel por {total} números')

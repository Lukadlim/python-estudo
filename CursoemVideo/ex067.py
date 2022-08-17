n = int(input('Digite um número para ver a tabuada: '))
while True:
    print('='*39)
    if n < 0:
        break
    for c in range(1, 11):
        total = n * c
        print(f'{n} x {c} = {total}')
    print('='*39)
    n = int(input('Digite outro número para ver a tabuada: '))
print('Programa finalizado')

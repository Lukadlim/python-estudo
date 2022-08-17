print('Gerador de PA')
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
limite = r*8+p1
print(p1, end=', ')
while p1 < limite:
    p1 += r
    print(p1, end=', ')
print(f'{p1+r}.')
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
limite = r*9+p1
termo = 1
print(p1, end=', ')
while p1 < limite:
    p1 += r
    print(p1, end=', ')
while termo != 0:
    termo = int(input('\nMais quantos termos deseja ver? '))
    limite = termo*r+p1
    while p1 < limite:
        p1 += r
        print(p1, end=', ')
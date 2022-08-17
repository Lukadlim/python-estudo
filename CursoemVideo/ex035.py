r1 = float(input('1° reta: '))
r2 = float(input('2° reta: '))
r3 = float(input('3° reta: '))
if r1-r2 < r3 and r3 < r1+r2 and r1-r3 < r2 and r2 < r1+r3 and r2-r3 < r1 and r1 < r2+r3:
    print('É possível formar um triangulo')
else:
    print('Não é possível formar um triangulo')
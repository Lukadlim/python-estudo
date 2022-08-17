'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'na posiçao {c} encontrei o valor {v}')
print(enumerate(valores))
#num = [2, 5, 9, 1]
'''num[2] = 3
num.append(7)
num.sort()
num.insert(2, 2)'''

'''if 4 in num:
    num.remove(4)
else:
    print('Não achei o 4')'''
#num.pop(3)
#print(num)

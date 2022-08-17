n1 = int(input('Digite um número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
m = n1
if n2<n1 and n2<n3:
    m = n2
if n3<n1 and n3<n2:
    m = n3
print(f'O menor número é {m}')
ma = n1
if n2>n1 and n2>n3:
    ma = n2
if n3>n1 and n3>n2:
    ma = n3
print(f'O maior número é {ma}')


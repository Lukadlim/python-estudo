print('Somador de números pares')
t = 0
q = 0
for c in range(1, 7):
    n = int(input(f'Digite {c}° valor: '))
    if n % 2 == 0:
        q += 1
        t += n
print(f'A soma de {q} numeros pares é {t} ')
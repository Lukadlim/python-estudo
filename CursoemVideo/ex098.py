from time import sleep
print('='*35)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    if i > f:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    print('=' * 35)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

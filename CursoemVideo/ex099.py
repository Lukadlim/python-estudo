from time import sleep


def maior(* n):
    cont = m = 0
    print('=' * 50)
    print('Analisando os valores passados...')
    for v in n:
        print(v, end=' ')
        sleep(0.5)
        if cont == 0:
            m = v
        else:
            m = max(n)
        cont += 1
    print(f'Foram informados, {len(n)} valores ao todo')
    print(f'O maior valor informado foi: {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

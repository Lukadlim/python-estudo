soma = 0
multi = 1
operacao = 0
for c in range(1, 3):
    n = int(input(f'Digite o {c}° valor: '))
    soma = soma + n
    multi = multi * n
    if c == 1:
        n1 = n
while operacao != 5:
    print('''=====================
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    operacao = int(input('O que deseja? '))
    print('=====================')
    if operacao == 1:
        print(f'{n1}+{n}={soma}')
    elif operacao == 2:
        print(f'{n1}x{n}={multi}')
    elif operacao == 3:
        if n1 > n:
            print(f'Entre {n1} e {n} o maior número é o {n1}')
        else:
            print(f'Entre {n1} e {n} o maior número é {n}')
    elif operacao == 4:
        soma = 0
        multi = 1
        operacao = 0
        for c in range(1, 3):
            n = int(input(f'Digite o {c}° valor: '))
            soma = soma + n
            multi = multi * n
            if c == 1:
                n1 = n
    elif operacao == 5:
        print('Programa encerrado')
    else:
        print('Opção invalida, digite corretamente')
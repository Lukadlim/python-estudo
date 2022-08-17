def leiaint(frase):
    while True:
        n = input(frase)
        if n.isnumeric():
            return n
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')

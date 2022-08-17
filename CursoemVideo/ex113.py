try:
    def leiaint(frase):
        while True:
            n = input(frase)
            try:
                int(n)
            except:
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            else:
                return n


    def leiafloat(valor):
        while True:
            n = input(valor)
            try:
                float(n)
            except:
                print('\033[31mERRO! Digite um número real válido.\033[m')
            else:
                return n

    inteiro = decimal = 0
    inteiro = leiaint('Digite um número inteiro: ')
    decimal = leiafloat('Digite um número real: ')
    print(f'O valor inteiro digitado foi {inteiro} e o real foi {decimal}')
except KeyboardInterrupt:
    print('\033[31mO usuário preferiu não digitar esse número.\033[m')
    print(f'O valor inteiro digitado foi {inteiro} e o real foi {decimal}')

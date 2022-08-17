frase = str(input('Digite uma frase para saber se é um palíndromo: ')).lower().strip()
frase1 = frase.split()
frase2 = ''.join(frase1)
invertida = frase2[::-1]
if frase2 == invertida:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')
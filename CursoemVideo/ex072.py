n = 22
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
print('Numeros por extenso')
while n not in range(0, 21):
    n = int(input('Digite um número entre 0 a 20: '))
print(f'Você digitou o número: {extenso[n]}')

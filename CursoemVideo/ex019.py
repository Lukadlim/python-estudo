import random
an1 = input('Nome do aluno N1: ')
an2 = input('Nome do aluno N2: ')
an3 = input('Nome do alnuo N3: ')
an4 = input('Nome do aluno N4: ')
lista = [an1, an2, an3, an4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi o {escolhido}')
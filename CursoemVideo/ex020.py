import random
al1 = str(input('Aluno N1: '))
al2 = str(input('Aluno N2: '))
al3 = str(input('Aluno N3: '))
al4 = str(input('Aluno n4: '))
nomes = [al1, al2, al3, al4]
random.shuffle(nomes)
print(f'A ordem de apresentacao sera: {nomes}')
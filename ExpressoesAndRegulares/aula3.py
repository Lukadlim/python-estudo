# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}


import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jão
'''

print(re.findall(r'JO+ãO+', texto, flags=re.I))
print(re.findall(r'JO{1,}ãO{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# print(re.sub(r'JO*ãO+', 'Felipe', texto, flags=re.I))
# print(re.sub(r'JO?ãO+', 'Felipe', texto, flags=re.I))
# print(re.sub(r'JO{1,}ãO{1,}', 'Felipe', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall('ama[do]*', texto2, flags=re.I))
print(re.findall('ama[do]{0,2}', texto2, flags=re.I))
print(re.findall('ama[do]*', texto2, flags=re.I))

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

# print(re.findall('jo*ão*', texto, flags=re.I))
# print(re.findall('jo+ão+', texto, flags=re.I))
print(re.findall('jo?ão?', texto, flags=re.I))
# print(re.findall('ve{1,3}m+', texto, flags=re.I))
# print(re.findall('ve{3}m', texto, flags=re.I))
# print(re.sub('jo*ão*', 'Felipe', texto, flags=re.I))

texto2 = 'João ama ser amado'

print(re.findall('ama[do]{0,2}', texto2, flags=re.I))

from ex7Classe import *

c1 = Cliente('Luiz', 32)
c1.insere_enderecos('Belo horizonte', 'MG')
print(c1.nome, c1.idade)
c1.lista_enderecos()
del c1
print('-' * 40)

c2 = Cliente('Maria', 55)
c2.insere_enderecos('Salvador', 'BA')
c2.insere_enderecos('Rio De Janeiro', 'RJ')
print(c2.nome, c2.idade)
c2.lista_enderecos()
print('-' * 40)

c3 = Cliente('João', 19)
c3.insere_enderecos('São Paulo', 'SP')
print(c3.nome, c3.idade)
c3.lista_enderecos()
print('-' * 40)

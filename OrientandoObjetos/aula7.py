from aula7Classe import *

cliente1 = Cliente('Luiz', 32)
cliente1.insere_enderecos('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()


cliente2 = Cliente('Maria', 55)
cliente2.insere_enderecos('Salvador', 'BA')
cliente2.insere_enderecos('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_enderecos('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print('#' * 50)

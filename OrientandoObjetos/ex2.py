class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
        return self._nome

    def desconto(self, porc):
        self.preco = self.preco - (self.preco * porc / 100)
        return f'R${self.preco:.2f}'

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, qnt):
        if type(qnt) == str:
            qnt = int(qnt.replace('R$', ''))
        self._preco = qnt


p1 = Produto('CAMISA', 100)
print(p1.nome, p1.desconto(10))

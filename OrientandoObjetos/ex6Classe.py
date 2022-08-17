class CarrinhoDeCompras:
    def __init__(self):
        self.produto = []

    def inserir_produto(self, produto):
        self.produto.append(produto)

    def lista_produtos(self):
        for produto in self.produto:
            print(produto.nome, produto.preco)

    def soma_total(self):
        total = 0
        for produto in self.produto:
            total += produto.preco
        print(total)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
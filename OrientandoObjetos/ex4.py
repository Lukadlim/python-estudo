class BancoDeDados:
    def __init__(self):
        self.__dados = dict()

    def inserir_cliente(self, id, nome):
        if 'Clientes' not in self.__dados:
            self.__dados['Clientes'] = {id: nome}
        else:
            self.__dados['Clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['Clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['Clientes'][id]

    @property
    def dados(self):
        return self.__dados


bd = BancoDeDados()
bd.inserir_cliente(1, 'Joao')
bd.inserir_cliente(2, 'Maria')
print(bd.dados)
bd.apagar_cliente(1)
bd.lista_clientes()

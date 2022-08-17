class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print('A caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')

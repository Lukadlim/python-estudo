from ex5Classe import *

escritor = Escritor('Joaozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina

print(escritor.nome)
escritor.ferramenta.escrever()


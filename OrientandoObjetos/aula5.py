from aula5Classe import *

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

# del escritor
print(caneta.marca)
maquina.escrever()


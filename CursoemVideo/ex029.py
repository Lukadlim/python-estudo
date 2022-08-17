v = int(input('Velocidade do carro: '))
if v > 80:
    print(f'Você foi multado! terá que pagar uma multa de R${(v-80)*7.00:.2f}')
import math
oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi de: {m:.1f}')
print('PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!')
#if m >=6.0:
    #print('Sua média foi boa!PARABÈNS')
#else:
    #print('Sua média foi ruim! ESTUDE MAIS!')
print('Calculadora de IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f'Com o IMC de {imc:.1f} você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print(f'Com o IMC de {imc:.1f} você está no peso ideal')
elif imc > 25 and imc <= 30:
    print(f'Com o IMC de {imc:.1f} você está sobrepeso')
elif imc > 30 and imc <= 40:
    print(f'Com o IMC de {imc:.1f} seu IMC é de obesidade')
else:
    print(f'Com o IMC de {imc:.1f} seu IMC é de obesidade mórbida')

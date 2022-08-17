km = int(input('Quantos kilometros: '))
#print(f'Sua viagem custara R${km*0.50:.2f}'if km <= 200 else f'Sua viagem custara R${km*0.45:.2f}')
preco = km*0.50 if km <= 200 else km*0.45
print(f'Voce tera que pagar R${preco:.2f} por {km}km viajados')
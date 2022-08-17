def voto(nasc):
    from datetime import date
    global idade
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return 'NÃO VOTA'
    if idade >= 65 or idade == 16 or idade == 17:
        return 'VOTO OPCIONAL'
    if idade >= 18:
        return 'VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano você nasceu? '))
result = voto(nasc)
print(f'Com {idade} anos: {result}')

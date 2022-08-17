sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Digite seu sexo [M/F]: ')).lower()[0]
    if 'f' != sexo != 'm':
        print('Resposta invalida, tente novamente')
if sexo == 'm':
    print('Voce é homem, foda se')
elif sexo == 'f':
    print('Voce tem uma carne mijada')
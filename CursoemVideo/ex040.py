n1 = float(input('1° nota: '))
n2 = float(input('2º nota: '))
media = round((n1+n2)/2, 1)
if media < 5.0:
    print(f'Media de {media}, voce esta \033[31mREPROVADO!\033[m')
elif media >= 5.0 and media <= 6.9:
    print(f'Com a media de {media} voce esta de \033[33mRECUPERAÇÃO\033[m')
elif media >= 7.0:
    print(f'Com a media de {media} voce foi \033[32mAPROVADO\033[m')
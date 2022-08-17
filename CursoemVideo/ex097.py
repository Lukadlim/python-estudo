def escreva(txt):
    qnt = len(txt)+4
    print('~'*qnt)
    print(f'{txt:^{qnt}}')
    print('~' * qnt)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')

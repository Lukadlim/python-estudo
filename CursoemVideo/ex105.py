def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: sem return
    """
    global numeros, boletim
    boletim = {}
    numeros = [n]
    boletim['total'] = len(numeros[0])
    boletim['maior'] = max(numeros[0])
    boletim['menor'] = min(numeros[0])
    media = 0
    for n in numeros[0]:
        media += n
    boletim['média'] = media / boletim['total']
    if sit:
        if boletim['média'] < 5:
            boletim['situação'] = 'RUIM'
        elif 5 <= boletim['média'] < 7:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'BOA'


notas(5.5, 9.5, 10, 6.5, sit=True)
print(boletim)


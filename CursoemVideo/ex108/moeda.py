def metade(num):
    n = num / 2
    return n


def dobro(num):
    n = num * 2
    return n


def aumentar(n, por):
    au = n + (n * por / 100)
    return au


def diminuir(n, por):
    dim = n - (n * por / 100)
    return dim


def moeda(n):
    formatado = f'R${n:.2f}'
    ponto = formatado.index('.')
    formatado = formatado.replace(formatado[ponto], ',')
    return formatado

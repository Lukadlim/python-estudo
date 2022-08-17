def metade(num, show=False):
    n = num / 2
    if show:
        n = moeda(n)
    return n


def dobro(num, show=False):
    n = num * 2
    if show:
        n = moeda(n)
    return n


def aumentar(n, por, show=False):
    au = n + (n * por / 100)
    if show:
        au = moeda(au)
    return au


def diminuir(n, por, show=False):
    dim = n - (n * por / 100)
    if show:
        dim = moeda(dim)
    return dim


def moeda(n):
    formatado = f'R${n:.2f}'
    ponto = formatado.index('.')
    formatado = formatado.replace(formatado[ponto], ',')
    return formatado

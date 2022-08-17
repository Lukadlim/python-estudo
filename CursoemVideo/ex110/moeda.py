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


def resumo(p, au=0, dim=0):
    print('-' * 32)
    print(f'{"RESUMO DO VALOR":^32}')
    print('-' * 32)
    print(f'{"Preço analisado:":<20} {moeda(p)}')
    print(f'{"Dobro do preço:":<20} {dobro(p, True)}')
    print(f'{"Metade do preço:":<20} {metade(p, True)}')
    print(f'{f"{au}% de aumento:":<20} {aumentar(p, au, True)}')
    print(f'{f"{dim}% de redução:":<20} {diminuir(p, dim, True)}')
    print('-' * 32)

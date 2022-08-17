def fatorial(n, show=False):
    """
    -> Calcula o farorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    if show:
        print(f'{n} x ', end='')
    for c in range(n - 1, 1, -1):
        n *= c
        if show:
            print(c, end=' x ')
    if show:
        print('1 = ', end='')
    return n


print(fatorial(5, True))

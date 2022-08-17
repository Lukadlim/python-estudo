def leiadinheiro(valor):
    while True:
        n = input(valor).strip()
        if ',' in n:
            return float(n.replace(',', '.'))
        if '.' in n:
            ncopy = n
            n = n.replace('.', '')
            if n.isnumeric():
                return float(ncopy)
        if n.isnumeric():
            return float(n)
        if n.isalpha() or n == "":
            print(f'\033[31mERRO: "{n}" é um preço inválido!\033[m')

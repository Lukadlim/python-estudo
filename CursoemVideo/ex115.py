global co
# Cores
co = ['\033[m',  # 0 Normal
      '\033[33m',  # 1 Amarelo
      '\033[34m',  # 2 Azul
      '\033[31m',  # 3 Vermelho
      ]


def lerinput(msg):
    n = input(msg).strip().split()
    n = ' '.join(n).title()
    n = f'{n:<40}'
    return n


def idadeinput(msg):
    while True:
        idade = input(msg)
        try:
            int(idade)
        except:
            print(f'{co[3]}ERRO! Digite um número inteiro válido por favor{co[0]}')
        else:
            idade = idade[0:3]
            idade = f'{f" {idade:>3} anos":<5}\n'
            return idade


def leropcao(msg):
    while True:
        opcao = input(msg)
        try:
            opcao = int(opcao)
            if opcao not in range(1, 4):
                opcao = int(' ')
        except:
            print(f'{co[3]}ERRO! Digite uma opção válida por favor{co[0]}')
        else:
            return int(opcao)

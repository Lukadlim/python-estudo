#print('\033[;31;45mOla, mundo\033[m')
nome = 'Lucas'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[0;30m'}
print('Prazer em te conhece-lo {}{}'.format(cores['azul'], nome))
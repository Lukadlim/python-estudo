simbolos = ['(', ')']
expressao = input('Digite a expressão: ')
n1 = expressao.count(simbolos[0])
n2 = expressao.count(simbolos[1])
if '(' not in expressao and ')' not in expressao:
    j = 0
    k = 1
for c in range(0, len(expressao)):
    if '(' not in expressao[c:]:
        break
    j = expressao[c:].index('(')
    if ')' not in expressao[c:]:
        break
    k = expressao[c:].index(')')
if n1 == n2 and j < k:
    print('É uma expressão válida')
else:
    print('Não é uma expressão válida')

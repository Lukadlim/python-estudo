palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis',
            'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'U', 'O')
for c in range(0, len(palavras)):
    print(f'\nNa palavra "{palavras[c]}" as vogais são: ', end='')
    for b in range(0, len(vogais)):
        quantidade = palavras[c].count(vogais[b])
        if vogais[b] in palavras[c]:
            print(f'{vogais[b]}'*quantidade, end=' ')

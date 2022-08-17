cidade = str(input('Nome da cidade: ')).lower().strip()
sep = cidade.split()
sa = 'santo' in sep[0]
print(f'O nome da cidade comeca com Santo? {sa}')
import re

string = 'Este é um teste de expressões teste regulares'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string, count=1))

regexp = re.compile(r'teste')
print(f'''{regexp.search(string)}
{regexp.findall(string)}
{regexp.sub('DEF', string)}''')

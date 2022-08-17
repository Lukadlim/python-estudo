import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

# print(re.findall(r'(<([pdiv]{0,3})>.*?</\2>)', texto))

# tags = re.findall(r'(<([pdiv]{0,3})>.*?</\2>)', texto)
# for tag in tags:
#     um, dois = tag
#     print(um, dois)

print(re.sub(r'(<(.+?)>)(.+?)(</\2>)', r'\1batata\4', texto))

cpf = 'a 147.852.963-12 a'

# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

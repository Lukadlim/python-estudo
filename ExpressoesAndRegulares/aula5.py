# Meta caracteres: ^ $ ( )
#
import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

cpf = 'a 147.852.963-12 a'

# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

print(re.findall(r'(<([divp]{0,3})>.+?<\/\2>)', texto))
# tags = re.findall(r'(<([divp]{0,3})>(.+?)<\/\2>)', texto)
# tags = re.findall(r'<([divp]{0,3})>(?:.+?)<\/\1>', texto)
# tags = re.findall(r'<(?P<tag>[divp]{1,3})>(.+?)<\/(?P=tag)>', texto)
# pprint(tags)

# print(re.sub(r'(<(.+?)>)(.+?)(</\2>)', r'\1\3\4', texto))

# for tag in tags:
#    um, dois, tres = tag
#    print(tres)

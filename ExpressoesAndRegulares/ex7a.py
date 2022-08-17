import re

texto = '''
131.768.460-53 ABC
055.123.060-50 DEF
955.123.060-90
'''

print(re.findall(r'^((?:\d{3}.){2}\d{3}-\d{2}$)', texto, flags=re.M))

texto2 = 'O João gostade folia \n E adora ser amado'

print(re.findall(r'^o.+o$', texto2, flags=re.I | re.S))

import re

cpf = '025.258.963-10'

cpf_reg_exp = re.compile(r'^(\d){3}\.(\d){3}\.(\d){3}-(\d){2}$')
# print(cpf_reg_exp.search(cpf))

ip_reg_exp = re.compile('''
    ^
    (?:
        (?:   
            25[0-5] | # 250-255
            2[0-4][0-9] | # 200-249
            1[0-9]{2} | # 100-199
            [1-9][0-9] | # 10-99
            [0-9] # 0-9
        )
        \.
    ){3}
        (?:   
            25[0-5] | # 250-255
            2[0-4][0-9] | # 200-249
            1[0-9]{2} | # 100-199
            [1-9][0-9] | # 10-99
            [0-9] # 0-9
        )$
''', flags=re.X)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))

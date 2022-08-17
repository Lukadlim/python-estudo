import re

cpf = '025.258.963-10'

cpf_reg_exp = re.compile(r'^(\d{3}\.){2}\d{3}-\d{2}$')

# print(cpf_reg_exp.search(cpf))

ip_reg_exp = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$')

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))

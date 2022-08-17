import urllib.request
try:
    urllib.request.urlopen("http://www.pudim.com.br").getcode()
except:
    print('\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[33mConsegui acessar o site Pudim com sucesso!\033[m')

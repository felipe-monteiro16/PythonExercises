import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except Exception:
    print('\033[91mNão consegui acessar o site Pudim.\033[m')
else:
    print('\033[92mConsegui acessar o site Pudim com sucesso!\033[m')

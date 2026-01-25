import urllib.request

try:
    a1 = urllib.request.urlopen('https://pudim.com.br/') 
except:
    print("\033[0;31mNAO FOI POSSIVEL ACESSAR O SITE NO MOMENTO!\033[m")
else:
    print("\033[1;32mSITE ACESSADO COM SUCESSO!\033[m")
    print(a1)
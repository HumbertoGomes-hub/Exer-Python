def leiaDinheiro(msg):
    while True:
        valor = str(input(msg))
        valor = valor.replace(",",".")
        if valor.isalpha():
            print(f"\033[1;31mERRO VALOR '{valor}' INVALIDO!\033[m")
    
        if valor.strip() == "":
            print("\033[1;31mERRO VALOR INVALIDO!\033[m")
        else:
            res = float(valor)
            break
    return res






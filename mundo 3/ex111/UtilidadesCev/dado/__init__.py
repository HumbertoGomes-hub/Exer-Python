def leiaDinheiro(msg):
    while True:
        valor = str(input(msg))
        a1 = valor.replace(",",".")
        a1 = valor.isnumeric()
        print(a1)
        if a1 == float(a1):
            res = float(a1)
            break
            
    
        if a1 == "".strip():
            print("\033[1;31mERRO VALOR INVALIDO!\033[m")
        #elif v == str(v):
        print(f"\033[1;31mERRO VALOR '{a1}' INVALIDO!\033[m")
    
    
    
    return res


leiaDinheiro("difite: ")
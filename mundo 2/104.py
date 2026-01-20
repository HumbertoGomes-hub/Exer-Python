def LeiaInt(msg):
    cor = {"vermelho":"\033[0;31m"}
    num = str(input(msg))
    if num.isnumeric():
        return int(num)
    else:
        while True:
            print(f"{cor['vermelho']}ERRO! Digite um numero inteiro valido")
            num = str(input("Digite um numero: "))
            if num.isnumeric():
                return int(num)
                break
    
    
    
    
    

n = LeiaInt("Digite um numero: ")
print(f"Voce acabou de digitar o numero {n}")
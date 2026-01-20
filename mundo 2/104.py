def LeiaInt(msg):
    num = str(input(msg))
    if num.isnumeric():
        return int(num)
    else:
        while True:
            print("\033[0;31mERRO! Digite um numero inteiro valido\033[m")
            num = str(input("Digite um numero: "))
            if num.isnumeric():
                return int(num)
                break
    
    
    
    
    
print("-" * 30)
n = LeiaInt("Digite um numero: ")
print(f"Voce acabou de digitar o numero {n}")
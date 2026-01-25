def LeiaInt():
    while True:
        try:
            num = (str(input("DIGITE UM VALOR INTEIRO: "))).strip()
        except KeyboardInterrupt:
            print()
            print("\033[0;31mO USUARIO NAO DIGITOU O NUMERO.\033[m")
            return 0
        try:
            int(num)
        except:
            print("\033[0;31mERRO! Digite um numero inteiro valido\033[m")
        
        else: 
            break
    return num


def LeiaFloat():
    while True:
        try:
            num = (str(input("DIGITE UM VALOR REAL: "))).strip()
        except KeyboardInterrupt:
            print()
            print("\033[0;31mO USUARIO NAO DIGITOU O NUMERO.\033[m")
            return 0
        try:
            num = float(num)
        except:
            print("\033[0;31mERRO! Digite um numero real valido\033[m")
        
        else: 
            break
    return num
        

inte = LeiaInt() 
real = LeiaFloat()

    
print(f"O valor inteiro digitado foi {inte} e o real foi {real}")
    
    
    
    
    
    
    
                





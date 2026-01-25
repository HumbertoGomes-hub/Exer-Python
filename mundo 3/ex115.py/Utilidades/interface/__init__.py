def titulo(msg):
    msg = msg.center(30)
    print("-" * 30)
    print(msg)
    print("-" * 30)


def menu():
    print("1 - VER PESSOAS CADASTRADAS\n2 - CADASTRAR PESSOAS\n3 - SAIR")
    print("-" * 30)
     

def LeiaInt(msg):
    while True:
        try:
            num = (str(input(f"DIGITE {msg}: "))).strip()
        except KeyboardInterrupt:
            print()
            print("\033[0;31mO USUARIO OPTOU POR NAO DIGITAR.\033[m")
            return 0
        try:
            num = int(num)
        except:
            print("\033[0;31mERRO! DIGITE UM VALOR VALIDO.\033[m")
        
        else: 
            break
    return num




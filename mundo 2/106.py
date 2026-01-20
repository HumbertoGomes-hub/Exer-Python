cores = {"verde": "\033[1;42m", "azul": "\033[1;44m", 
         "vermelho": "\033[1;41m",
         "remover": "\033[0;0m", "amarelo": "\033[1;43m"
          }



def ajuda(msg):
    from time import sleep
    titulo(f" ACESSANDO MANUAL DO COMANDO {funcao} ", cor=cores["azul"])
    sleep(0.4)
    
    print(cores["amarelo"])
    texto = help(msg)
    print(cores["remover"])
    
    return texto


def titulo(msg2, cor=cores["remover"]):
    tam = len(msg2)+4
    print(cor)
    print("~" * tam)
    print(f"  {msg2}")
    print("~" * tam, end="")
    print(cores["remover"])
    
    
    
# Programa Principal
while True:
    titulo("SISTEMA DE AJUDA PyHelp", cor=cores["verde"])
    funcao = str(input("Função ou Biblioteca > ")).lower().strip()
    ajuda(funcao)
    if funcao == "fim":
        titulo("ATE LOGO!",cor=cores["vermelho"])
        break
    
    
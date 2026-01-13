def mensagem(msg):
    print("-" * len(msg))
    print(f"{msg}")
    print("-" * len(msg))
    

frase = str(input("DIGITE: "))
mensagem(frase)
mensagem('São Paulo')
mensagem('rj')
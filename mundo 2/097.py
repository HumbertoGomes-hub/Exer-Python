def mensagem(msg):
    print("-" * (len(msg)+4))
    print(f"  {msg}")
    print("-" * (len(msg)+4))
    

frase = str(input("DIGITE: "))
mensagem(frase)
mensagem('São Paulo')
mensagem('rj')
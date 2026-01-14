def maior(*valores):
    from time import sleep
    
    
    a1 = "ANALISANDO VALORES"
    print(a1)
    print("-=" * len(a1))
    
    for c in valores:
        sleep(0.5)
        print(c, end=" ", flush=True)
    
    print(" são os valores", end="")
    print(f" Maior valor {max(valores)}")
        
    
    
    

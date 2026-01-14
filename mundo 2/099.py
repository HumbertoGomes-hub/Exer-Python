def maior(*valores):
    from time import sleep
    
    
    a1 = "ANALISANDO VALORES"
    print(a1)
    print("-=" * len(a1))
    
    for c in valores:
        sleep(0.5)
        print(c, end=" ", flush=True)
    
    print("SÃO OS VALORES", end="")
    print(f" TOTAL DE VALORES [{len(valores)}] MAIOR VALOR [{max(valores)}]")
        
    
    
    
maior(1,2,3,4,5,6)
maior(17,62,98)
maior(9,3,2,5)
maior(21,17)
from time import sleep

def maior(*valores):
    print("-=" * 20)
    print("ANALISANDO VALORES")
    print("-=" * 20)
    if valores:
        for c in valores:
            sleep(0.5)
            print(c, end=" ", flush=True)
        vmaior = max(valores)
        totv = len(valores)
        print("SÃO OS VALORES", end="")
        print(f" TOTAL DE VALORES [{totv}] MAIOR VALOR [{vmaior}]")
    else:
        print("SÃO OS VALORES", end="")
        print(" TOTAL DE VALORES [] MAIOR VALOR []")
        
    
    
    
maior(1,2,3,4,5,6)
maior(17,62,98)
maior(1,1,0)
maior()
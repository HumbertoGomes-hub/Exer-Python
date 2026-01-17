from time import sleep

def contador(i , f, p): #i: inicio f: fim p: passo
    
    if i == f:
        print(i)
    elif f > i:
        if p == 0:
            p = 1
        for c in range(i,f+1,p):
            sleep(0.4)
            print(c, end=" ", flush=True)
        print("FIM!")
    elif f < i:
        if p == 0:
            p = 1
        
        if p > 0:
            p = -p
        for c in range(i,f-1,p):
            sleep(0.4)
            print(c, end=" ", flush=True)
        print("FIM!")
    
    
def linha():
    print("=" * 20)        



# PROGRAMA PRINCIPAL
linha()   
print("CONTAGEM 1 A 10 DE 1 EM 1")
contador(1,10,1)
linha()
print("CONTAGEM 10 A 0 DE 2 EM 2")
contador(10,0,2)
linha()
ini = int(input("INICIO: "))
fim = int(input("FINAL:  "))
pas = int(input("PASSO:  "))
linha()
print("CONTAGEM PERSONALIZADA")
linha()
contador(ini, fim, pas)
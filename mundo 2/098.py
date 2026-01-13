def contador(i , f, p): #i: inicio f: fim p: passo
    from time import sleep
    if f > i:
        for c in range(i,f+1,p):
            sleep(0.4)
            print(c, end=" ", flush=True)
        print("FIM!")
    elif f < i:
        for c in range(i,f-1,p):
            sleep(0.4)
            print(c, end=" ", flush=True)
            
        print("FIM!")
    
    
def linha():
    print("=" * 20)        

        
linha()   
print("CONTAGEM 1 A 10 DE 1 EM 1")
contador(1,10,1)
linha()
print("CONTAGEM 10 A 0 DE 2 EM 2")
contador(10,0,-2)
linha()
inicio = int(input("INICIO: "))
fim = int(input("FINAL: "))
passo = int(input("PASSO: "))
linha()
print("CONTAGEM PERSONALIZADA")
linha()
contador(inicio, fim, passo)
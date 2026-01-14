def sorteia():
    from random import randint
    from time import sleep
    
    for c in range(5):
        numeros.append(randint(1,100))
    print("SORTEANDO 5 VALORES ", end="")
    for i in numeros:
        sleep(0.4)
        print(i,flush=True, end=" ")
    print()

def somaPar():
    soma = list()
    for c in numeros:
        
        if c%2 == 0:
            soma.append(c)
    print(f"SOMANDO OS VALORES {numeros} A SOMA DOS PARES SÃO {sum(soma)}")
            
            
          
            
numeros = list()
sorteia()
print("-=" * 30)
somaPar()
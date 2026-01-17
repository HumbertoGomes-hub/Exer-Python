from random import randint
from time import sleep

def sorteia(lista):
    for c in range(5):
        lista.append(randint(1,10))
    print("SORTEANDO 5 VALORES ", end="")
    for i in lista:
        sleep(0.4)
        print(i,flush=True, end=" ")
    print()

def somaPar(lista):
    soma = list()
    for c in lista:
        if c%2 == 0:
            soma.append(c)
    print(f"SOMANDO OS VALORES {lista} A SOMA DOS PARES SÃO {sum(soma)}")
            
            
          
            
numeros = list()
sorteia(numeros)
print("-=" * 30)
somaPar(numeros)

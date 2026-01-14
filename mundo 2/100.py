def sorteia():
    from random import randint
    
    for c in range(5):
        numeros.append(randint(1,100))
    print(f"")   

def somaPar():
    soma = list()
    for c in numeros:
        
        if c%2 == 0:
            soma.append(c)
    print(f"SOMANDO OS VALORES {numeros} A SOMA DOS PARES SÃO {sum(soma)}")
            
            

numeros = list()
sorteia()
somaPar()
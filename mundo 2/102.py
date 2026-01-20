def fatorial(num=0,show=False):
    """ 
    -> Calcula o Fatorial de um numero.
    !param num: O numero a ser calculado.
    !param show: (opcional) Mostrar ou não a conta.
    !return: O valor fatorial de um numero num.
    """
    fat = 1
    print("-" * 30)  
    for c in range(num,0,-1):
        fat *= c
        if show == True:
            print(f"{c} ",end="")
            if c == 1:
                print(f"= ", end="")
                break
            print("x ", end="")
    return fat

        
        
       
print(fatorial(5, True))
help(fatorial)
        
        
    
        
    
        
    
    
        
        
        
    
        
        
        


def fatorial(num=0,show=False):
    """ 
    -> Calcula o Fatorial de um numero.
    !param num: O numero a ser calculado.
    !param show: (opcional) Mostrar ou não a conta.
    !return: O valor fatorial de um numero num.
    """
    fat = num
    if show == True:
        
        for c in range(num,0,-1):
            if c < 5:
                fat *= c

            print(f"{c} ",end="")
            if c == 1:
                print(f"= ", end="")
                break
            print("x ", end="")
        return fat
            
    else:
        for c in range(num,0,-1):
            if c < 5:
                fat *= c
        return fat

        
        
    
print("-" * 30)   
help(fatorial)
        
        
    
        
    
        
    
    
        
        
        
    
        
        
        


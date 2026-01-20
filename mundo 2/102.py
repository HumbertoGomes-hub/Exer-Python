def fatorial(num=0,show=False):
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
print(fatorial(5, True))
        
        
    
        
    
        
    
    
        
        
        
    
        
        
        


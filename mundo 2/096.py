def area(a, l):
    sm = a * l
    print("-" * 20)
    print(f"A área do terreno {a:.1f}x{l:.1f} é de {sm:.2f}m2")
    print("-" * 20)
    
a1 = "CONTROLE DE TERRENOS"
print(a1)
print("-" * len(a1))
altura = float(input("Comprimento (m): "))
largura = float(input("Largura (m): "))
area(a=altura, l=largura)
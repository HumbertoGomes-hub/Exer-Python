from ex107 import moeda

p = float(input("Digite o valor: "))
print(f"Metade de R${p:.2f} e R${moeda.metade(p):.2f} ")
print(f"O dobro de R${p:.2f} e R${moeda.dobro(p):.2f}")
print(f"Aumento de 10% de R${p:.2f} e R${moeda.aumentar(p):.2f}")
print(f"Reduzindo 13% de R${p:.2f} e R${moeda.diminuir(p):.2f}")




    
    
    
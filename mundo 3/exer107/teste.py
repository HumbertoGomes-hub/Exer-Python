import moeda

p = float(input("Digite o valor: "))
print(f"Metade de R${p} e R${moeda.metade(p)} ")
print(f"O dobro de R${p} e R${moeda.dobro(p)}")
print(f"Aumento de 10% de R${p} e R${moeda.aumentar(p)}")
print(f"Reduzindo 13% de R${p} e R${moeda.diminuir(p)}")

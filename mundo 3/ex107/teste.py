import moeda

valor = float(input("DIGITE O VALOR: "))
print(f"A METADE DE {valor} É {moeda.metade(valor)}")
print(f"O DOBRO DE {valor} É {moeda.dobro(valor)}")
print(f"AUMENTANDO 10% O RESULTADO É {moeda.aumentar(valor)}")
print(f"DIMINUINDO 13% O RESULTADO É {moeda.diminuir(valor)}")
